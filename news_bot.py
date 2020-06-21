import requests
import MarkupPy

# 1. Get Source - ycombinator news

class Scraper:
    def _init_(self):
        self.markup = requests.get('https://news.ycombinator.com/').text
        
