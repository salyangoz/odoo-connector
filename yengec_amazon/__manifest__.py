{
    'name': 'Amazon Connector',
    'version': '17.0.1.0.0',
    'category': 'eCommerce',
    'summary': 'Sync Odoo with Amazon marketplace',
    'description': (
        'Connect your Odoo to Amazon via Yengeç – guided setup wizard. '
        'Odoo\'yu Yengeç aracılığıyla Amazon\'a bağlayın – adım adım kurulum.'
    ),
    'author': 'Yengeç',
    'website': 'https://yengec.co',
    'support': 'iletisim@yengec.co',
    'license': 'LGPL-3',
    'depends': ['yengec_connector'],
    'data': ['views/amazon_menu.xml'],
    'installable': True,
    'application': True,
    'images': ['static/description/banner.png'],
    'auto_install': False,
}
