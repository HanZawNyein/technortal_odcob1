from odoo import http
from odoo.http import request


class HMSRoomController(http.Controller):
    # @http.route('/api/hms_room',type='http',auth='user')
    # def hms_room(self,**kwargs):
    #     rooms_ids = request.env['hms.room'].sudo().search([])
    #     return http.request.render('ica_hms.hms_room', {'room_ids':rooms_ids})

    @http.route('/api/hms_room', type='jsonrpc', auth='user')
    def hms_room(self, **kwargs):
        limit = kwargs.get('limit', 1)
        offset = kwargs.get('offset', 0)
        order = kwargs.get('order', 'id desc')
        room_ids = request.env['hms.room'].sudo().search_read([], fields=['id', 'display_name', 'type'], limit=limit,
                                                              offset=offset, order=order)
        return {'room_ids': room_ids}

    @http.route('/api/hms_room/create/<string:name>/<model("res.company"):company_id>', type='jsonrpc', auth='user')
    # @http.route('/api/hms_room/create/<string:name>/<int:company_id>', type='jsonrpc', auth='user')
    def hms_room(self, name, company_id, **kwargs):
        room_id = request.env['hms.room'].create({'name': name, 'company_id': company_id.id})
        return {'room_id': room_id.read()}
