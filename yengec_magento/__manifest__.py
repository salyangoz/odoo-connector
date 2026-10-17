{
    'name': 'Magento Connector',
    'version': '20.0.1.0.0',
    'category': 'eCommerce',
    'summary': 'Sync Odoo with Magento store',
    'description': (
        'Connect your Odoo to Magento via Yengeç – guided setup. '
        'Odoo\'yu Yengeç aracılığıyla Magento ile bağlayın – adım adım kurulum.'
    ),
    'author': 'Yengeç',
    'website': 'https://yengec.co',
    'support': 'iletisim@yengec.co',
    'license': 'LGPL-3',
    'depends': ['yengec_connector'],
    'data': ['views/magento_menu.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
