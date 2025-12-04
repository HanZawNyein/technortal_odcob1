import {Component, onWillStart,useState} from "@odoo/owl";
import {useService} from "@web/core/utils/hooks";

export class Partner extends Component {
    static template = "ica_hms.Partner";
    static props = {};

    setup() {
        this.state = useState({
            partners: [],
        });
        this.orm = useService('orm');
        onWillStart(async () => {
            await this.getPartners();
        });
    }

    async getPartners() {
        let partners = await this.orm.webSearchRead('res.partner', [], {
                specification: {
                    id: {},
                    display_name: {},
                },
            });
        console.log(partners['records'])
        this.state.partners=partners['records']
        console.log()
    }

}