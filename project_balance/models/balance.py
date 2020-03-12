# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Project(models.Model):
    _inherit = 'project.project'
    expense_id = fields.One2many('hr.expense', 'project_id')


class Task(models.Model):
    _inherit = 'project.task'
    # expense_id = fields.One2many('hr.expense', 'project_id')
    planned_budget = fields.Float("", default=0.0)  # change to Monetary
    real_budget = fields.Float("", default=0.0)
    # hours_type = fields.One2many('hours.type', 'task_id', string='Hour Type')

    @api.onchange('planned_hours')
    def _onchange_project_id_expense(self):
        self.planned_budget = self.planned_hours * 10
        if self.hours_type.type == 'Planned':
            self.hours = self.planned_hours


class HrExpense(models.Model):
    _inherit = 'hr.expense'
    project_id = fields.Many2one('project.project')
    bank_reference = fields.Char('N° de transferencia')

# class HoursType(models.Model):
#    _name = 'hours.type'
#    type = fields.Char(string="Type",store=True)
#    hours = fields.Float(string="Hours", help='Group of hours', tracking=True,
#                         default=1, store=True)
#    task_id = fields.Many2one('project.task', string='Task')


# class HrAttendance(models.Model):
#    _inherit = 'hr.attendance'
#    project_id = fields.Many2one('project.project')
