from odoo import models, fields, api


class StudentClass(models.Model):
    _name = 'student.class'
    _description = 'student.studentClass'
    _rec_name='class_name'

    class_name = fields.Char(string='Class Name', required=True)
    class_description = fields.Char(string='Class Description')
    schedule = fields.Datetime(string='Schedule', required=True)
    specialization = fields.Char(string='Specialization')
    teacher_id = fields.Many2many('student.teacher')
    student_ids = fields.One2many('student.student','class_id',string='Student')
    division_ids = fields.Many2many('student.division')
    subject_ids=fields.One2many('student.subject','class_id',string="Subject")
    student_count = fields.Integer(string="Student Count",default=0,compute="compute_student_count")


    @api.depends('student_ids')
    def compute_student_count(self):
        self.student_count = len(self.student_ids)

        


    # def name_get(self):class_name
    #     result = []
    #     for rec in self:
    #         name = rec.class_name + ' ' + rec.class_description
    #         result.append((rec.id, name))
    #     return result