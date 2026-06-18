{
    'name': 'Hepsiburada Connector',
    'version': '17.0.1.0.0',
    'category': 'eCommerce',
    'summary': 'Sync Odoo with Hepsiburada marketplace',
    'description': (
        'Connect your Odoo to Hepsiburada via Yengeç – guided setup wizard. '
        'Odoo\'yu Yengeç aracılığıyla Hepsiburada\'ya bağlayın – adım adım kurulum.'
    ),
    'author': 'Yengeç',
    'website': 'https://yengec.co',
    'support': 'iletisim@yengec.co',
    'license': 'LGPL-3',
    'depends': ['yengec_connector'],
    'data': [
        'views/hepsiburada_menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
