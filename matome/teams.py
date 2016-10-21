import sqlite3
import requests
from bs4 import BeautifulSoup
from python_utils import converters
num = 0

def get_parsed_page(url):
    return BeautifulSoup(requests.get(url).text, "lxml")
teamsp = get_parsed_page("http://www.hltv.org/?pageid=182&mapCountOverride=5")
connector = sqlite3.connect("hltv.db")

while  1<2:
  temp = teamsp.find_all("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:40%;float:left;"})[num]
  num += 1
  teamurl = temp.find("a")["href"]

  url = "http://www.hltv.org" + teamurl
  team = get_parsed_page(url)
  nb = url[39:43]

  teamN = team.find("div", {"class": "covSmallHeadline", "style": "width:100%;float:left;"})

  kuni = team.find("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:180px;float:left;"})

 # connector = sqlite3.connect("hltv.db")
  sql = "insert into teams (team_id, team_name, country) VALUES (?,?,?);"

  connector.execute(sql,(nb,teamN.text,kuni.text.strip()))
  connector.commit()
  print(nb)
  print(teamN.text)
  print(kuni.text.strip())
  if nb == "5074":
      break
#connector.commit()
connector.close()
print("end")
