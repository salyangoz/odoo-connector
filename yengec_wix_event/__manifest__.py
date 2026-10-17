{
    'name': 'Wix Event Connector',
    'version': '18.0.1.0.0',
    'category': 'eCommerce',
    'summary': 'Sync Odoo with Wix Event store',
    'description': (
        'Connect your Odoo to Wix Event via Yengeç – guided setup. '
        'Odoo\'yu Yengeç aracılığıyla Wix Event ile bağlayın – adım adım kurulum.'
    ),
    'author': 'Yengeç',
    'website': 'https://yengec.co',
    'support': 'iletisim@yengec.co',
    'license': 'LGPL-3',
    'depends': ['yengec_connector'],
    'data': ['views/wix_event_menu.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
