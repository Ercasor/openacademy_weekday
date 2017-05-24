# -*- coding: utf-8 -*-
{
    'name': "Open Academy Weekdays",

    'summary': """Manage trainings""",

    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
            - weekdays
    """,

    'author': "Ernesto",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'openacademy'],

    # always loaded
    'data': [
        # 'security/security.xml',
        # 'security/ir.model.access.csv',
        # 'templates.xml',
        'views/courses.xml',
        # 'views/partner.xml',
        # 'views/session_workflow.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo.xml',
    ],
    'installable': True,
    'active': False,
}
