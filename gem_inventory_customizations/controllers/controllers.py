# -*- coding: utf-8 -*-
# from odoo import http


# class InventoryCustomizations(http.Controller):
#     @http.route('/inventory_customizations/inventory_customizations', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inventory_customizations/inventory_customizations/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('inventory_customizations.listing', {
#             'root': '/inventory_customizations/inventory_customizations',
#             'objects': http.request.env['inventory_customizations.inventory_customizations'].search([]),
#         })

#     @http.route('/inventory_customizations/inventory_customizations/objects/<model("inventory_customizations.inventory_customizations"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inventory_customizations.object', {
#             'object': obj
#         })
