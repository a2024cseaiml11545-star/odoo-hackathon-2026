from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date


class FleetDriver(models.Model):
    _name = 'fleet.driver'
    _description = 'Fleet Driver'

    name = fields.Char(string="Driver Name", required=True)

    contact_number = fields.Char(string="Contact Number")

    license_number = fields.Char(string="License Number", required=True)

    license_category = fields.Selection([
        ('lmv', 'LMV'),
        ('hmv', 'HMV'),
        ('transport', 'Transport')
    ], string="License Category", required=True)

    license_expiry_date = fields.Date(string="License Expiry Date", required=True)

    safety_score = fields.Float(string="Safety Score", default=100)

    status = fields.Selection([
        ('available', 'Available'),
        ('on_trip', 'On Trip'),
        ('off_duty', 'Off Duty'),
        ('suspended', 'Suspended')
    ], string="Status", default='available')

    active = fields.Boolean(default=True)

    @api.constrains('license_expiry_date')
    def _check_license_expiry(self):
        for record in self:
            if record.license_expiry_date and record.license_expiry_date < date.today():
                raise ValidationError("Driver license has expired.")