from odoo import models, fields, api


class division(models.Model):
    _name = 'student.division'
    _description = 'student.division'

    division_name = fields.Char(string='Division Name', required=True)
    division_description = fields.Char(string='Division Description', required=True)
    location = fields.Char(string='Location', required=True)
    contact_num = fields.Integer(string='Contact NUmber')
    d_class_id = fields.Many2one('student.class',string="Class")