import requests
from bs4 import BeautifulSoup
from python_utils import converters
import re

def get_parsed_page(url):
    return BeautifulSoup(requests.get(url).text, "lxml")

urls = "http://www.hltv.org/?pageid=188&matchid=25001"
matches = get_parsed_page(urls)

"""
def get_match_id():
    ma = urls[26:33]
    return ma
"""

def get_player_id():
    ma = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:20%;float:left;"})[0] #0~9
    ta = ma.find("a")["href"]
    l = len(ta)
    elta = ta[8:]
    transInt = re.match("\d*",elta)
    da = transInt.group()
    if l >= 23:
        return ta[22:]
    elif l < 23:
        return da

def get_kill():
    kill = matches.find("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:10%;float:left;text-align:center"}).text.split()[0]
    return kill

def get_assist():
    assist = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:5%;float:left;text-align:center"})[0].text
    return assist

def get_death():
    death = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:5%;float:left;text-align:center"})[1].text
    return death

def get_kd_ratio():
    ratio = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:10%;float:left;text-align:center"})[1].text
    return ratio

def get_rating():
    rating = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:10%;float:left;text-align:center"})[2].text
    return rating

#print(get_match_id()) un-use
print(get_player_id())
print(get_kill())
print(get_assist())
print(get_death())
print(get_kd_ratio())
print(get_rating())
