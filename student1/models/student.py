from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import date
from odoo.exceptions import ValidationError
import re

class Student(models.Model):
    _name = 'student.student'
    _description = 'Student'
    _rec_name = 'seq'

    

    seq = fields.Char(string = 'Sequence',required = True,readonly = True,copy = False,default = 'New')
    first_name = fields.Char(string ='First Name')
    last_name = fields.Char(string ='Last Name')
    class_id = fields.Many2one('student.class',string = 'class')
    dob = fields.Date(string = 'Date of Birth' )
    grade = fields.Selection([('A','A'),
                         ('B','B'),
                         ('C','C'),
                         ('D','D')],string = 'Grade',default='A')
    contact_num = fields.Char(string = 'Contact Number')
    e_mail = fields.Char(string = 'E-mail')
    schedule_s = fields.Datetime(string = 'schedule',related = 'class_id.schedule')
    age = fields.Integer(string = 'Age',compute = '_compute_age')
    status = fields.Selection([('drafted','Drafted'),
                                       ('confirmed','Confirmed'),
                                       ('rejected','Rejected')],string='Status',default='drafted')

    def confirm(self):
        self.status = "confirmed"

    def reject(self):
        self.status = "rejected"

    @api.depends('status')
    def _compute_status_color(self):
        for record in self:
            if record.status == 'drafted':
                record.status_color = 1  # Green color
            elif record.status == 'confirmed':
                record.status_color = 0  # Yellow color
            elif record.status == 'rejected':
                record.status_color = 2  # Red color

    status_color = fields.Integer(compute='_compute_status_color', string='Status Color')

    @api.depends('dob')
    def _compute_age(self):
        # print("-------------------self---------------------",self)
        for rec in self:
            delta = relativedelta(date.today(),rec.dob)
            # print("-------------------------delta------------------------------------",delta)
            rec.age = delta.years

    @api.constrains('e_mail')
    def _validate_email(self):
        for record in self:
            if record.e_mail and not self._is_valid_email(record.e_mail):
                raise ValidationError('Invalid email address')
            
    @api.constrains('contact_num')
    def _check_number_length(self):
        for record in self:
            if record.contact_num and len(record.contact_num) != 10:
                raise ValidationError('Number must be exactly 10 digits')

    @staticmethod
    def _is_valid_email(email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return bool(re.match(pattern, email))
    
    @api.model
    def create(self, vals):
        if vals.get('seq',('New')) == ('New'):
            vals['seq'] = self.env['ir.sequence'].next_by_code('student1.Student.seq') or ('New')
        res = super(Student, self).create(vals)
        return res
    
    def action_smartbutton_library(self):
        return{
            'name':'Library Details',
            'type':'ir.actions.act_window',
            'res_model':'student.library',
            'domain':[('student_id','=',self.id)],
            'view_mode':'tree,form',
            'target':'current',
            }

    def action_smartbutton_class(self):
        return{
            'name':'Class Details',
            'type':'ir.actions.act_window',
            'res_model':'student.class',
            'domain':[('student_ids','=',self.id)],
            'view_mode':'tree,form',
            'target':'current',
            }


    # scheduled action

    def display_state(self):
            print("...............Scheduled Action is Active.........................")

    # email action , sent email using button
    def send_email_action(self):
        template_id = self.env.ref('student1.email_template_id')    
        template_id.send_mail(self.id, force_send=True)
        print("----------------Email genarated---------------")

   
    # sent email to all records all email ids in the record using 'Action scheduler'    
    def send_email_action_crown(self):
        print("----------------Again printed---------------")
        st = self.search([])
        for rec in st:
            template_id = rec.env.ref('stdefault_wizard_field1udent1.email_template_id')
            email_values = {
                'email_to': rec.e_mail,
            }
            template_id.send_mail(rec.id, force_send=True, email_values=email_values)
            print("----------------Email genarated---------------")


    def action_open_wizard(self):
        # Prepare the context to pass data from the form view to the wizard
        context = {
            'default_student_id': self.id  # Pass values from your form view fields
        }

        # Open the wizard using an action
        return {
            'name': 'Wizard Title',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'student.wizardlibrary',
            'target': 'new',
            'type': 'ir.actions.act_window',
            'context': context,
        }


    # def write(self, vals):
    #     print("_______________________________write method is triggered______________________",vals)
    #     return super(Student,self).write(vals)

    # def unlink(self):
    #     print("__________test__________")
    #     if self.first_name=='student4':
    #         raise ValidationError("You cannot delete record having first name student4")
    #     return super(Student,self).unlink()
    
    # @api.model
    # def default_get(self, fields):
    #     vals = super(Student, self).default_get(fields)
    #     print("fields==========================", fields)
    #     print("vals==========================", vals)
    #     vals['e_mail'] = 'example@gmail.com'
    #     return vals

    # url_action
    # def action_url(self):
    #     return {
    #         'type':'ir.actions.act_url',
    #         'target':'self',
    #         'url':'https://runbot.odoo.com/'
    #         }
    
    
    # def name_get(self):
    #     result = []
    #     for record in self:
    #         name=record.first_name+" "+record.last_name
    #         result.append((record.id,name)) # Customize the display name as needed
    #     return result

    
    # @api.model
    # def default_get(self,fields):
    #     res=super(Student,self).default_get(fields)
    #     print("______test__________")


    
    # @api.model
    # def create(self, vals):
    #     print("creat ca+++++++++")
    #     vals['e_mail'] = "suuuiiiiiiiiiiii"
    #     res = super(Student, self).create(vals)
    #
    #     return res

    # def write(self, vals):
    #     print("write ca+++++++++")
    #     vals['e_mail'] = "suuuiiiiiiiiiiii"
    #     res = super(Student, self).write(vals)
    #
    #     record = self.env['student.student'].search([('first_name', "=", "student1")])
    #     print('=========================', record)
    #     vals={
    #         'first_name': 'student1',
    #         'last_name': 'p'
    #     }
    #     new_rec = self.env['student.student'].create(vals)
    #     print("----------------------------------------",new_rec)
    #
    #     browse_rec = self.env['student.student'].browse([1])
    #     print(browse_rec, "---------------===================================")
    #     print(browse_rec.first_name, "---------------===================================")
    #
    #     record.unlink()
    #