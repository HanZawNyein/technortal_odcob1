from odoo import api, fields, models

class HmsRoom(models.Model):
    _name = 'hms.room' # hms_room
    _description = 'HmsRoom'

    name = fields.Char(required=True)
    type = fields.Selection([
        ('normal', 'Normal'),
        ('vip', 'VIP'),
        ('vvip', 'VVIP'),
    ], default='normal')

    hotel_id = fields.Many2one('hms.hotel',required=True)
    currency_id = fields.Many2one('res.currency',related="hotel_id.currency_id")
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
        }
