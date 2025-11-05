{
    "name":"Hotel Management System",
    "author":"Agaa, IdeaCode Academy",
    "depends":["mail","hr","contacts","website"],
    "data":[
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

        "views/menus.xml",
        #
        # "views/hms_rooms_template.xml",


        # "report/hms_room.xml",
        "report/hms_room_report_template.xml",
        "report/hms_room_report_action.xml",
    ],
    "images":[
        "static/description/icon.png",
    ],
    "demo":[
        "data/hms_hotel.xml",
        "data/hms_room.xml",
    ],
    # "external_dependencies":{
    #     "python":["numpy"],
    # },
    "license":"LGPL-3"
}