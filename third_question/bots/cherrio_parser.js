export default  class CheerioParser {

    constructor() {}
  
    static match_selector(selector, soup) {
      return soup.querySelector(selector);
    }
  
    static match_reduce(matches, soup) {
      return Object.keys(matches).reduce((result, key) => {
        const value = matches[key](this.match_selector(key, soup));
        return { ...result, ...value };
      }, {});
    }
  }