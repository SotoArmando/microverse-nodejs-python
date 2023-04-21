from . bot import Bot
from . html_parser import HtmlParser


class AmazonItemDetailsBot(Bot, HtmlParser):
    """Performs amazon details bot"""

    def __init__(self):
        super().__init__(self.html_parser)


    def html_parser(self, html):
        """Parses amazon details data"""

        matches = {
            "name": self.match_tag_and_class("h6", "display-7 mr-2 mb-0"),
            "description": self.match_tag_and_class("div", "itemFacts mb-2"),
            "src": self.match_attribute("img", "img-fluid", "src"),
            "feature-bullets": [self.match_tag_and_class("ul", "a-unordered-list a-vertical a-spacing-mini"), self.match_tag_and_class("li", "a-list-item")]
        }

        return self.reduce_matches(matches, html)
