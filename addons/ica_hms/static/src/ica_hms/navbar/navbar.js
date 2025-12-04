import { Component } from "@odoo/owl";

export class Navbar extends Component {
    static template = "ica_hms.Navbar";
    static props = {};

    setup(){
        console.log(this.props)
    }

    switchScreen(screenName){
        this.props.switchScreen(screenName)
    }
}