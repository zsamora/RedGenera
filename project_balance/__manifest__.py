# -*- coding: utf-8 -*-
{
    'name': "project_balance",

    'summary': """
        Balance de proyectos (horas trabajadas y presupuesto)""",

    'description': """
        Vista de balance de proyectos, con detalle en gráfico de horas y
        presupuesto utilizado en cada uno de los proyectos
    """,

    'author': "zsamora",
    'website': "github.com/zsamora",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','project','hr_expense','hr_timesheet'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/project_balance.xml',
    ],
    'qweb': [
        # "static/src/xml/hr_dashboard.xml",
    ],
}
