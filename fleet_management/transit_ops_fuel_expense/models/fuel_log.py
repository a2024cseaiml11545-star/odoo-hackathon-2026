from odoo import models, fields

class FuelLog(models.Model):
    _name = 'fuel.log'
    _description = 'Fuel Log'

    vehicle = fields.Char(string="Vehicle")
    driver = fields.Char(string="Driver")
    fuel_date = fields.Date(string="Fuel Date")
    fuel_type = fields.Selection([
        ('petrol','Petrol'),
        ('diesel','Diesel'),
        ('cng','CNG')
    ], string="Fuel Type")

    liters = fields.Float(string="Liters")
    price_per_liter = fields.Float(string="Price/Liter")
    total_cost = fields.Float(string="Total Cost")
    odometer = fields.Float(string="Odometer")