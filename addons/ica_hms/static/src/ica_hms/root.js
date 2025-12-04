import {Component, useState} from "@odoo/owl";
import {Navbar} from "./navbar/navbar";
import {Home} from "./home/home";
import {Partner} from "./partner/partner";

export class Root extends Component {
    static template = "ica_hms.Root";
    static props = {};
    static components = {Navbar, Home, Partner};

    setup() {
        this.state = useState({
            currentScreen: 'HomeScreen',
        })
    }

    get getScreen() {
        return this.state.currentScreen === 'homeScreen' ? Home : Partner;
    }

    switchScreen(screenName) {
        this.state.currentScreen = screenName;
    }
}