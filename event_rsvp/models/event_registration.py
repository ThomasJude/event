from odoo import models, fields, _, api


class EventRegistration(models.Model):
    _inherit = "event.registration"

    state = fields.Selection(
        selection_add=[("rsvp", "Confirmed"), ("done",)],
        ondelete={"rsvp": "set default"},
    )

    access_token = fields.Char(
        string="Access Token", help="Token used to access the RSVP link."
    )

    @api.model_create_multi
    def create(self, val_list):
        for vals in val_list:
            vals["access_token"] = self.create_access_token()
        return super(EventRegistration, self).create(val_list)  # noqa

    @api.model
    def create_access_token(self):
        """Generate a unique access token for the registration."""
        import secrets

        return secrets.token_urlsafe(16)

    def action_rsvp(self):
        self.write({"state": "rsvp"})
