{
    'name': 'Ideasoft Connector',
    'version': '19.0.1.2.0',
    'category': 'eCommerce',
    'summary': 'Sync Odoo with Ideasoft store',
    'description': (
        'Connect your Odoo to Ideasoft via Yengeç – guided setup wizard. '
        'Odoo\'yu Yengeç aracılığıyla Ideasoft\'a bağlayın – adım adım kurulum.'
    ),
    'author': 'Yengeç',
    'website': 'https://yengec.co',
    'support': 'iletisim@yengec.co',
    'license': 'LGPL-3',
    'depends': ['yengec_connector'],
    'data': ['views/ideasoft_menu.xml'],
    'installable': True,
    'application': True,
    'images': ['static/description/banner.png'],
    'auto_install': False,
}
