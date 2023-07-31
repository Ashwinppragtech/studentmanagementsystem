from odoo import models,fields,api

class Sports(models.Model):
    _name = "student.sports"
    _description = "sports"

    name = fields.Char(string = "Activity Name")
    description = fields.Text(string = "Description")
    date_activity = fields.Date(string = "Date")
    duration = fields.Float(string = "Duration")
    teacher_ids = fields.Many2many("student.teacher",string = "In Charge")
    student_ids = fields.Many2many("student.student")
    first_price = fields.Many2one("student.student",string= "First Prize")
    second_price = fields.Many2one("student.student",string= "Second Prize")
    third_price = fields.Many2one("student.student",string= "Third Prize")

