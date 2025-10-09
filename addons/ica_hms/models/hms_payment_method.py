from odoo import api, fields, models

class HmsPaymentMethod(models.Model):
    _name = 'hms.payment.method'
    _description = 'HmsPaymentMethod'

    name = fields.Char(required=True)
    currency_id = fields.Many2one('res.currency')
    image = fields.Image()