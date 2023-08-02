from odoo import models,fields,api

class Sports(models.Model):
    _name = "student.sports"
    _description = "sports"

    sports_event_id = fields.Many2one("student.sportsevent", string = "Sports Event")
    name = fields.Char(string = "Activity Name")
    description = fields.Text(string = "Description")
    date_activity = fields.Date(string = "Date")
    duration = fields.Float(string = "Duration")
    teacher_ids = fields.Many2many("student.teacher",string = "In Charge")
    student_ids = fields.Many2many("student.student")
    first_price = fields.Many2one("student.student",string = "First Prize")
    second_price = fields.Many2one("student.student",string = "Second Prize")
    third_price = fields.Many2one("student.student",string = "Third Prize")

class SportsEvent(models.Model):
    _name = "student.sportsevent"
    _description = "Sports Event"
    _rec_name = "event_name"

    event_name = fields.Char(string = "Event Name")
    event_date = fields.Date(string = "Date")
    sports_type = fields.Char(string = "Sports Type")
    sports_name_ids = fields.One2many("student.sports","sports_event_id", string = "Sports Item")
    sports_item_count = fields.Integer(string = "No Of Sports Item", compute = "get_sports_item_count")

    @api.depends("sports_name_ids")
    def get_sports_item_count(self):
        self.sports_item_count = len(self.sports_name_ids)









