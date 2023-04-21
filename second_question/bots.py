import threading
import schedule
import functools
import requests
import asyncio
from urllib.request import urlopen



class Bot():
    """Performs tasks to extract, parse, research data"""

    def __init__(self, htmlParser):
        self.parser = htmlParser;

    def open_url(self, url):
        """Opens a url page and returns its html contents"""
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        return html;

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


