from odoo import models, fields, api
from datetime import date


class CreateWizard(models.TransientModel):

    _name="student.wizardlibrary"
    _description = "Create wizard library"

    lib_id = fields.Many2one('student.library',string='Lib ID',default=lambda self: self.show_id())
    student_id = fields.Many2one('student.student',related='lib_id.student_id',store=True)
    student_name = fields.Char(string='Name',related='lib_id.student_name',store= True)
    issue_date = fields.Date(string="Issue Date",default=date.today(),readonly=True)
    return_date = fields.Date(string='Return Date',related='lib_id.return_date')
    book_ids = fields.Many2many('student.book')
    days_left = fields.Integer(string="Days left",related='lib_id.days_left')
    
    # default=lambda self: self.show_id()

    def save_to_another_model(self):
        # Get the target model
        MusicModel = self.env['student.library']
        MusicModel.create({
            'student_id':self.student_id.id,
            'student_name': self.student_name,
            'issue_date': self.issue_date,
            'return_date':self.return_date, 
            'book_ids':self.book_ids,

        })
        
    
    @api.model
    def show_id(self):
        active_id = self.env.context.get('active_id')
        if active_id:
            return active_id
        return False
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