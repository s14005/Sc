import requests
from bs4 import BeautifulSoup
from python_utils import converters

def get_parsed_page(url):
    return BeautifulSoup(requests.get(url).text, "lxml")

urls = "http://www.hltv.org/?pageid=188&matchid=27000"
matches = get_parsed_page(urls)

def get_round_team_1(math,num):
    da = matches.findAll("div", {"style": "display:flex;flex-direction: row;justify-content: space-between;height:25px;border-bottom:1px solid rgb(189,189,189);"})[math]
    du = da.findAll("img", {"style": "width:12px;"})[num]["src"]
    if du == "http://static.hltv.org/images/scoreboard/emptyHistory.svg":
        return 2
    elif du != "http://static.hltv.org/images/scoreboard/emptyHistory.svg":
        return 1
"""
def get_round_team_2(math,num):
    da = matches.findAll("div", {"style": "display:flex;flex-direction: row;justify-content: space-between;height:25px;"})[math]
    du = da.findAll("img", {"style": "width:12px;"})[num]["src"]
    if du == "http://static.hltv.org/images/scoreboard/emptyHistory.svg":
        return 1
    elif du != "http://static.hltv.org/images/scoreboard/emptyHistory.svg":
        return 2
"""

def get_round_first_score(math,num):
    da = str(get_round_team_1(math,num)) + "-" + str(get_round_team_1(math,num+1)) + "-" + str(get_round_team_1(math,num+2))
    return da

def get_round_second_score(math,num):
    da = str(get_round_team_1(math,num)) + "-" + str(get_round_team_1(math,num+1)) + "-" + str(get_round_team_1(math,num+2))
    return da


print(get_round_first_score(0,0))
print(get_round_second_score(1,0))

