{
    'name': 'idefix Connector',
    'version': '20.0.1.0.0',
    'category': 'eCommerce',
    'summary': 'Sync Odoo with idefix marketplace',
    'description': (
        'Connect your Odoo to idefix via Yengeç – guided setup. '
        'Odoo\'yu Yengeç aracılığıyla idefix ile bağlayın – adım adım kurulum.'
    ),
    'author': 'Yengeç',
    'website': 'https://yengec.co',
    'support': 'iletisim@yengec.co',
    'license': 'LGPL-3',
    'depends': ['yengec_connector'],
    'data': ['views/idefix_menu.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
