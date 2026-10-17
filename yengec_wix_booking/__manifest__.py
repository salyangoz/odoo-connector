{
    'name': 'Wix Booking Connector',
    'version': '19.0.1.0.0',
    'category': 'eCommerce',
    'summary': 'Sync Odoo with Wix Booking store',
    'description': (
        'Connect your Odoo to Wix Booking via Yengeç – guided setup. '
        'Odoo\'yu Yengeç aracılığıyla Wix Booking ile bağlayın – adım adım kurulum.'
    ),
    'author': 'Yengeç',
    'website': 'https://yengec.co',
    'support': 'iletisim@yengec.co',
    'license': 'LGPL-3',
    'depends': ['yengec_connector'],
    'data': ['views/wix_booking_menu.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
