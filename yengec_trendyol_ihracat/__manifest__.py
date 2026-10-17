{
    'name': 'Trendyol İhracat Connector',
    'version': '18.0.1.0.0',
    'category': 'eCommerce',
    'summary': 'Sync Odoo with Trendyol İhracat marketplace',
    'description': (
        'Connect your Odoo to Trendyol İhracat via Yengeç – guided setup. '
        'Odoo\'yu Yengeç aracılığıyla Trendyol İhracat ile bağlayın – adım adım kurulum.'
    ),
    'author': 'Yengeç',
    'website': 'https://yengec.co',
    'support': 'iletisim@yengec.co',
    'license': 'LGPL-3',
    'depends': ['yengec_connector'],
    'data': ['views/trendyol_ihracat_menu.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
