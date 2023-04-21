import threading
import schedule
from urllib.request import urlopen



class Bot():
    def __init__(self, htmlParser):
        self.parser = htmlParser;

    def perform(self, html):
        return self.parser(html);

    def monitor(self, site):
        def job():
            html = openUrl(site);
            

        return schedule.every(10).seconds.do(job);


    def aggregate(self):
        print("aggregating")
    
    def research(self, sites):
        print("researching")

    def automate(self, sites):
        print("automating")

    def openUrl(url):
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        return html;
