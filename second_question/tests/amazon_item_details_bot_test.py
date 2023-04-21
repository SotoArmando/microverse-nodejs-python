import unittest
from bots.amazon_item_details_bot import AmazonItemDetailsBot



class AmazonItemDetailsBotTest(unittest.TestCase):

    def test_it_parses_correctly_0(self):
        mybot = AmazonItemDetailsBot()
        print(mybot.perform_url("https://www.ikea.com.do/es/pd/vinarn-toalla-de-bano-rosado-claro-art-40521220"))


if __name__ == '__main__s':
    unittest.main()
