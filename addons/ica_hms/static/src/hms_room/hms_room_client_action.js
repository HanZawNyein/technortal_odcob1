import { registry } from "@web/core/registry";
import { Layout } from "@web/search/layout";
import { Component } from  "@odoo/owl";

class MyClientAction extends Component {
    static template = "ica_hms.hms_room";
    static components = {Layout};

    printWeb(){
        console.log("hello")
    }
}

// remember the tag name we put in the first step
registry.category("actions").add("ica_hms.hms_room", MyClientAction);