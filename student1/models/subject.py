from odoo import models,fields,api

class StudentSubject(models.Model):
    _name = 'student.subject'
    _description = 'subject.studentsubject'
    # _rec_name = 'subject_id'

    subject = fields.Char(string = 'Subject ID')
    subject_name = fields.Selection([
        ('maths','Maths'),
        ('hindi','Hindi'),
        ('english','English'),
        ('computer_science','Computer Science')
    ],string= 'Subject Name')
    class_id = fields.Many2one('student.class')
    teacher_id = fields.Many2one('student.teacher', string='Teacher')
