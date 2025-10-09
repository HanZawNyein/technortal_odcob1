from odoo import api, fields, models

class HmsHotel(models.Model):
    _name = 'hms.hotel'
    _inherit = ['image.mixin']
    _description = 'HmsHotel'

    name = fields.Char()
    room_ids = fields.One2many('hms.room', 'hotel_id')
    currency_id = fields.Many2one('res.currency',required=True)

    def action_create_booking(self):
        return {
            "name": f"{self.name}'s create booking",
            "type":"ir.actions.act_window",
            "res_model": "hms.booking",
            "view_mode": "form",
            "target": "new",
            "context":{"default_hotel_id":self.id},
        }