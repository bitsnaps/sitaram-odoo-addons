# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) Sitaram Solutions (<https://sitaramsolutions.in/>).
#
#    For Module Support : info@sitaramsolutions.in  or Skype : contact.hiren1188
#
##############################################################################

from odoo import models, fields, api
from odoo.osv import expression


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_barcode_ids = fields.One2many('sr.multi.barcode', 'product_tmpl_id', 'Multi Barcode')


class ProductProduct(models.Model):
    _inherit = 'product.product'

    product_barcode_ids = fields.One2many('sr.multi.barcode', 'product_id', 'Multi Barcode')

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        product_id = self._search(expression.AND(
            [
                ['|', '|', ('name', operator, name), ('default_code', operator, name),
                  '|', ('product_barcode_ids', operator, name), ('barcode', operator, name)
                ],args
            ]), limit=limit)
        return self.browse(product_id).name_get()
        
