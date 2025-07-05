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
    def event_rsvp(self, registration_id, access_token=None, **kwargs):
        registration = request.env["event.registration"].sudo().browse(registration_id)
        if not registration.exists():
            _logger.error("Registration with ID %s does not exist.", registration_id)
            return request.not_found()
        else:
            _logger.info("Processing RSVP for registration ID: %s", registration_id)
        if access_token and registration.access_token != access_token:
            _logger.warning(
                "Access token mismatch for registration ID %s. Provided: %s, Expected: %s",
                registration_id,
                access_token,
                registration.access_token,
            )
            return request.not_found()
        else:
            _logger.info(
                "Access token verified for registration ID %s. Proceeding with RSVP.",
                registration_id,
            )
            return request.render(
                "event_rsvp.RSVP_prompt",
                {
                    "registration": registration,
                },
            )

    @route(
        ["/rsvp/<int:registration_id>/confirm"],
        type="http",
        auth="public",
        website=True,
    )
    def event_rsvp_confirm(self, registration_id, access_token=None, **kwargs):
        pass

    @route(
        ["/rsvp/<int:registration_id>/cancel"],
        type="http",
        auth="public",
        website=True,
    )
    def event_rsvp_cancel(self, registration_id, access_token=None, **kwargs):
        pass
