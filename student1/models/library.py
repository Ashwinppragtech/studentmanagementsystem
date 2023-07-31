from odoo import models,fields,api
from datetime import date

class StudentLibrary(models.Model):
    _name = "student.library"
    _description = "studentlibrary"

    student_id = fields.Many2one('student.student',string='Student ID')
    student_name = fields.Char(string='Name',related='student_id.first_name',store= True)
    issue_date = fields.Date(string="Issue Date",default=date.today(),readonly=True)
    return_date = fields.Date(string='Return Date')
    days_left = fields.Integer(string="Days left", compute="_compute_date_difference")
    book_ids = fields.Many2many('student.book',string='book')
    book_serial_number = fields.Char(string="Serial Number",related='book_ids.book_serial_number')
    book_is_available = fields.Boolean(string="Is available",related="book_ids.is_available",store=True)

    
    
    @api.onchange('return_date')
    def _compute_date_difference(self):
        for record in self:
            if record.issue_date and record.return_date and record.issue_date<record.return_date:
                record.days_left = (record.return_date-record.issue_date).days
            else:
                record.days_left = 0


    def approve(self):
        rec=self.env['student.book'].search([('book_serial_number','=',self.book_serial_number)])
        rec.write({
            'is_available':False,
        })    
    def returned(self):
        rec=self.env['student.book'].search([('book_serial_number','=',self.book_serial_number)])
        rec.write({
            'is_available':True,
        })  



class StudentBook(models.Model):
    _name = "student.book"
    _description = "studentbook"
    rec_name = "book_name"

    book_serial_number = fields.Char(string="Serial Number")
    book_name = fields.Char(string="Book Name")
    auther = fields.Char(string="Auther")
    is_available = fields.Boolean(string="Is Available",default=True,readonly=True)
    # library_id = fields.Many2one("student.library")
