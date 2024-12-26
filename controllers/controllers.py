# -*- coding: utf-8 -*-
# from odoo import http


# class VitaData(http.Controller):
#     @http.route('/vita_data/vita_data', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vita_data/vita_data/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vita_data.listing', {
#             'root': '/vita_data/vita_data',
#             'objects': http.request.env['vita_data.vita_data'].search([]),
#         })

#     @http.route('/vita_data/vita_data/objects/<model("vita_data.vita_data"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vita_data.object', {
#             'object': obj
#         })

