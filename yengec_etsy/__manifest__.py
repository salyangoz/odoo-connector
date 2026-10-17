{
    'name': 'Etsy Connector',
    'version': '17.0.1.0.0',
    'category': 'eCommerce',
    'summary': 'Sync Odoo with Etsy marketplace',
    'description': (
        'Connect your Odoo to Etsy via Yengeç – guided setup. '
        'Odoo\'yu Yengeç aracılığıyla Etsy ile bağlayın – adım adım kurulum.'
    ),
    'author': 'Yengeç',
    'website': 'https://yengec.co',
    'support': 'iletisim@yengec.co',
    'license': 'LGPL-3',
    'depends': ['yengec_connector'],
    'data': ['views/etsy_menu.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
