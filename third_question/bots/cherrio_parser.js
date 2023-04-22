module.exports = class CheerioParser {

    constructor() {}
  
    static match_selector(selector, soup) {
      return soup(selector).first();
    }
  
    static match_reduce(matches, soup) {
      return Object.keys(matches).reduce((result, key) => {
        const value = matches[key](CheerioParser.match_selector(key, soup));
        return { ...result, ...value };
      }, {});
    }
  }