import requests
from bs4 import BeautifulSoup
from python_utils import converters

def get_parsed_page(url):
    return BeautifulSoup(requests.get(url).text, "lxml")

urls = "http://www.hltv.org/match/2298810-private-vination-99damage-league-season-1"
matches = get_parsed_page(urls)

"""
def get_match_id():
    ma = urls[26:33]
    return ma
"""

def get_map_name():
    nb = matches.findAll("img", style = "border-radius: 4px;;")[0]["src"]
    map_1 = nb[40:-4]
    return map_1

def get_team_1_id():
    ia = matches.find("span", {"style": "vertical-align: -15%;max-width:179px;display: inline-block;white-space: nowrap; overflow: hidden; text-overflow: ellipsis;"})
    sa = ia.find("a", {"style": "color:black;"})["href"]
    da = sa[20:]
    return da

def get_team_2_id():
    ib = matches.find("span", {"style": "vertical-align: -15%;max-width:172px;display: inline-block;white-space: nowrap; overflow: hidden; text-overflow: ellipsis;"})
    sb = ib.find("a", {"style": "color:black;"})["href"]
    db = sb[20:]
    return db

def get_team_1_name():
    team1name = matches.find("a", {"style": "color:black;"})
    return team1name.text

def get_team_2_name():
    b = matches.find("div", {"style": "display:table-cell;width:46%;text-align:left"})
    team2name = b.find("a", {"style": "color:black;"})
    return team2name.text

def get_team_1_map_score(num,math):
    ca = matches.findAll("div", {"class": "hotmatchbox", "style": "margin-top: -7px;font-size: 12px;width:270px;border-top:0;"})[num].findAll("span")[math]
    return ca.text

def get_team_2_map_score():
    cb = matches.findAll("div", {"class": "hotmatchbox", "style": "margin-top: -7px;font-size: 12px;width:270px;border-top:0;"})[1].findAll("span")[1]
    return cb.text

def get_win_team():
    if int(get_team_1_map_score()) > int(get_team_2_map_score()):
        return get_team_1_name()
    elif int(get_team_1_map_score()) < int(get_team_2_map_score()):
        return get_team_2_name()
    else:
        return None

def get_lose_team():
    if int(get_team_1_map_score()) < int(get_team_2_map_score()):
        return get_team_1_name()
    elif int(get_team_1_map_score()) > int(get_team_2_map_score()):
        return get_team_2_name()
    else:
        return None

def get_date():
    da = matches.find("div", {"style": "text-align:center;font-size: 18px;display:flex;flex-direction: row;justify-content: center;align-items: center"})
    date = da.find("span", {"style": "font-size:14px;"}).text.strip().split()
    year = date[3]

    month = date[2]
    if month == "January":
        month = 1
    elif month == "February":
        month = 2
    elif month == "March":
        month = 3
    elif month == "April":
        month = 4
    elif month == "May":
        month = 5
    elif month == "June":
        month = 6
    elif month == "July":
        month = 7
    elif month == "August":
        month = 8
    elif month == "September":
        month = 9
    elif month == "October":
        month = 10
    elif month == "November":
        month = 11
    elif month == "December":
        month = 12
    else:
        month = None

    day = date[0].strip("dhnrst")

    dates = (str(year) + "/" + str(month) + "/" + str(day))

    return dates


###print(get_match_id())
print(get_map_name())
print(get_team_1_id())
print(get_team_2_id())
print(get_team_1_name())
print(get_team_2_name())
print(get_team_1_map_score())
print(get_team_2_map_score())
print(get_win_team())
print(get_lose_team())
print(get_date())
