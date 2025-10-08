from odoo import api, fields, models, _
from odoo.exceptions import UserError


class HmsBooking(models.Model):
    _name = 'hms.booking'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'HmsBooking'
    _rec_name = "partner_id"

    partner_id = fields.Many2one('res.partner', required=False, tracking=True,copy=False)
    category_ids = fields.Many2many('res.partner.category',related="partner_id.category_id")
    room_id = fields.Many2one('hms.room', required=True, tracking=True,copy=True)
    hotel_id = fields.Many2one('hms.hotel', related="room_id.hotel_id")
    currency_id = fields.Many2one('res.currency', related="room_id.currency_id")
    amount = fields.Monetary(tracking=True,currency_field='currency_id')
    reference = fields.Char(default=lambda self: _("New"), readonly=True,copy=False)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('paid', 'Paid'),
        ('check_in', 'Check In'),
        ('check_out', 'Check Out'),
        ('cancelled', 'Cancelled'),
    ], default='draft', tracking=True)
    check_in_datetime = fields.Datetime(tracking=True,copy=False,readonly=True)
    check_out_datetime = fields.Datetime(tracking=True,copy=False,readonly=True)

    @api.onchange('room_id')
    def _onchange_room(self):
        if self.room_id:
            self.amount = self.room_id.amount

    # @api.model
    # def create(self, values):
    #
    #     return super(HmsBooking, self).create(values)

    @staticmethod
    def _allow_states():
        return [
            ('draft', 'confirmed'),
            ('confirmed', 'draft'),
            ('confirmed', 'paid'),
            ('paid', 'check_in'),
            ('check_in', 'check_out'),
            ('confirmed', 'cancelled'),
            ('draft', 'cancelled'),
        ]

    def _change_state(self,new_state):
        if (self.state,new_state) not in self._allow_states():
            raise UserError(_(f'{self.state} to {new_state} is not allowed.'))
        self.state=new_state

    def action_draft(self):
        self._change_state('draft')

    def action_confirm(self):

        if not self.partner_id:
            raise UserError(_('You need to enter a customer.'))
        if not self.reference or self.reference == _("New"):
           self.reference = self.env['ir.sequence'].next_by_code('hms.booking')
        self._change_state('confirmed')

    def action_paid(self):
        self._change_state('paid')

    def action_check_in(self):
        self._change_state('check_in')
        self.check_in_datetime = fields.Datetime.now()

    def action_check_out(self):
        self._change_state('check_out')
        self.check_out_datetime = fields.Datetime.now()

    def action_cancel(self):
        self._change_state('cancelled')
