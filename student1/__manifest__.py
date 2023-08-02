# -*- coding: utf-8 -*-
{
    'name': "student1",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base','website','sale'],

    # always loaded
    'data': [
        'data/ir_sequence_data.xml',
        'data/cron.xml',
        'data/email_template.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizard/createlibrarywizard_view.xml',
        'views/views.xml',
        'views/student_view.xml',
        'views/teacher_view.xml',
        'views/classes_view.xml',
        'views/division_view.xml',
        'views/subject_view.xml',
        'views/library_view.xml',
        'views/book_view.xml',
        'views/saleorder_view.xml',
        'views/sports_view.xml',
        'views/sportsevent_view.xml',
        'reports/student_profile.xml',
        'reports/student_id_card.xml',
        'reports/library_report.xml',
        'reports/product_report_table.xml',
        'reports/sports_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
