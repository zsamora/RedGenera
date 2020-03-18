# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Project(models.Model):
    _inherit = 'project.project'
    expense_id = fields.One2many('hr.expense', 'project_id')
    selling_price = fields.Monetary("Precio de venta", store=True,
                                    currency_field='currency_id',
                                    help="Selling price of project")
    planned_expense = fields.Monetary("Presupuesto de materiales",
                                      store=True, currency_field='currency_id',
                                      help="Expenses planned")
    real_expense = fields.Monetary("Total de gastos", compute='_compute_amount_expense',
                                   store=True, currency_field='currency_id',
                                   help="Real expense in project")
    hours_price = fields.Monetary("Valor de hora", store=True, currency_field='currency_id',
                                  help="Labor cost")
    planned_hours = fields.Float("Presupuesto de horas", compute='_compute_amount_hours_planned',    # TODO: Modificar si se requiere manual solamente
                                 store=True, help="Hours planned")
    value_planned_hours = fields.Monetary("Valor de horas planeado",
                                  compute='_compute_amount_value_planned_hours',
                                store=True, currency_field='currency_id', help="Value of planned hours")
    real_hours = fields.Float("Total de horas trabajadas", compute='_compute_amount_hours_spent',
                                   store=True, help="Real hours worked")
    value_real_hours = fields.Monetary("Valor de horas utilizado",
                              compute='_compute_amount_value_real_hours',
                              store=True, currency_field='currency_id', help="Value of real hours")
    progress = fields.Float("Progreso", compute='_compute_progress_hours',
                            store=True, group_operator="avg", help="Progress status bar")

    @api.depends('expense_id')
    def _compute_amount_expense(self):
        for project in self:
            project.real_expense = sum(
                project.expense_id.mapped('total_amount'))

    @api.depends('task_ids.total_hours_spent')
    def _compute_amount_hours_spent(self):
        for project in self:
            project.real_hours = sum(
                project.task_ids.mapped('total_hours_spent'))

    @api.depends('real_hours', 'hours_price')
    def _compute_amount_value_real_hours(self):
        for project in self:
            project.value_real_hours = project.hours_price * project.real_hours

    @api.depends('task_ids.planned_hours')
    def _compute_amount_hours_planned(self):
        for project in self:
            project.planned_hours = sum(
                project.task_ids.mapped('planned_hours'))

    @api.depends('planned_hours', 'hours_price')
    def _compute_amount_value_planned_hours(self):
        for project in self:
            project.value_planned_hours = project.hours_price * project.planned_hours

    @api.depends('planned_hours', 'real_hours')
    def _compute_progress_hours(self):
        for project in self:
            if project.planned_hours > 0.0:
                if project.real_hours > project.planned_hours:
                    project.progress = 100
                else:
                    project.progress = round(
                        100.0 * project.real_hours / project.planned_hours, 2)
            else:
                project.progress = 0.0


class HrExpense(models.Model):
    _inherit = 'hr.expense'
    project_id = fields.Many2one('project.project')
    bank_reference = fields.Char('N° de transferencia')


class Product(models.Model):
    _inherit = 'product.product'
    store_id = fields.Many2one('res.partner',
                                string='Tienda', store=False)
                                # readonly=True,
                                # related='company_id.partner_id',
    document_type = fields.Selection([
        ('0', 'Boleta'),
        ('1', 'Factura'),
        ('2', 'Ninguno')],
        string="Tipo de Documento", default='1')
