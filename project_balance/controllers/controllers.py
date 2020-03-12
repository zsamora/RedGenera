# -*- coding: utf-8 -*-
from odoo import http


#class ProjectBalance(http.Controller):
#    @http.route('/project_balance/', auth='public')
#    def index(self, **kw):
#        return http.request.render('project_balance.project_balance_graph',{})

#     @http.route('/project_balance/project_balance/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_balance.listing', {
#             'root': '/project_balance/project_balance',
#             'objects': http.request.env['project_balance.project_balance'].search([]),
#         })

#     @http.route('/project_balance/project_balance/objects/<model("project_balance.project_balance"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_balance.object', {
#             'object': obj
#         })
