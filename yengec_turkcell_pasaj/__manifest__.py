{
    'name': 'Turkcell Pasaj Connector',
    'version': '20.0.1.0.0',
    'category': 'eCommerce',
    'summary': 'Sync Odoo with Turkcell Pasaj marketplace',
    'description': (
        'Connect your Odoo to Turkcell Pasaj via Yengeç – guided setup. '
        'Odoo\'yu Yengeç aracılığıyla Turkcell Pasaj ile bağlayın – adım adım kurulum.'
    ),
    'author': 'Yengeç',
    'website': 'https://yengec.co',
    'support': 'iletisim@yengec.co',
    'license': 'LGPL-3',
    'depends': ['yengec_connector'],
    'data': ['views/turkcell_pasaj_menu.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
