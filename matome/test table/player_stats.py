import requests, re
from bs4 import BeautifulSoup
from python_utils import converters
import sqlite3

connerctor = sqlite3.connect("hltv.db")
def get_parsed_page(url):
    return BeautifulSoup(requests.get(url).text, "lxml")

def get_player_stats(num):
    ma = matches.findAll("div", {"style": "padding-left:5px;padding-top:5px;"})[num]
    mb = ma.findAll("div", {"class": "covSmallHeadline"})[1].text
    return mb

#0~5 Overall_stats
#6~12 Round_stats
#13~18 Opening_stats
#19~23 Weapon_stats

m = 1
while m < 12547:
    urls = "http://www.hltv.org/?pageid=175&playerid="+str(m)
    matches = get_parsed_page(urls)
   # print("playerid" + str(m))
    if int(get_player_stats(6)) == 0:
	print("unti")
    else:
	sql = "insert into overall_stats(player_id, kills, deaths, kill_round, rounds_with_kills) VALUES(?,?,?,?,?);"

	connerctor.execute(sql,(m, get_player_stats(0), get_player_stats(1), get_player_stats(3), get_player_stats(4)))

	sql = "insert into round_stats(player_id, total_rounds, zero_kill_rounds, one_kill_rounds, two_kill_rounds, three_kill_rounds, four_kill_rounds, five_kill_rounds) VALUES(?,?,?,?,?,?,?,?);"

	connerctor.execute(sql,(m, get_player_stats(6), get_player_stats(7), get_player_stats(8), get_player_stats(9), get_player_stats(10), get_player_stats(11), get_player_stats(12)))

	sql = "insert into opening_stats(player_id,  total_opening_kills, total_opening_deaths, opening_kill_rating, team_win_percent_after_first_kill, first_kill_in_won_rounds) VALUES(?,?,?,?,?,?);"

	connerctor.execute(sql,(m, get_player_stats(13), get_player_stats(14), get_player_stats(16), get_player_stats(17), get_player_stats(18)))

	sql = "insert into weapon_stats(player_id, sniper_kill, rifle_kills, pistol_kills, grenade, other) VALUES(?,?,?,?,?,?);"

	connerctor.execute(sql,(m, get_player_stats(19), get_player_stats(20), get_player_stats(21), get_player_stats(22), get_player_stats(23)))
    print("playerid" + str(m))

    if m % 100 == 0:
        connerctor.commit()
    m += 1
connerctor.commit()
connerctor.close()
print("end")

