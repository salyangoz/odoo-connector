{
    'name': 'Çiçeksepeti Connector',
    'version': '17.0.1.0.0',
    'category': 'eCommerce',
    'summary': 'Sync Odoo with Çiçeksepeti marketplace',
    'description': (
        'Connect your Odoo to Çiçeksepeti via Yengeç – guided setup. '
        'Odoo\'yu Yengeç aracılığıyla Çiçeksepeti ile bağlayın – adım adım kurulum.'
    ),
    'author': 'Yengeç',
    'website': 'https://yengec.co',
    'support': 'iletisim@yengec.co',
    'license': 'LGPL-3',
    'depends': ['yengec_connector'],
    'data': ['views/ciceksepeti_menu.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
