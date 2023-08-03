# -*- coding: utf-8 -*-
from odoo import models


class AccountEdiFormat(models.Model):
    _inherit = 'account.edi.format'

    def _is_required_for_invoice(self, invoice):
        # OVERRIDE
        self.ensure_one()
        if self.code != 'cfdi_3_3' and invoice.l10n_mx_edi_sign_required is True:
            return super()._is_required_for_invoice(invoice)

        # Determine on which invoices the Mexican CFDI must be generated.
        return invoice.move_type in ('out_invoice', 'out_refund') and \
            invoice.country_code == 'MX' and invoice.l10n_mx_edi_sign_required
