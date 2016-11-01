import requests, re
from bs4 import BeautifulSoup
from python_utils import converters

def get_parsed_page(url):
    return BeautifulSoup(requests.get(url).text, "lxml")
urls ="http://www.hltv.org/match/2302717-optic-tsm-mlg-regional-minor-championship-americas"

matches = get_parsed_page(urls)

def get_event():
    event = matches.find_all("div", {"style": "text-align:center;font-size: 18px;"})[1]
    event1 = event.find("a")["href"]
    return event1[20:]

print(get_event())
