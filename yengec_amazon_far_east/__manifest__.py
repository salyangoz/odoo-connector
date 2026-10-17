{
    'name': 'Amazon Seller Far East Connector',
    'version': '18.0.1.0.0',
    'category': 'eCommerce',
    'summary': 'Sync Odoo with Amazon Seller Far East marketplace',
    'description': (
        'Connect your Odoo to Amazon Seller Far East via Yengeç – guided setup. '
        'Odoo\'yu Yengeç aracılığıyla Amazon Seller Far East ile bağlayın – adım adım kurulum.'
    ),
    'author': 'Yengeç',
    'website': 'https://yengec.co',
    'support': 'iletisim@yengec.co',
    'license': 'LGPL-3',
    'depends': ['yengec_connector'],
    'data': ['views/amazon_far_east_menu.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
