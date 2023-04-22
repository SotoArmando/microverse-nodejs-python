from . bot import Bot
from . beautiful_soup_parser import BeautifulSoupParser


class IkeaItemDetailsBot(Bot, BeautifulSoupParser):
    """Performs Ikea details bot"""

    def __init__(self):
        super().__init__(self.html_parser)


    def html_parser(self, soup):
        """Parses Ikea details data"""

        matches = {
            "h6.display-7.mr-2.mb-0":  lambda element: { "name": element.text },
            "div.itemFacts.mb-2": lambda element: { "description": element.text },
            "img.img-fluid[src]": lambda element: { "src": element['src'] },
            "p.itemPrice.itemLowerPrice.display-6": lambda element: { "price": element.text },
            "p.itemOldPrice": lambda element: { "prev_price": element.text },
        }
        
        return self.match_reduce(matches, soup)
