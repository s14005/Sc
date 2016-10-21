import requests, re
from bs4 import BeautifulSoup
from python_utils import converters

def get_parsed_page(url):
    return BeautifulSoup(requests.get(url).text, "lxml")

urls = "http://www.hltv.org/?pageid=188&matchid=27007"
matches = get_parsed_page(urls)

if urls != matches:
    print("redirect")

def get_most_kills_user_id():
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:125px;float:left;text-align:left"})[0]
    ta = ka.find("a")["href"]
    l = len(ta)
    elta = ta[8:]
    transInt = re.match("\d*",elta)
    da = transInt.group()
    if l >= 23:
        return ta[22:]
    elif l < 23:
        return da

def get_most_kills_score():
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style":"font-weight:normal;width:30px;float:left;text-align:right"})[0].text
    return ka

def get_most_assists_user_id():
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:125px;float:left;text-align:left"})[1]
    ta = ka.find("a")["href"]
    l = len(ta)
    elta = ta[8:]
    transInt = re.match("\d*",elta)
    da = transInt.group()
    if l >= 23:
        return ta[22:]
    elif l < 23:
        return da

def get_most_assists_score():
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style":"font-weight:normal;width:30px;float:left;text-align:right"})[1].text
    return ka


def get_most_awp_kills_user_id():
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:125px;float:left;text-align:left"})[2]
    ta = ka.find("a")["href"]
    l = len(ta)
    elta = ta[8:]
    transInt = re.match("\d*",elta)
    da = transInt.group()
    if l >= 23:
        return ta[22:]
    elif l < 23:
        return da

def get_most_awp_kills_score():
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style":"font-weight:normal;width:30px;float:left;text-align:right"})[2].text
    return ka



def get_most_first_kills_user_id():
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:125px;float:left;text-align:left"})[3]
    ta = ka.find("a")["href"]
    l = len(ta)
    elta = ta[8:]
    transInt = re.match("\d*",elta)
    da = transInt.group()
    if l >= 23:
        return ta[22:]
    elif l < 23:
        return da

def get_most_first_kills_score():
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style":"font-weight:normal;width:30px;float:left;text-align:right"})[3].text
    return ka

def get_best_rating_user_id():
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:125px;float:left;text-align:left"})[4]
    ta = ka.find("a")["href"]
    l = len(ta)
    elta = ta[8:]
    transInt = re.match("\d*",elta)
    da = transInt.group()
    if l >= 23:
        return ta[22:]
    elif l < 23:
        return da

def get_best_rating_score():
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style":"font-weight:normal;width:30px;float:left;text-align:right"})[4].text
    return ka


print(get_most_kills_user_id())
print(get_most_kills_score())
print(get_most_assists_user_id())
print(get_most_assists_score())
print(get_most_awp_kills_user_id())
print(get_most_awp_kills_score())
print(get_most_first_kills_user_id())
print(get_most_first_kills_score())
print(get_best_rating_user_id())
print(get_best_rating_score())
