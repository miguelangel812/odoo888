# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo888(http.Controller):
#     @http.route('/odoo888/odoo888/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo888/odoo888/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo888.listing', {
#             'root': '/odoo888/odoo888',
#             'objects': http.request.env['odoo888.odoo888'].search([]),
#         })

#     @http.route('/odoo888/odoo888/objects/<model("odoo888.odoo888"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo888.object', {
#             'object': obj
#         })
