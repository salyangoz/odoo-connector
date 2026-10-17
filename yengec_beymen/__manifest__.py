{
    'name': 'Beymen Connector',
    'version': '17.0.1.0.0',
    'category': 'eCommerce',
    'summary': 'Sync Odoo with Beymen marketplace',
    'description': (
        'Connect your Odoo to Beymen via Yengeç – guided setup. '
        'Odoo\'yu Yengeç aracılığıyla Beymen ile bağlayın – adım adım kurulum.'
    ),
    'author': 'Yengeç',
    'website': 'https://yengec.co',
    'support': 'iletisim@yengec.co',
    'license': 'LGPL-3',
    'depends': ['yengec_connector'],
    'data': ['views/beymen_menu.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
