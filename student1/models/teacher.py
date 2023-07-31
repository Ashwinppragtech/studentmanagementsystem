from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import date


class teacher(models.Model):
    _name = 'student.teacher'
    _description = 'student.teacher'
    _rec_name='first_name'

    t_seq = fields.Char(string="sequence",required = True,readonly = True,copy = False,default = 'New')
    t_class_ids=fields.Many2many('student.class','teacher_id')
    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    dob = fields.Date(string='Date of Birth')
    specialization = fields.Char(string='Specialization')
    contact_num = fields.Char(string='Contact Number')
    e_mail = fields.Char(string='E-mail')
    age=fields.Integer(string="Age",compute="_compute_age")

    @api.depends('dob')
    def _compute_age(self):
        for rec in self:
            delta = relativedelta(date.today(), rec.dob)
            rec.age = delta.years

    @api.model
    def create(self, vals):
        if vals.get('t_seq',('New')) == ('New'):
            vals['t_seq'] = self.env['ir.sequence'].next_by_code('student1.teacher.seq') or ('New')
        res = super(teacher, self).create(vals)
        return res