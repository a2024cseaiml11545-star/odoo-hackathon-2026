from odoo import models, fields, api
from odoo.exceptions import ValidationError


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

    @api.constrains('driver_id')
    def _check_driver_status(self):
        for record in self:
            if record.driver_id.status == 'suspended':
                raise ValidationError("Suspended driver cannot be assigned to a trip.")

            if record.driver_id.status == 'on_trip':
                raise ValidationError("Driver is already assigned to another trip.")

    def action_dispatch(self):
        for record in self:
            record.status = 'dispatched'
            record.driver_id.status = 'on_trip'
            if record.vehicle_id:
                record.vehicle_id.status = 'on_trip'

    def action_complete(self):
        for record in self:
            record.status = 'completed'
            record.driver_id.status = 'available'
            if record.vehicle_id:
                record.vehicle_id.status = 'available'

    def action_cancel(self):
        for record in self:
            record.status = 'cancelled'
            record.driver_id.status = 'available'
            if record.vehicle_id:
                record.vehicle_id.status = 'available'