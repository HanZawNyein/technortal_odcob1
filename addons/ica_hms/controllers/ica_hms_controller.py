from odoo.http import request, route, Controller


class IcaHmsController(Controller):
    @route("/ica_hms/standalone_app", auth="public")
    def standalone_app(self):
        return request.render(
            'ica_hms.standalone_app',
            {
                'session_info': request.env['ir.http'].get_frontend_session_info(),
            }
        )
