from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"


thisdict = {
  bots: {
    
  }
}

def scrape(url):
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    print(html)
