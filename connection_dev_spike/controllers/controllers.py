# -*- coding: utf-8 -*-
from odoo import http

# class ConnectionDevSpike(http.Controller):
#     @http.route('/connection_dev_spike/connection_dev_spike/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/connection_dev_spike/connection_dev_spike/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('connection_dev_spike.listing', {
#             'root': '/connection_dev_spike/connection_dev_spike',
#             'objects': http.request.env['connection_dev_spike.connection_dev_spike'].search([]),
#         })

#     @http.route('/connection_dev_spike/connection_dev_spike/objects/<model("connection_dev_spike.connection_dev_spike"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('connection_dev_spike.object', {
#             'object': obj
#         })