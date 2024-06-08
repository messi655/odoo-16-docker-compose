# -*- coding: utf-8 -*-
{
    'name': "rest-api",

    'summary': """
        A API for external application access to Odoo system to perform CRUD.""",

    'description': """
        This API help external application can interactive with Odoo system via REST HTTP with data format JSON.
    """,

    'author': "rest-api",
    'website': "https://www.helloworld.py",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'developers',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    "application": True,
    "installable": True,
    "auto_install": False,

    'external_dependencies': {
        'python': ['pypeg2']
    }
}
