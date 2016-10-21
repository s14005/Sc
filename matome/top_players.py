import requests, re
from bs4 import BeautifulSoup
from python_utils import converters

def get_parsed_page(url):
    return BeautifulSoup(requests.get(url).text, "lxml")

urls = "http://www.hltv.org/?pageid=188&matchid=27996"
matches = get_parsed_page(urls)

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

def get_most_damage_user_id():
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:125px;float:left;text-align:left"})

    if len(ka) == 5:
        return None
    else:
        ta = ka[1].find("a")["href"]
        l = len(ta)
        elta = ta[8:]
        transInt = re.match("\d*",elta)
        da = transInt.group()
        if l >= 23:
            return ta[22:]
        elif l < 23:
            return da

def get_most_damage_score():
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style":"font-weight:normal;width:30px;float:left;text-align:right"})
    if len(ka) == 5:
        return None
    else:
        return ka[1].text

def get_most_assists_user_id():
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:125px;float:left;text-align:left"})
    if len(ka) == 5:
        ta = ka[1].find("a")["href"]
    else:
        ta = ka[2].find("a")["href"]
    l = len(ta)
    elta = ta[8:]
    transInt = re.match("\d*",elta)
    da = transInt.group()
    if l >= 23:
        return ta[22:]
    elif l < 23:
        return da


def get_most_assists_score():
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style":"font-weight:normal;width:30px;float:left;text-align:right"})
    if len(ka) == 5:
        return ka[1].text
    else:
        return ka[2].text


def get_most_awp_kills_user_id():
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:125px;float:left;text-align:left"})
    if len(ka) == 5:
        ta = ka[2].find("a")["href"]
    else:
        ta = ka[3].find("a")["href"]
    l = len(ta)
    elta = ta[8:]
    transInt = re.match("\d*",elta)
    da = transInt.group()
    if l >= 23:
        return ta[22:]
    elif l < 23:
        return da

def get_most_awp_kills_score():
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style":"font-weight:normal;width:30px;float:left;text-align:right"})
    if len(ka) == 5:
        return ka[2].text
    else:
        return ka[3].text



def get_most_first_kills_user_id():
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:125px;float:left;text-align:left"})
    if len(ka) == 5:
        ta = ka[3].find("a")["href"]
    else:
        ta = ka[4].find("a")["href"]
    l = len(ta)
    elta = ta[8:]
    transInt = re.match("\d*",elta)
    da = transInt.group()
    if l >= 23:
        return ta[22:]
    elif l < 23:
        return da

def get_most_first_kills_score():
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style":"font-weight:normal;width:30px;float:left;text-align:right"})
    if len(ka) == 5:
        return ka[3].text
    else:
        return ka[4].text


def get_best_rating_user_id():
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:125px;float:left;text-align:left"})
    if len(ka) == 5:
        ta = ka[4].find("a")["href"]
    else:
        ta = ka[5].find("a")["href"]
    l = len(ta)
    elta = ta[8:]
    transInt = re.match("\d*",elta)
    da = transInt.group()
    if l >= 23:
        return ta[22:]
    elif l < 23:
        return da

def get_best_rating_score():
    ka = matches.findAll("div", {"class": "covSmallHeadline", "style":"font-weight:normal;width:30px;float:left;text-align:right"})
    if len(ka) == 5:
        return ka[4].text
    else:
        return ka[5].text



#print(len(get_best_rating_score()))

print(get_most_kills_user_id())
print(get_most_kills_score())
print(get_most_damage_user_id())
print(get_most_damage_score())
print(get_most_assists_user_id())
print(get_most_assists_score())
print(get_most_awp_kills_user_id())
print(get_most_awp_kills_score())
print(get_most_first_kills_user_id())
print(get_most_first_kills_score())
print(get_best_rating_user_id())
print(get_best_rating_score())
