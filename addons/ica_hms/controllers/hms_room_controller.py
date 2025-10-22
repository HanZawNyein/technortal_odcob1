from odoo import http
from odoo.http import request

class HMSRoomController(http.Controller):
    # @http.route('/api/hms_room',type='http',auth='user')
    # def hms_room(self,**kwargs):
    #     rooms_ids = request.env['hms.room'].sudo().search([])
    #     return http.request.render('ica_hms.hms_room', {'room_ids':rooms_ids})

    @http.route('/api/hms_room',type='jsonrpc',auth='user')
    def hms_room(self,**kwargs):
        limit = kwargs.get('limit',1)
        offset = kwargs.get('offset',0)
        order = kwargs.get('order','id desc')
        room_ids = request.env['hms.room'].sudo().search_read([],fields=['id','display_name','type'],limit=limit,offset=offset,order=order)
        return {'room_ids': room_ids}