{
    'name': 'Koçtaş Connector',
    'version': '18.0.1.0.0',
    'category': 'eCommerce',
    'summary': 'Sync Odoo with Koçtaş marketplace',
    'description': (
        'Connect your Odoo to Koçtaş via Yengeç – guided setup. '
        'Odoo\'yu Yengeç aracılığıyla Koçtaş ile bağlayın – adım adım kurulum.'
    ),
    'author': 'Yengeç',
    'website': 'https://yengec.co',
    'support': 'iletisim@yengec.co',
    'license': 'LGPL-3',
    'depends': ['yengec_connector'],
    'data': ['views/koctas_menu.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
