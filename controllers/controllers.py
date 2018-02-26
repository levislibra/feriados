# -*- coding: utf-8 -*-
from openerp import http

# class Feriados(http.Controller):
#     @http.route('/feriados/feriados/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/feriados/feriados/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('feriados.listing', {
#             'root': '/feriados/feriados',
#             'objects': http.request.env['feriados.feriados'].search([]),
#         })

#     @http.route('/feriados/feriados/objects/<model("feriados.feriados"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('feriados.object', {
#             'object': obj
#         })