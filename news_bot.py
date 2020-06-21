import redis
import requests
from bs4 import BeautifulSoup

# 1. Get Source - ycombinator news

class Scraper:
    def __init__(self, keywords):
        self.markup = requests.get('https://news.ycombinator.com/').text
        self.keywords = keywords

# 2. Parse the HTML with beautifulsoup
    def parse(self):
        soup = BeautifulSoup(self.markup.'html.parser')
        links = soup.findAll("a", {"class": "storylink"})

    # loop through links add links with keyword to saved_links list
        self.saved_links = []
        for link in links:
            for keyword in self.keywords:
                if keyword in link.text:
                    self.saved.links.append(link)

    # create redis connection and store
    def store(self):
        r = redis.Redis(host='localhost', port=6379, db=0)
        r.set('foo', 'bar')
    
        
        
        
Scraper(['Engineer'])
