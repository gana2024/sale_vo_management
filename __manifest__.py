# -*- coding: utf-8 -*-
{
    'name': "Sale VO Management",
    'summary': """
    """,
    'description': """
    """,
    'author': "CDS Solutions SRL",
    'website': "www.cdsegypt.com",
    'version': '0.1',
    'depends': ['sale_management', 'crm','sale_crm'],
    'data': [
         'security/ir.model.access.csv',
         'views/sale_views.xml',
        'views/crm_lead_views.xml',

    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
