{
    'name': 'Amazon Seller Global Connector',
    'version': '19.0.1.0.0',
    'category': 'eCommerce',
    'summary': 'Sync Odoo with Amazon Seller Global marketplace',
    'description': (
        'Connect your Odoo to Amazon Seller Global via Yengeç – guided setup. '
        'Odoo\'yu Yengeç aracılığıyla Amazon Seller Global ile bağlayın – adım adım kurulum.'
    ),
    'author': 'Yengeç',
    'website': 'https://yengec.co',
    'support': 'iletisim@yengec.co',
    'license': 'LGPL-3',
    'depends': ['yengec_connector'],
    'data': ['views/amazon_global_menu.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
