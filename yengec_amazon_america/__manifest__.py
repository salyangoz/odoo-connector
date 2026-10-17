{
    'name': 'Amazon Seller America Connector',
    'version': '20.0.1.0.0',
    'category': 'eCommerce',
    'summary': 'Sync Odoo with Amazon Seller America marketplace',
    'description': (
        'Connect your Odoo to Amazon Seller America via Yengeç – guided setup. '
        'Odoo\'yu Yengeç aracılığıyla Amazon Seller America ile bağlayın – adım adım kurulum.'
    ),
    'author': 'Yengeç',
    'website': 'https://yengec.co',
    'support': 'iletisim@yengec.co',
    'license': 'LGPL-3',
    'depends': ['yengec_connector'],
    'data': ['views/amazon_america_menu.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
