from odoo import models, fields, _


class EventRegistration(models.Model):
    _inherit = "event.registration"

    state = fields.Selection(
        selection_add=[("rsvp", "Confirmed"), ("done",)],
        ondelete={"rsvp": "set default"},
    )
