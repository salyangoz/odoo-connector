import urllib.parse
from odoo import http
from odoo.http import request

YENGEC_SETUP_URL = 'https://app.yengec.co/auth/callback/odoo'
YENGEC_API_KEY_PARAM = 'yengec_connector.api_key'


class YengecConnector(http.Controller):

    @http.route(['/yengec/setup', '/yengec/setup/<string:integration>'],
                type='http', auth='user', methods=['GET'])
    def redirect_to_setup(self, integration=''):
        sys_params = request.env['ir.config_parameter'].sudo()
        base_url = sys_params.get_param('web.base.url', '')
        db_uuid = sys_params.get_param('database.uuid', '')

        stored_key = sys_params.get_param(YENGEC_API_KEY_PARAM, False)
        key_exists = stored_key and request.env['res.users.apikeys'].sudo().search([
            ('name', '=', 'Yengeç Connector'),
        ], limit=1)

        if key_exists:
            api_key = stored_key
        else:
            api_key = request.env['res.users.apikeys']._generate(
                scope='rpc', name='Yengeç Connector'
            )
            sys_params.set_param(YENGEC_API_KEY_PARAM, api_key)

        query = urllib.parse.urlencode({
            'integration': integration,
            'odoo_url': base_url,
            'db_uuid': db_uuid,
            'api_key': api_key,
            'return_url': base_url + '/web',
        })
        return request.redirect(f'{YENGEC_SETUP_URL}?{query}', local=False)
