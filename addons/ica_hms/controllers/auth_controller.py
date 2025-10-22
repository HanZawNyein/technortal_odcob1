from odoo import http
from odoo.http import request

class HMSRoomController(http.Controller):
    @http.route('/api/login',type='jsonrpc',auth='none')
    def api_login(self,**kwargs):
        login = kwargs.get('login')
        password = kwargs.get('password')
        credential = {'login': login, 'password': password, 'type': 'password'}
        auth_info = request.session.authenticate(request.env, credential)
        return {'auth_info': auth_info,"message":"login successfully."}