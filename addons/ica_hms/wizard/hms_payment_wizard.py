from odoo import api, fields, models

class HmsPaymentWizard(models.TransientModel):
    _name = 'hms.payment.wizard'
    _description = 'HmsPaymentWizard'

    payment_method_id = fields.Many2one('hms.payment.method',required=True)
    amount = fields.Monetary(string='Amount', required=True)
    currency_id = fields.Many2one('res.currency', string='Currency',related='payment_method_id.currency_id')

    # @api.model
    # def create(self, values):
    #     # Add code here
    #     result = super(HmsPaymentWizard, self).create(values)
    #     booking_model = self.env.context.get('active_model') # hms.booking
    #     booking_id = self.env.context.get('active_id') # database ID
    #     record = self.env[booking_model].browse(booking_id)
    #     record.action_paid()
    #     return result

    def action_create_payment(self):
        booking_model = self.env.context.get('active_model') # hms.booking
        booking_id = self.env.context.get('active_id') # database ID
        record = self.env[booking_model].browse(booking_id)
        record.action_paid()