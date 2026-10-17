{
    'name': 'Novadan Connector',
    'version': '19.0.1.0.0',
    'category': 'eCommerce',
    'summary': 'Sync Odoo with Novadan marketplace',
    'description': (
        'Connect your Odoo to Novadan via Yengeç – guided setup. '
        'Odoo\'yu Yengeç aracılığıyla Novadan ile bağlayın – adım adım kurulum.'
    ),
    'author': 'Yengeç',
    'website': 'https://yengec.co',
    'support': 'iletisim@yengec.co',
    'license': 'LGPL-3',
    'depends': ['yengec_connector'],
    'data': ['views/novadan_menu.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
