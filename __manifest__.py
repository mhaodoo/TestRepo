# -*- coding: utf-8 -*-
# Copyright (C) 2017-Today  Technaureus Info Solutions(<http://technaureus.com/>).
{
    'name': 'Saudi VAT Invoice',
    'version': '13.0.0.1',
    'sequence':1,
    'category': 'Accounting',
    'summary': 'Saudi VAT Invoice',
    'author': 'Technaureus Info Solutions Pvt. Ltd.',
    'website': 'http://www.technaureus.com/',
    'price': 15,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'description': """
This module is for Saudi VAT Invoice
        """,
    'depends': ['account','sa_uae_vat'],
    'data': [
        'report/saudi_report_layout.xml',
        'report/saudi_vat_invoice_report_template.xml',
        'report/saudi_vat_invoice_report.xml',
        'views/vat_invoice_view.xml',
    ],
    'images': ['images/main_screenshot.png'],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
