from odoo import api, fields, models

class ResCompany(models.Model):
    _inherit = 'res.company'

    hms_default_payment_method= fields.Many2one('hms.payment.method', string='Payment Method')