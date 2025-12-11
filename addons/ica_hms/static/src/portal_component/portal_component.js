import {Component} from "@odoo/owl";
import {registry} from "@web/core/registry"
import { useRef, onPatched, onMounted, useState } from "@odoo/owl";

export class PortalComponent extends Component {
    static template = "ica_hms.PortalComponent";
    static props = {};

    setup(){
        this.state = useState({
            counter:0,
        });
    }

    addCounter(){
        this.state.counter++;
    }
}

registry.category("public_components").add("ica_hms.PortalComponent", PortalComponent);