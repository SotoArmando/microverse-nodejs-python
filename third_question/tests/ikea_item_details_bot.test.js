
let IkeaItemDetailsBot = require('../bots/ikea_item_details_bot');

test('adds 1 + 2 to equal 3', async () => {
    let bot = new IkeaItemDetailsBot();
    result = await bot.performUrl("https://www.ikea.com.do/en/pd/svardborg-rug-flatwoven-off-white-multicolor-art-90507924");
    console.log(result)
});