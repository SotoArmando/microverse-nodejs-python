const cheerio = require('cheerio');
const request = require('request');
const schedule = require('node-schedule');

export default class Bot {
    constructor(htmlParser) {
        this.parser = htmlParser;
    }

    async openUrl(url) {
        const htmlContent = await new Promise((resolve, reject) => {
            request(url, (error, response, html) => {
                if (error) reject(error);
                resolve(html);
            });
        });
        const $ = cheerio.load(htmlContent);
        return $;
    }

    async performRequest(request) {
        const response = await new Promise((resolve, reject) => {
            request(request.method, request.url, request.args, (error, response) => {
                if (error) reject(error);
                resolve(response);
            });
        });
        return this.perform(response);
    }

    async performUrl(url) {
        const $ = await this.openUrl(url);
        return this.perform($);
    }

    perform(html) {
        return this.parser(html);
    }

    monitor(site) {
        const job = async () => {
            const $ = await this.openUrl(site);
            return this.perform($);
        };
        return schedule.scheduleJob('0 */4 * * *', job);
    }

    aggregate(aggregateHTMLParser, site) {
        const job = async () => {
            const $ = await this.openUrl(site);
            return aggregateHTMLParser($);
        };
        return job();
    }

    async research(sites) {
        const result = await Promise.all(sites.map((url) => this.performUrl(url)));
        return result;
    }

    async automate(requests) {
        const result = await Promise.all(requests.map((request) => this.performRequest(request)));
        return result;
    }
}