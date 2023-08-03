# -*- coding: utf-8 -*-
from odoo import fields, models


class AccountTax(models.Model):
    _inherit = 'account.tax'

    # To this case the options in selection field are in Spanish, because are
    # only three options and We need that value to set in the CFDI
    l10n_mx_cfdi_tax_key = fields.Selection(
        [('001', '[001] Retención ISR'),
         ('002', '[002] Retención IVA'),
         ('003', '[003] Retención IEPS'),
         ('004', '[004] Impuesto Local'),], 'Tax Key',
        help='The CFDI version 4.0 have the attribute "Impuesto" in the tax '
        'lines. The Tax Catalog specifies which are the Tax Keys transferred and '
        'taxes withheld, linked to the concepts of Digital Tax Receipts on the Internet.')
