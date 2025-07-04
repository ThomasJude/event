import logging

from odoo.http import Controller, route, request

_logger = logging.getLogger(__name__)


class EventController(Controller):
    @route(
        ["/rsvp/<int:registration_id>"],
        type="http",
        auth="public",
        website=True,
    )
    def event_rsvp(self, registration_id, **kwargs):
        registration = request.env["event.registration"].sudo().browse(registration_id)
        if registration:
            if registration.state == "open":
                registration.state = "rsvp"
        return
