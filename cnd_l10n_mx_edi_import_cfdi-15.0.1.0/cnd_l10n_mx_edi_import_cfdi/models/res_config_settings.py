# -*- coding: utf-8 -*-
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    create_products = fields.Boolean(
        string='Create Products',
        related='company_id.create_products',
        readonly=False,
        help='If marked, product in the xml file are going to be created.')
    product_type_default = fields.Selection(
        string='Product Type',
        related='company_id.product_type_default',
        readonly=False,
        help='A storable product is a product for which you manage stock. The Inventory app has to be installed.\n'
             'A consumable product is a product for which stock is not managed.\n'
             'A service is a non-material product you provide.')
    product_categ_id_default = fields.Many2one(
        'product.category',
        string='Product Category',
        related='company_id.product_categ_id_default',
        readonly=False,
        help="Select category for the current product")