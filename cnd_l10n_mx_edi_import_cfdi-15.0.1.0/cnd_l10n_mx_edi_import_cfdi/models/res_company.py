# -*- coding: utf-8 -*-
from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    def _get_default_category_id(self):
        # Deletion forbidden (at least through unlink)
        return self.env.ref('product.product_category_all')

    create_products = fields.Boolean(
        string='Create Products',
        default=False,
        help='If marked, product in the xml file are going to be created.')
    product_type_default = fields.Selection(
        selection=[
            ('consu', 'Consumable'),
            ('service', 'Service'),
            ('product', 'Storable Product')],
        string='Product Type',
        default='service',
        help='A storable product is a product for which you manage stock. The Inventory app has to be installed.\n'
             'A consumable product is a product for which stock is not managed.\n'
             'A service is a non-material product you provide.')
    product_categ_id_default = fields.Many2one(
        'product.category',
        string='Product Category',
        default=_get_default_category_id,
        help="Select category for the current product")
