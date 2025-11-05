from odoo import api, fields, models

class HmsRoom(models.Model):
    _name = 'hms.room' # hms_room
    _inherit = ['image.mixin']
    _description = 'HmsRoom'

    name = fields.Char(required=True)

    _hms_room_name_unique = models.Constraint(
        'unique(name)',
        'Room name already exists.',
    )

    type = fields.Selection([
        ('normal', 'Normal'),
        ('vip', 'VIP'),
        ('vvip', 'VVIP'),
    ], default='normal')

    # hotel_id = fields.Many2one('hms.hotel',required=True)
    company_id = fields.Many2one('res.company',required=True)
    currency_id = fields.Many2one('res.currency',related="company_id.currency_id")
    amount = fields.Monetary(currency_field='currency_id')
    active = fields.Boolean(default=True)
    booking_ids = fields.One2many('hms.booking','room_id', string='Bookings')
    booking_count = fields.Integer(compute='_compute_booking_count')





    @api.depends('booking_ids')
    def _compute_booking_count(self):
        for rec in self:
            rec.booking_count = len(rec.booking_ids)


    def action_view_bookings(self):
        return {
            "name":f"{self.name}'s bookings",
            "view_mode":"list,form",
            "domain":[("id","in",self.booking_ids.ids)],
            "type":"ir.actions.act_window",
            "res_model":"hms.booking",
            "context":{"default_company_id":self.company_id.id,"default_room_id":self.id},
        }


