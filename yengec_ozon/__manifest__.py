{
    'name': 'Ozon Connector',
    'version': '20.0.1.0.0',
    'category': 'eCommerce',
    'summary': 'Sync Odoo with Ozon marketplace',
    'description': (
        'Connect your Odoo to Ozon via Yengeç – guided setup. '
        'Odoo\'yu Yengeç aracılığıyla Ozon ile bağlayın – adım adım kurulum.'
    ),
    'author': 'Yengeç',
    'website': 'https://yengec.co',
    'support': 'iletisim@yengec.co',
    'license': 'LGPL-3',
    'depends': ['yengec_connector'],
    'data': ['views/ozon_menu.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
