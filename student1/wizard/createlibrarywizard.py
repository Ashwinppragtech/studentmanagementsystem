from odoo import models, fields, api
from datetime import date


class CreateWizard(models.TransientModel):

    _name="student.wizardlibrary"
    _description = "Create wizard library"

    # lib_id = fields.Many2one('student.library',string='Lib ID',default=lambda self: self.show_id())
    student_id = fields.Many2one('student.student' ,  string = "Student")
    student_name = fields.Char(string='Name',related='student_id.first_name',store= True)
    issue_date = fields.Date(string="Issue Date",default=date.today(),readonly=True)
    return_date = fields.Date(string='Return Date', compute = "_compute_date_difference")
    book_ids = fields.Many2many('student.book')
    days_left = fields.Integer(string="Days left")
    
    # default=lambda self: self.show_id()

    def save_to_another_model(self):
        # Get the target model
        MusicModel = self.env['student.library']
        MusicModel.create({
            'student_id':self.student_id.id,
            'student_name': self.student_name,
            'issue_date': self.issue_date,
            'return_date':self.return_date, 
            'days_left': self.days_left,
            'book_ids':self.book_ids,

        })

    @api.onchange('return_date')
    def _compute_date_difference(self):
        for record in self:
            if record.issue_date and record.return_date and record.issue_date<record.return_date:
                record.days_left = (record.return_date-record.issue_date).days
            else:
                record.days_left = 0
        
    
    # @api.model
    # def show_id(self):
    #     active_id = self.env.context.get('active_id')
    #     if active_id:
    #         print("....................................................................")
    #         self.student_id =  active_id
        
        # active_id = self.env.context.get('active_id')
        # if active_id:
        #     return self.env['student.library'].browse(active_id)
        # current_id=self.env.context.get('active_id')
        # current_record=self.env['student.library'].browse(current_id)
        # for rec in current_record:
        #     self.lib_id=rec.id
        

# default=lambda self: self.show_id()

    def print_report(self):
        model = self.env.context.get('active_model')
        docs = self.env[model].browse(self.env.context.get('active_id'))
        return self.env.ref('student1.student_library_report').report_action(docs)
        

    def action_print_report(self):
        for record in self:
            values = {}
            model = self.env.context.get('active_model')
            docs = self.env[model].browse(self.env.context.get('active_id'))
            data = {'records':self.env['sale.order'].search([],limit=5).ids}
            values.update(data)
            print('................data.........',values,docs)
            return self.env.ref('student1.action_products_report').report_action(docs,data=values)