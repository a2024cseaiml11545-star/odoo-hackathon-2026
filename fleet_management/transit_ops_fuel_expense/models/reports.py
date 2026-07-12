from odoo import models, fields

class FuelExpenseReport(models.Model):
    _name = 'fuel.expense.report'
    _description = 'Fuel Expense Report'

    report_name = fields.Char(string="Report Name")
    total_fuel_cost = fields.Float(string="Total Fuel Cost")
    total_expense = fields.Float(string="Total Expense")
    total_trips = fields.Integer(string="Total Trips")
    generated_on = fields.Date(string="Generated On")