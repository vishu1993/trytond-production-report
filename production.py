# -*- coding: utf-8 -*-
"""
    production.py

    :copyright: (c) 2014 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from openlabs_report_webkit import ReportWebkit

from trytond.transaction import Transaction
from trytond.pool import Pool, PoolMeta


__metaclass__ = PoolMeta
__all__ = ['ProductionReport']


class ProductionReport(ReportWebkit):
    __name__ = 'production.report'

    @classmethod
    def wkhtml_to_pdf(cls, data, options=None):
        """
        Call wkhtmltopdf to convert the html to pdf
        """
        Company = Pool().get('company.company')

        company = ''
        if Transaction().context.get('company'):
            company = Company(Transaction().context.get('company')).party.name
        options = {
            'margin-bottom': '0.50in',
            'margin-left': '0.50in',
            'margin-right': '0.50in',
            'margin-top': '0.50in',
            'footer-font-size': '8',
            'footer-left': company,
            'footer-line': '',
            'footer-right': '[page]/[toPage]',
            'footer-spacing': '5',
        }
        return super(ProductionReport, cls).wkhtml_to_pdf(
            data, options=options
        )