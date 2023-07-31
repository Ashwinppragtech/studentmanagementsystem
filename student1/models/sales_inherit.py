from odoo import models,fields,api

class SalesInherit(models.Model):
    _inherit = "sale.order"

    def apply_discount(self):
        for rec in self:
            context_percentage = self._context.get('disc_perc')
            if rec.amount_total:
                rec.amount_total = rec.amount_total - ((rec.amount_total * float(context_percentage)) / 100)


    # def discount_percentage(self):
    #     for record in self:
    #         total = record.amount_total
    #         discount = record.env.context.get('disc_perc')
    #         discount_get = (total * discount) /100
    #         record.amount_total = record.amount_total-discount_get