{
    'name': 'Boyner Connector',
    'version': '18.0.1.0.0',
    'category': 'eCommerce',
    'summary': 'Sync Odoo with Boyner marketplace',
    'description': (
        'Connect your Odoo to Boyner via Yengeç – guided setup. '
        'Odoo\'yu Yengeç aracılığıyla Boyner ile bağlayın – adım adım kurulum.'
    ),
    'author': 'Yengeç',
    'website': 'https://yengec.co',
    'support': 'iletisim@yengec.co',
    'license': 'LGPL-3',
    'depends': ['yengec_connector'],
    'data': ['views/boyner_menu.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
