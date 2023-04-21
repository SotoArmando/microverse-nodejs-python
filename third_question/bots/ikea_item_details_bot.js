
import Bot from './bot';
import { match_reduce } from './cherrio_parser';


class IkeaItemDetailsBot extends Bot {
    constructor() {
        super();
        this.html_parser = this.html_parser.bind(this);
    }

    html_parser(soup) {
        const matches = {
            "h6.display-7.mr-2.mb-0": (element) => ({ "name": element.text() }),
            "div.itemFacts.mb-2": (element) => ({ "description": element.text() }),
            "img.img-fluid[src]": (element) => ({ "src": element.attr('src') }),
            "p.itemPrice.itemLowerPrice.display-6": (element) => ({ "price": element.text() }),
            "p.itemOldPrice": (element) => ({ "prev_price": element.text() }),
        };

        return match_reduce(matches, soup);
    }
}

Object.assign(IkeaItemDetailsBot.prototype, BeautifulSoupParser);

module.exports = IkeaItemDetailsBot;