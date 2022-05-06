# -*- coding: utf-8 -*-
{
    'name': "Session Dinamica",

    'summary': """
        """,

    'description': """
    """,

    'author': "Synergia Profesional SAS",
    'website': "http://www.synergiaprofesional.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Préstamo',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['prestamo', 'prestamo_zona'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',

    ],
}
