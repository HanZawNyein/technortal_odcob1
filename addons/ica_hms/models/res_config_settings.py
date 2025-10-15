from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    hms_default_payment_method= fields.Many2one('hms.payment.method', string='Payment Method',
                                                related='company_id.hms_default_payment_method',readonly=False)