{
    'name': 'T-Soft Connector',
    'version': '20.0.1.0.0',
    'category': 'eCommerce',
    'summary': 'Sync Odoo with T-Soft store',
    'description': (
        'Connect your Odoo to T-Soft via Yengeç – guided setup. '
        'Odoo\'yu Yengeç aracılığıyla T-Soft ile bağlayın – adım adım kurulum.'
    ),
    'author': 'Yengeç',
    'website': 'https://yengec.co',
    'support': 'iletisim@yengec.co',
    'license': 'LGPL-3',
    'depends': ['yengec_connector'],
    'data': ['views/t_soft_menu.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
