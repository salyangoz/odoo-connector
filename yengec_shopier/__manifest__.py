{
    'name': 'Shopier Connector',
    'version': '17.0.1.0.0',
    'category': 'eCommerce',
    'summary': 'Sync Odoo with Shopier store',
    'description': (
        'Connect your Odoo to Shopier via Yengeç – guided setup. '
        'Odoo\'yu Yengeç aracılığıyla Shopier ile bağlayın – adım adım kurulum.'
    ),
    'author': 'Yengeç',
    'website': 'https://yengec.co',
    'support': 'iletisim@yengec.co',
    'license': 'LGPL-3',
    'depends': ['yengec_connector'],
    'data': ['views/shopier_menu.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
