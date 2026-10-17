{
    'name': 'Wix Payment Connector',
    'version': '20.0.1.0.0',
    'category': 'eCommerce',
    'summary': 'Sync Odoo with Wix Payment store',
    'description': (
        'Connect your Odoo to Wix Payment via Yengeç – guided setup. '
        'Odoo\'yu Yengeç aracılığıyla Wix Payment ile bağlayın – adım adım kurulum.'
    ),
    'author': 'Yengeç',
    'website': 'https://yengec.co',
    'support': 'iletisim@yengec.co',
    'license': 'LGPL-3',
    'depends': ['yengec_connector'],
    'data': ['views/wix_payment_menu.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
