from odoo import models, fields

class FleetTrip(models.Model):
    _name = 'fleet.trip'
    _description = 'Fleet Trip'

    name = fields.Char(string="Trip ID", required=True)

    source = fields.Char(string="Source", required=True)

    destination = fields.Char(string="Destination", required=True)
    
    vehicle_id = fields.Many2one(
        'fleet.vehicle',
        string="Vehicle",
        required=True

    )

    driver_id = fields.Many2one(
        'fleet.driver',
        string="Driver",
        required=True
    )

    cargo_weight = fields.Float(string="Cargo Weight")

    planned_distance = fields.Float(string="Planned Distance (KM)")

    status = fields.Selection([
        ('draft', 'Draft'),
        ('dispatched', 'Dispatched'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], string="Trip Status", default='draft')

    from odoo.exceptions import ValidationError
from odoo import api

@api.constrains('driver_id')
def _check_driver_status(self):
    for record in self:
        if record.driver_id.status == 'suspended':
            raise ValidationError("Suspended driver cannot be assigned to a trip.")

        if record.driver_id.status == 'on_trip':
            raise ValidationError("Driver is already assigned to another trip.")