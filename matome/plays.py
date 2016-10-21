import sqlite3
import requests
from bs4 import BeautifulSoup
from python_utils import converters
count = 0
num = 6000
unti = 0
list1 = []
#playerpage url get!
def get_parsed_page(url):
    return BeautifulSoup(requests.get(url).text, "lxml")
#players = get_parsed_page("http://www.hltv.org/?pageid=181&mapCountOverride=5")
connector = sqlite3.connect("hltv.db")

#url hairetu
"""
while 1<2:
#playerpages janp
 geturl = players.find_all("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:24%;float:left;"})[unti]
 geturls = geturl.find("a")["href"]

 list1.append(geturls)
 print(list1[num]) #[22:]

 if list1[num][22:] == "12547": #[22:]
     break
 else:
     num += 1
     unti += 2

for urlal in list1:
"""
while 1<2:
  count += 1
  num += 1
  mai = 0
  #playerid
  playerid = "http://www.hltv.org/?pageid=173&playerid=" + str(num)
  #print (playerid[41:])

  player = get_parsed_page(playerid)
  #team_id
  tmp = player.find_all("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:185px;float:left;text-align:right;color:black;"})[3]
  tmp2 = tmp.find("a")["href"]
  if tmp2[20:24] == "0":
      teamid = None
  else:
      teamid = tmp2[20:]

  #player_name
  name = player.find("div", {"class": "covSmallHeadline", "style": "width:100%;float:left;"})
  #print(name.text)

#player_rating
  rating = player.find("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:100px;float:left;text-align:right;color:black;font-weight:bold"})
  #print(rating.text)

  test = player.find_all("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:100px;float:left;text-align:right;color:black"})

#kd_ratio
  kd = player.find_all("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:100px;float:left;text-align:right;color:black"})[3]
#print(kd.text)

#average_kil
  kill = player.find_all("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:100px;float:left;text-align:right;color:black"})[6]

#average_asist
  asa = player.find_all("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:100px;float:left;text-align:right;color:black"})[7]
  asist = asa.text

#print(kill.text)
  if(len(test) == 8):
      asist = 0
      mai = 1
#average_death
  if(0.00 < float(rating.text)):
          death = player.find_all("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:100px;float:left;text-align:right;color:black"})[8-mai]
#print(death.text)

#print(asist.text)
  if(0.00 < float(rating.text)):
      sql = "insert into players (player_id, team_id, player_name, player_rating, kd_ratio, average_kill, average_death, average_asist) VALUES (?,?,?,?,?,?,?,?);"

      connector.execute(sql,(playerid[41:],teamid,name.text,rating.text,kd.text,kill.text,death.text,asist))
      print(playerid[41:])
      print(teamid)
      print(name.text)
      print(rating.text)
      print(kd.text)
      print(kill.text)
      print(death.text)
      print(asist)

  if playerid[41:] == "12547": #12547
      break

  if count % 100 == 0:
      print ("commit")
      connector.commit()
connector.commit()
connector.close()
print("end")
