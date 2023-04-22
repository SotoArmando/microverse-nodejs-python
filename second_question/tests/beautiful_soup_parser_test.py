import unittest
from pprint import pprint
from bots.ikea_item_details_bot import IkeaItemDetailsBot

class IkeaItemDetailsBotTest(unittest.TestCase):

    def test_ikea_item_details_bot_parses_url(self):
        bot = IkeaItemDetailsBot();
        result = bot.perform_url("https://www.ikea.com.do/es/pd/vinarn-toalla-de-bano-rosado-claro-art-40521220")

        self.assertTrue(result["description"] == 'Toalla de baño,\n\nrosado claro, 39x59 "\n\n')
        self.assertTrue(result["name"] == '\nVINARN\n')
        self.assertTrue(result["prev_price"] == '\nPrecio anterior: \nRD$1,195 \n')
        self.assertTrue(result["price"] == '\nRD$875\n')
        self.assertTrue(result["src"] == 'https://d2ko4igzsg7f0j.cloudfront.net/webroot/img/logos/IKEA_logo.svg?v=477')
        

if __name__ == '__main__s':
    unittest.main()
