import functools
import re

class BeautifulSoupParser():
    
    def __init__(self) -> None:
        pass

    def match_selector(self, selector, soup):
        return soup.select_one(selector)

    def match_reduce(self, matches, soup):
        return functools.reduce(lambda x, key:  {**x, **matches[key](self.match_selector(key, soup)) } , matches, {}) 

