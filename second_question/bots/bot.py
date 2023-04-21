import requests
import asyncio
import schedule
from requests_html import HTMLSession


class Bot():
    """Performs tasks to extract, parse, research data"""

    def __init__(self, html_parser):
        self.parser = html_parser;


    def open_url(self, url):
        """Opens a url page and returns its html contents"""
        session = HTMLSession()
        session.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
        response = session.get(url, headers=session.headers)

        script = """
        () => {
            return {
                width: document.documentElement.clientWidth,
                height: document.documentElement.clientHeight,
                deviceScaleFactor: window.devicePixelRatio,
            }
        }
        """

        # response.html.render(script=script, reload=False)
        return response.html;

    def perform_request(self, request):
        """Performs bot parser task, but using a request"""
        response = request(request.method, request.url, request.args);
        return self.perform(response)
    
    def perform_url(self, url): 
        """Performs bot parser task, but using a url."""
        html = self.open_url(url)
        return self.perform(html)
    
    def perform(self, html):
        """Performs bot parser task."""
        return self.parser(html)

    def monitor(self, site):
        """Monitors url page by performing bot predefined task every 4 hours."""
        def job():
            html = self.open_url(site)
            return self.perform(html)

        return schedule.every(4).hours.do(job)

    def aggregate(self, aggregateHTMLParser, site):
        """Parses url page into aggregate data."""
        html = self.open_url(site)
        return aggregateHTMLParser(html)

    def research(self, sites):
        """Fetch requests and returns them unconditionally."""
        async def job():
            result = await asyncio.gather(*[self.perform_url(url) for url in sites])
            return result

        loop = asyncio.get_event_loop()
        loopresult = loop.run_until_complete(job())
        loop.close()
        return loopresult;

    def automate(self, requests):
        """Fetch requests and sorting them funcionally over methods and response types."""
        async def job():
            result = await asyncio.gather(*[self.perform_request(request) for request in requests])
            return result

        loop = asyncio.get_event_loop()
        loopresult = loop.run_until_complete(job())
        loop.close()
        return loopresult;


