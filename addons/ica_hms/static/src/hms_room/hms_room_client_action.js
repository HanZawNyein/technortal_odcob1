import {registry} from "@web/core/registry";
import {Layout} from "@web/search/layout";
import {Component, useState, onWillStart} from "@odoo/owl";
import {useService} from "@web/core/utils/hooks";


class MyClientAction extends Component {
    static template = "ica_hms.hms_room";
    static components = {Layout};

    setup() {
        this.state = useState({
            value: 100,
            partners: []
        });
        this.orm = this.env.services.orm;
        this.effect = useService('effect');
        this.titleService = useService("title");
        this.titleService.setParts({ odoo: "Odoo 15", fruit: "Apple" });


        console.log(this.env.services.orm)
        onWillStart(async () => {
            await this.getPartners();
        })
    }

    showEffect() {
        this.effect.add({
            type: "rainbow_man", // can be omitted, default type is already "rainbow_man"
            message: "Boom! Team record for the past 30 days.",
        });
    }

    async getPartners() {
        this.state.partners = await this.orm.searchRead('res.partner', [], ['id', 'display_name', 'create_uid', 'create_date']);
        console.log(this.state.partners)
    }

    async deletePartners(partnerId) {
        await this.orm.unlink('res.partner', [partnerId]);
        console.log("partner is delete")
        console.log(partnerId)
        this.state.partners = this.state.partners.filter(existing_partner => existing_partner.id !== partnerId);
    }

    value_add() {
        this.state.value++;
        console.log(this.state.value);
    }

    printWeb() {
        console.log("hello")
    }
}

// remember the tag name we put in the first step
registry.category("actions").add("ica_hms.hms_room", MyClientAction);