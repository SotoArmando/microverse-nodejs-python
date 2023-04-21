from . bot import Bot
from . html_parser import HtmlParser

class AmazonItemDetailsBot(Bot, HtmlParser):
    """Performs amazon details bot"""

    def __init__(self):
        super.__init__(self.html_parser);
    
    def html_parser(self, html):
        """Parses amazon details data"""

        matches = {
            "name": self.match_tag_and_class("span","a-size-large product-title-word-break"),
            "price": self.match_tag_and_class("span","a-offscreen"),
            "src": self.match_attribute("img","a-dynamic-image", "src"),
        }

        return self.reduce_matches(matches, html);
    
