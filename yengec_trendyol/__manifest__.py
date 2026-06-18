{
    'name': 'Trendyol Connector',
    'version': '17.0.1.0.0',
    'category': 'eCommerce',
    'summary': 'Sync Odoo with Trendyol marketplace',
    'description': (
        'Connect your Odoo to Trendyol via Yengeç – guided setup wizard. '
        'Odoo\'yu Yengeç aracılığıyla Trendyol\'a bağlayın – adım adım kurulum.'
    ),
    'author': 'Yengeç',
    'website': 'https://yengec.co',
    'support': 'iletisim@yengec.co',
    'license': 'LGPL-3',
    'depends': ['yengec_connector'],
    'data': ['views/trendyol_menu.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
