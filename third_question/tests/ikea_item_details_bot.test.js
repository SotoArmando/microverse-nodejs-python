
let IkeaItemDetailsBot = require('../bots/ikea_item_details_bot');

test('IkeaItemDetailsBot should succesfully read and parse html data', async () => {
    let bot = new IkeaItemDetailsBot();
    result = await bot.performUrl("https://www.ikea.com.do/en/pd/svardborg-rug-flatwoven-off-white-multicolor-art-90507924");
    console.log(result)
    
    expect(result["name"]).toEqual('\nSVÄRDBORG\n');
    expect(result["src"]).toEqual('https://d2ko4igzsg7f0j.cloudfront.net/webroot/img/logos/IKEA_logo.svg?v=477');
    expect(result["price"]).toEqual("\nRD$575\n");
    expect(result["prev_price"]).toEqual("\nRD$16,495 \n");
  
});