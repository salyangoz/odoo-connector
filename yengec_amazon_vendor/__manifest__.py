{
    'name': 'Amazon Vendor Central Connector',
    'version': '17.0.1.0.0',
    'category': 'eCommerce',
    'summary': 'Sync Odoo with Amazon Vendor Central marketplace',
    'description': (
        'Connect your Odoo to Amazon Vendor Central via Yengeç – guided setup. '
        'Odoo\'yu Yengeç aracılığıyla Amazon Vendor Central ile bağlayın – adım adım kurulum.'
    ),
    'author': 'Yengeç',
    'website': 'https://yengec.co',
    'support': 'iletisim@yengec.co',
    'license': 'LGPL-3',
    'depends': ['yengec_connector'],
    'data': ['views/amazon_vendor_menu.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
