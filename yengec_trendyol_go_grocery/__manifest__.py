{
    'name': 'Trendyol Go Hızlı Market Connector',
    'version': '19.0.1.0.0',
    'category': 'eCommerce',
    'summary': 'Sync Odoo with Trendyol Go Hızlı Market marketplace',
    'description': (
        'Connect your Odoo to Trendyol Go Hızlı Market via Yengeç – guided setup. '
        'Odoo\'yu Yengeç aracılığıyla Trendyol Go Hızlı Market ile bağlayın – adım adım kurulum.'
    ),
    'author': 'Yengeç',
    'website': 'https://yengec.co',
    'support': 'iletisim@yengec.co',
    'license': 'LGPL-3',
    'depends': ['yengec_connector'],
    'data': ['views/trendyol_go_grocery_menu.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
