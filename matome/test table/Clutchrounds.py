import sqlite3
import requests
from bs4 import BeautifulSoup
from python_utils import converters

def get_parsed_page(url):
    return BeautifulSoup(requests.get(url).text, "lxml")

connector = sqlite3.connect("hltv.db")

def round_playerd():
    round = player.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:180px;float:left;text-align:right;color:black;"})[0].text
    return int(round)

def get_win_lose(num):
    win = player.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:180px;float:left;text-align:right;color:black;"})[2].text.split()[num]
    return win
#win=num 0
#lose=num 2
pid = 9700
urls = "http://www.hltv.org/?pageid=194&statsfilter=0&playerid="+str(pid)

player = get_parsed_page(urls)

#pid = 8152

while 12547 > pid:
    urls = "http://www.hltv.org/?pageid=194&playerid="+ str(pid) + "&statsfilter=9"

    player = get_parsed_page(urls)

    if round_playerd() == 0:
	print("nasi")
    else:
        sql = "insert into clutch_played(player_id, rounds_played, win_rounds, loss_rounds) VALUES (?,?,?,?);"

	connector.execute(sql,(pid, round_playerd(), get_win_lose(0), get_win_lose(2)))
        print("playerid" + str(pid))
        print(round_playerd())
        print(get_win_lose(0))
        print(get_win_lose(2))

    if pid%100 == 0:
	connector.commit()
        print("commit")
    pid += 1

connector.close()
print("end")
#print float(get_win_lose(0)) / float(round_playerd())
#print(round_playerd())
#print(get_win_lose(0))
#print(get_win_lose(2))
