import requests
from bs4 import BeautifulSoup
from python_utils import converters
import sqlite3
connerctor = sqlite3.connect("test.db")
#i = 25000
i =25010
def get_parsed_page(url):
    return BeautifulSoup(requests.get(url).text, "lxml")

def get_urls_page():
    #matches = get_parsed_page(urls2)
    matcheurl = matches.find_all("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:230px;float:left;text-align:right;"})[2]
    match = matcheurl.find("a")["href"]
    return match

def event1():
    event = matches.find_all("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:230px;float:left;text-align:right;"})[1]
    #events = event
    return event.text


def get_team_1_id():
    du = url1.find("span", {"style": "vertical-align: -15%;max-width:179px;display: inline-block;white-space: nowrap; overflow: hidden; text-overflow: ellipsis;"})
    st = du.find("a", {"style": "color:black;"})["href"]
    do = st[20:]
    return do

def get_team_2_id():
    ma = url1.find("span", {"style": "vertical-align: -15%;max-width:172px;display: inline-block;white-space: nowrap; overflow: hidden; text-overflow: ellipsis;"})
    mb = ma.find("a", {"style": "color:black;"})["href"]
    mc = mb[20:]
    return mc

def get_team_1_name():
    team1name = url1.find("a", {"style": "color:black;"})
    return team1name.text

def get_team_2_name():
    b = url1.find ("div", {"style": "display:table-cell;width:46%;text-align:left"})
    team2name = b.find("a", {"style": "color:black;"})
    return team2name.text

def get_team_1_score():
    team1score = url1.find("span", {"style": "vertical-align:30%;"})
    return int(team1score.text)

def get_team_2_score():
    team2= url1.find("div", {"style": "display:table-cell;width:46%;text-align:left"})
    team2score = team2.find("span", {"style": "vertical-align:30%;"})
    return int(team2score.text)

def get_team_1_1_score():
    if get_best_of() == 1:
        if get_team_1_score() > get_team_2_score():
            return 1
        else:
            return 0
    else:
        return get_team_1_score()

def get_team_2_1_score():
    if get_best_of() == 1:
        if get_team_1_score() < get_team_2_score():
            return 1
        else:
            return 0
    else:
        return get_team_2_score()

def get_best_of():
    bo = url1.find("div", {"id": "mapformatbox"}).text
    ba = bo[13:14]
    return int(ba)

def get_map_name(num):
    map_3 = url1.findAll("img", style= "border-radius: 4px;;")
    if len(map_3) <= num:
        return None

    nb3 = map_3[num]["src"][40:-4]
    return nb3

def get_win_team():
    if int(get_team_1_score()) > int(get_team_2_score()):
        return get_team_1_name()
    elif int(get_team_1_score()) < int(get_team_2_score()):
        return get_team_2_name()
    else:
        return "draw"

def get_lose_team():
    if int(get_team_1_score()) < int(get_team_2_score()):
        return get_team_1_name()
    elif int(get_team_1_score()) > int(get_team_2_score()):
        return get_team_2_name()
    else:
        return "draw"

###mapsdata
#matcheid = num

def get_map_name(num):
    nb = url1.findAll("img", style = "border-radius: 4px;;")[num]["src"]
    map_1 = nb[40:-4]
    return map_1

def get_team_1_map_score(num,math):
    ca = url1.findAll("div", {"class": "hotmatchbox", "style": "margin-top: -7px;font-size: 12px;width:270px;border-top:0;"})[num].findAll("span")[math]
    return int(ca.text)

def get_team_2_map_score(num,math):
    cb = url1.findAll("div", {"class": "hotmatchbox", "style": "margin-top: -7px;font-size: 12px;width:270px;border-top:0;"})[num].findAll("span")[math]
    return int(cb.text)

def map_win_team():
    if get_team_1_map_score(0) > get_team_2_map_score(1):
        return get_team_1_name()
    else:
        return get_team_2_name()

def map_lose_team():
    if get_team_2_map_score(1) < get_team_1_map_score(0):
        return get_team_2_name()
    else:
        return get_team_1_name()

def hanti_team(num):
    ki = matches.find("div", {"class": "covSmallHeadline", "style": "width:100%;float:left;"})
    kk = ki.find_all("a")[num]["href"]
    return kk[20:]

def first_kills_team1():
    kil = matches.find_all("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:100px;float:left;text-align:right;"})[1]
    kill = kil.text.split()
    if int(hanti_team(0)) == int(get_team_1_id()):
        return kill[0]
    else:
        return kill[2]

def first_kills_team2():
    kil = matches.find_all("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:100px;float:left;text-align:right;"})[1]
    kill = kil.text.split()
    if int(hanti_team(0)) == int(get_team_1_id()):
        return kill[2]
    else:
        return kill[0]

def clutches_1_won():
    cl = matches.find_all("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:100px;float:left;text-align:right;"})[2]
    clu = cl.text.split()
    if int(hanti_team(0)) == int(get_team_1_id()):
        return clu[0]
    else:
        return clu[2]

def clutches_2_won():
    cl = matches.find_all("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:100px;float:left;text-align:right;"})[2]
    clu = cl.text.split()
    if int(hanti_team(0)) == int(get_team_1_id()):
        return clu[2]
    else:
        return clu[0]

def bag(num):
     bg = matches.find_all("div", {"class": "tab_content"})[3]
     bb = bg.find_all("a")[num]["href"][21:]

     return int(bb)
tmp = 100
#nu = 0
while 25013 > i:
    urls2 = "http://www.hltv.org/?pageid=188&matchid=" + str(i)
    matches = get_parsed_page(urls2)
    urls = "http://www.hltv.org/" + get_urls_page()
    url1 = get_parsed_page(urls)
    nu = 0
    count = 0
    if int(get_best_of()) == 1:
        if tmp == bag(int(get_team_1_1_score())+int(get_team_2_1_score()-1)):
            print("unti")
           # print(i)
            i += 1
        else:
            for a in range(1, int(get_team_1_1_score())+int(get_team_2_1_score()+1)):
               # nu += 1
                i = int(bag(0))


                urls2 = "http://www.hltv.org/?pageid=188&matchid=" + str(i)

                tmp = i
                matches = get_parsed_page(urls2)
                print(i)
                #print(bag(0))
                print(get_map_name(nu - 1)) #OK
                print(get_team_1_name()) #OK
                print(get_team_2_name()) #OK
                print(get_team_1_map_score((count-1),0))
                print(get_team_2_map_score((count-1),1))
                print(get_win_team())
                print(get_lose_team())
                #print(hanti_team(0))
                print(first_kills_team1())
                print(first_kills_team2())
                print(get_team_1_id())
                print(get_team_2_id())
                print(clutches_1_won())
                print(clutches_2_won())

                i += 1


    else:
        if tmp == bag(int(get_team_1_1_score())+int(get_team_2_1_score())):
            i += 1
            print("unti")
           # print(i)
        else:
            for a in range(1, int(get_team_1_1_score())+int(get_team_2_1_score()+1)):
                nu += 1
                i = int(bag(nu))

                count += 1
                urls2 = "http://www.hltv.org/?pageid=188&matchid=" + str(i)
                tmp = i
                matches = get_parsed_page(urls2)
                print(i)
                #print(bag(1))
                print(get_map_name(nu - 1)) #OK
                print(get_team_1_name()) #OK
                print(get_team_2_name()) #OK
                print(get_team_1_map_score(1,0))
                print(get_team_2_map_score(1,1))
                print(get_win_team())
                print(get_lose_team())
                #print(hanti_team(0))
                print(first_kills_team1())
                print(first_kills_team2())
                print(get_team_1_id())
                print(get_team_2_id())
                print(clutches_1_won())
                print(clutches_2_won())
                i += 1
    #i += 1
print("end")


    #print(i)
    #print(get_map_name(0)) #OK
    #print(get_team_1_name()) #OK
    #print(get_team_2_name()) #OK
    #print(get_team_2_map_score(2))
    #print(get_win_team())
    #print(get_lose_team())
    #print(hanti_team(0))
    #print(first_kills_team1())
    #print(first_kills_team2())
    #print(get_team_1_id())
    #print(get_team_2_id())
    #print(clutches_1_won())
    #print(clutches_2_won())

"""
sql = "insert into matches(event, team_1_id, team_2_id, team_1_name, team_2_name, team_1_score, team_2_score, best_of, map_name_1, map_name_2, map_name_3, map_name_4, map_name_5, win_team, lose_tame) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"

connerctor.execute(sql,(event1(),get_team_1_id(),get_team_2_id(),get_team_1_name(),get_team_2_name(),get_team_1_1_score(),get_team_2_1_score(),get_best_of(),get_map_name(0),get_map_name(1),get_map_name(2),get_map_name(3),get_map_name(4),get_win_team(),get_lose_team()))

connerctor.commit()
connerctor.close()

print(get_team_1_id()) #OK
print(get_team_2_id()) #OK
print(get_team_1_name()) #OK
print(get_team_2_name()) #OK
print(get_team_1_1_score()) #OK
print(get_team_2_1_score()) #OK
print(get_best_of()) #OK
print(get_map_name(0)) #OK
print(get_map_name(1)) #OK
print(get_map_name(2)) #OK
print(get_win_team()) #OK
print(get_lose_team()) #OK
print(event1())
"""
