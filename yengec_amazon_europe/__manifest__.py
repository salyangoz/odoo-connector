{
    'name': 'Amazon Seller Europe Connector',
    'version': '18.0.1.0.0',
    'category': 'eCommerce',
    'summary': 'Sync Odoo with Amazon Seller Europe marketplace',
    'description': (
        'Connect your Odoo to Amazon Seller Europe via Yengeç – guided setup. '
        'Odoo\'yu Yengeç aracılığıyla Amazon Seller Europe ile bağlayın – adım adım kurulum.'
    ),
    'author': 'Yengeç',
    'website': 'https://yengec.co',
    'support': 'iletisim@yengec.co',
    'license': 'LGPL-3',
    'depends': ['yengec_connector'],
    'data': ['views/amazon_europe_menu.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
