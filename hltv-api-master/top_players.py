import requests, re
from bs4 import BeautifulSoup
from python_utils import converters

def get_parsed_page(url):
    return BeautifulSoup(requests.get(url).text, "lxml")

urls = "http://www.hltv.org/?pageid=188&matchid=29000"


matches = get_parsed_page(urls)

def get_most_kills_user_id(num):
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:125px;float:left;text-align:left"})[num]
    ta = ka.find("a")["href"]
    l = len(ta)
    elta = ta[8:]
    transInt = re.match("\d*",elta)
    da = transInt.group()
    if l >= 23:
        return ta[22:]
    elif l < 23:
        return da

def get_most_kills_score(num):
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style":"font-weight:normal;width:30px;float:left;text-align:right"})[num].text
    return ka


def get_most_damage_user_id(num):
    sa = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:125px;float:left;text-align:left"})
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:125px;float:left;text-align:left"})[num]
    ta = ka.find("a")["href"]
    l = len(ta)
    elta = ta[8:]
    transInt = re.match("\d*",elta)
    da = transInt.group()
    if len(sa) <= 5:
        return None
    elif l >= 23:
        return ta[22:]
    elif l < 23:
        return da

def get_most_damage_score(num):
    sa = matches.findAll("div", {"class": "covSmallHeadline", "style":"font-weight:normal;width:30px;float:left;text-align:right"})
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style":"font-weight:normal;width:30px;float:left;text-align:right"})[num].text
    if len(sa) <= 5:
        return None
    else:
        return ka

def get_most_assists_user_id(num):
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:125px;float:left;text-align:left"})[num]
    ta = ka.find("a")["href"]
    l = len(ta)
    elta = ta[8:]
    transInt = re.match("\d*",elta)
    da = transInt.group()
    if l >= 23:
        return ta[22:]
    elif l < 23:
        return da

def get_most_assists_score(num):
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style":"font-weight:normal;width:30px;float:left;text-align:right"})[num].text
    return ka


def get_most_awp_kills_user_id(num):
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:125px;float:left;text-align:left"})[num]
    ta = ka.find("a")["href"]
    l = len(ta)
    elta = ta[8:]
    transInt = re.match("\d*",elta)
    da = transInt.group()
    if l >= 23:
        return ta[22:]
    elif l < 23:
        return da

def get_most_awp_kills_score(num):
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style":"font-weight:normal;width:30px;float:left;text-align:right"})[num].text
    return ka



def get_most_first_kills_user_id(num):
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:125px;float:left;text-align:left"})[num]
    ta = ka.find("a")["href"]
    l = len(ta)
    elta = ta[8:]
    transInt = re.match("\d*",elta)
    da = transInt.group()
    if l >= 23:
        return ta[22:]
    elif l < 23:
        return da

def get_most_first_kills_score(num):
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style":"font-weight:normal;width:30px;float:left;text-align:right"})[num].text
    return ka

def get_best_rating_user_id(num):
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:125px;float:left;text-align:left"})[num]
    ta = ka.find("a")["href"]
    l = len(ta)
    elta = ta[8:]
    transInt = re.match("\d*",elta)
    da = transInt.group()
    if l >= 23:
        return ta[22:]
    elif l < 23:
        return da

def get_best_rating_score(num):
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style":"font-weight:normal;width:30px;float:left;text-align:right"})[num].text
    return ka

def get_top_players_score():
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style":"font-weight:normal;width:30px;float:left;text-align:right"})
    l = len(ka)

    if l == 5:
        print(get_most_kills_user_id(0))
        print(get_most_kills_score(0))
        print(get_most_damage_user_id(1))
        print(get_most_damage_score(1))
        print(get_most_assists_user_id(1))
        print(get_most_assists_score(1))
        print(get_most_awp_kills_user_id(2))
        print(get_most_awp_kills_score(2))
        print(get_most_first_kills_user_id(3))
        print(get_most_first_kills_score(3))
        print(get_best_rating_user_id(4))
        print(get_best_rating_score(4))

    elif l == 6:
        #print(get_most_kills_user_id(0))
        #print(get_most_kills_score(0))
        #print(get_most_damage_user_id(1))
        print(get_most_damage_score(1))
        #print(get_most_assists_user_id(2))
        #print(get_most_assists_score(2))
        #print(get_most_awp_kills_user_id(3))
        #print(get_most_awp_kills_score(3))
        #print(get_most_first_kills_user_id(4))
        #print(get_most_first_kills_score(4))
        #print(get_best_rating_user_id(5))
        #print(get_best_rating_score(5))

print(get_top_players_score())
