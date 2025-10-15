{
    "name":"Hotel Management System",
    "author":"Agaa, IdeaCode Academy",
    "depends":["mail","hr","contacts"],
    "data":[
        "data/ir_sequence.xml",
        "security/ir.model.access.csv",
        "views/hms_booking.xml",
        "views/hms_room.xml",
        # "views/hms_hotel.xml",
        "views/hms_payment_method.xml",
        "wizard/hms_payment_wizard.xml",
        "views/res_partner.xml",
        "views/res_config_settings.xml",

        "views/menus.xml",
    ],
    "images":[
        "static/description/icon.png",
    ],
    "demo":[
        "data/hms_hotel.xml",
        "data/hms_room.xml",
    ],
    "license":"LGPL-3"
}