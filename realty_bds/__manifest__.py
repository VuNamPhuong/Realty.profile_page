{
    'name': 'Realty',
    'version': '1.0',
    'depends': ['base'],
    'category': 'Uncategorized',
    'summary': 'Sườn phân quyền của Realty',
    "description": """
        - Allows admins to manage Hien Trang.
        - Allows admins to manage Loai Hinh.
        - Allows admins to manage Tag.
        - Allows admins to manage Reserve Words.
        - Allows admins to manage charateristic.
        - Allows admins to manage puprchase-purpose.
    """,
    'data': [
        #Views

        #Templates
        'views/my_profile_template.xml'
    ],

    "assets": {
        'web.assets_frontend': [
            #my_profile
            #js
            'realty_bds/static/src/my_profile/js/notify.js',

            #css
            'realty_bds/static/src/my_profile/css/style.css',
        ],
},

    "installable": True,
    "application": True,
    'auto_install': False,
    'license': 'LGPL-3',
}