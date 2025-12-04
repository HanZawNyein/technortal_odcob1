{
    "name": "Hotel Management System",
    "author": "Agaa, IdeaCode Academy",
    "depends": ["mail", "hr", "contacts", "web","base"],
    "data": [
        "data/ir_sequence.xml",

        "security/security.xml",
        "security/ir.model.access.csv",
        "views/hms_room.xml",
        # "views/hms_hotel.xml",
        "views/hms_payment_method.xml",
        "wizard/hms_payment_wizard.xml",
        "views/res_partner.xml",
        "views/res_config_settings.xml",
        "views/hms_booking.xml",
        "views/hms_hotel_client_action.xml",

        "views/menus.xml",
        "views/iac_hms_template.xml"
        #
        # "views/hms_rooms_template.xml",

        # "report/hms_room.xml",
        # "report/hms_room_report_template.xml",
        # "report/hms_room_report_action.xml",
    ],
    "images": [
        "static/description/icon.png",
    ],
    "demo": [
        "data/hms_hotel.xml",
        "data/hms_room.xml",
    ],
    # "external_dependencies":{
    #     "python":["numpy"],
    # },
    "assets": {
        "web.assets_backend": [
            "ica_hms/static/src/hms_room/**/*",
        ],
        'ica_hms.assets_standalone_app': [
            ('include', 'web._assets_helpers'),
            ('include', 'web._assets_backend_helpers'),
            'web/static/src/scss/pre_variables.scss',
            'web/static/lib/bootstrap/scss/_variables.scss',
            'web/static/lib/bootstrap/scss/_variables-dark.scss',
            'web/static/lib/bootstrap/scss/_maps.scss',
            ('include', 'web._assets_bootstrap_backend'),

            ('include', 'web._assets_core'),
            'ica_hms/static/src/ica_hms/**/*',
        ],

    },
    "license": "LGPL-3"
}
