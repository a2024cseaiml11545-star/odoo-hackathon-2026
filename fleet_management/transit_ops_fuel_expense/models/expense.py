from odoo import models, fields

class Expense(models.Model):
    _name = 'vehicle.expense'
    _description = 'Vehicle Expense'

    expense_name = fields.Char(string="Expense Name", required=True)
    vehicle = fields.Char(string="Vehicle")
    expense_type = fields.Selection([
        ('maintenance', 'Maintenance'),
        ('fuel', 'Fuel'),
        ('insurance', 'Insurance'),
        ('repair', 'Repair'),
        ('other', 'Other')
    ], string="Expense Type")

    amount = fields.Float(string="Amount")
    expense_date = fields.Date(string="Expense Date")
    description = fields.Text(string="Description")

    status = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('paid', 'Paid')
    ], default='draft', string="Status")