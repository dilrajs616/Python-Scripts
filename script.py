from bs4 import BeautifulSoup
import requests
import time

link = "https://kbiz.kasikornbank.com/menu/maker-management/maker-history"

class WebScraper():

    def __init__(self) -> None:
        self.call_scraper()

    def call_scraper(self):
        while True:
            self.scraper()
            time.sleep(5)

    def scraper(self):
        pass