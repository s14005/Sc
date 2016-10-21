import requests,re
from bs4 import BeautifulSoup
from python_utils import converters

def get_parsed_page(url):
    return BeautifulSoup(requests.get(url).text, "lxml")

urls = "http://www.hltv.org/?pageid=188&matchid=28004"
matches = get_parsed_page(urls)

"""
def get_match_id():
    ma = urls[26:33]
    return ma
"""

def get_player_id(num):
    ma = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:20%;float:left;"})[num] #0~9
    ta = ma.find("a")["href"]
    l = len(ta)
    elta = ta[8:]
    transInt = re.match("\d*",elta)
    da = transInt.group()
    if l >= 23:
        return ta[22:]
    elif l < 23:
        return da

def get_kill(num):
    kill = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:10%;float:left;text-align:center"})[num]
    ki = kill.text.split()[0]
    return ki

def get_assist(num):
    assist = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:5%;float:left;text-align:center"})[num].text
    return assist

def get_death(num):
    death = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:5%;float:left;text-align:center"})[num+1].text
    return death

def get_kd_ratio(num):
    ratio = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:10%;float:left;text-align:center"})[num+1].text
    return ratio

def get_adr(num):
    adr = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:8%;float:left;;text-align:center"})
    if len(adr) == 10:
        return adr[num].text
    else:
        return None

def get_rating(num):
    rating = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:10%;float:left;text-align:center"})[num+2].text
    return rating
m = 1
while 11 > m:

    print(get_player_id(1*m-1)) #OK
    print(get_kill(3*m-3)) #OK
    print(get_assist(2*m-2)) #OK
    print(get_death(2*m-2)) #OK
    print(get_kd_ratio(3*m-3)) #OK
    print(get_adr(m-1))
    print(get_rating(3*m-3)) #OK
    m+=1
