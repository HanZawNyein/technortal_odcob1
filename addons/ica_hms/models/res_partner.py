from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    date_of_birth = fields.Date()
    age = fields.Integer(compute="_compute_age")

    @api.depends('date_of_birth')
    def _compute_age(self):
        today = fields.Date.today()
        for rec in self:
            if rec.date_of_birth:
                # Compute full years
                rec.age = today.year - rec.date_of_birth.year - (
                        (today.month, today.day) < (rec.date_of_birth.month, rec.date_of_birth.day)
                )
            else:
                rec.age = 0