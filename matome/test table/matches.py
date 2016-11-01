import requests, re
from bs4 import BeautifulSoup
from python_utils import converters
import sqlite3
connerctor = sqlite3.connect("hltv.db")
#i = 25001
#i =27993 #test
i = 27938
def get_parsed_page(url):
    return BeautifulSoup(requests.get(url).text, "lxml")

def get_urls_page():
    #matches = get_parsed_page(urls2)
    matcheurl = matches.find_all("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:230px;float:left;text-align:right;"})[2]
    match = matcheurl.find("a")["href"]
    return match

def event1():
    event = url1.find_all("div", {"style": "text-align:center;font-size: 18px;"})[1]
    event1 = event.find("a")["href"]
    return event1[20:]

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
        elif get_team_1_score() == get_team_2_score():
            return 0
        else:
            return 0
    else:
        return get_team_1_score()

def get_team_2_1_score():
    if get_best_of() == 1:
        if get_team_1_score() < get_team_2_score():
            return 1
        elif get_team_1_score() == get_team_2_score():
            return 0
        else:
            return 0
    else:
        return get_team_2_score()

def get_best_of():
    bo = url1.find("div", {"id": "mapformatbox"}).text
    if bo.split()[1] == "Best":
        return int(bo[16:17])
    else:
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

###maps#####################################

def get_team_1_map_score(num,math):
    ca = url1.findAll("div", {"class": "hotmatchbox", "style": "margin-top: -7px;font-size: 12px;width:270px;border-top:0;"})[num].findAll("span")[math]
    return int(ca.text)

def get_team_2_map_score(num,math):
    cb = url1.findAll("div", {"class": "hotmatchbox", "style": "margin-top: -7px;font-size: 12px;width:270px;border-top:0;"})[num].findAll("span")[math]
    return int(cb.text)

def map_win_team(num):
    if get_team_1_map_score(num,0) > get_team_2_map_score(num,1):
        return get_team_1_name()
    else:
        return get_team_2_name()

def map_lose_team(num):
    if get_team_2_map_score(num,1) < get_team_1_map_score(num,0):
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

def unkn():
    un = matches.find("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:180px;float:left;text-align:right;"})
    return un.text

def get_date():
    da = url1.find("div", {"style": "text-align:center;font-size: 18px;display:flex;flex-direction: row;justify-content: center;align-items: center"})
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

#######top_players######
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
#####player_matches#####
def get_player_id(num):
    ma = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:20%;float:left;"})[num] #0~9
    ta = ma.find("a")["href"]
    l = len(ta)
    elta = ta[8:]
    transInt = re.match("\d*",elta)
    da = transInt.group()
    if l >= 23:
        return ta[22:]
    elif l < 23:
        return da

def get_kill(num):
    kill = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:10%;float:left;text-align:center"})[num].text.split()[0]
    return kill

def get_assist(num):
    assist = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:5%;float:left;text-align:center"})[num].text
    return assist

def get_death(num):
    death = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:5%;float:left;text-align:center"})[num+1].text
    return death

def get_kd_ratio(num):
    if (get_adr(0) == None):
        ratio = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:10%;float:left;text-align:center"})[num+1].text
    else:
        ratio = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:8%;float:left;text-align:center"})[num+1].text
    return ratio

def get_adr(num):
    adr = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:8%;float:left;;text-align:center"})
    if len(adr) == 10:
        return adr[num].text
    else:
        return None

def get_rating(num):
    if get_adr(0) == None:
        rating = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:10%;float:left;text-align:center"})[num+2].text
    else:
        rating = matches.findAll("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:8%;float:left;text-align:center"})[num+2].text
    return rating

######round_history
def get_round_team_1(math,num):
    da = matches.findAll("div", {"style": "display:flex;flex-direction: row;justify-content: space-between;height:25px;border-bottom:1px solid rgb(189,189,189);"})[math]
    du = da.findAll("img", {"style": "width:12px;"})[num]["src"]
    if du == "http://static.hltv.org/images/scoreboard/emptyHistory.svg":
        return 2
    elif du != "http://static.hltv.org/images/scoreboard/emptyHistory.svg":
        return 1

def get_round_first_score(math,num):
    da = str(get_round_team_1(math,num)) + "-" + str(get_round_team_1(math,num+1)) + "-" + str(get_round_team_1(math,num+2))
    return da

def get_round_second_score(math,num):
    da = str(get_round_team_1(math,num)) + "-" + str(get_round_team_1(math,num+1)) + "-" + str(get_round_team_1(math,num+2))
    return da

def map_id(num):
    if get_map_name(num) == "dust2":
        return 1
    elif get_map_name(num) == "inferno":
        return 2
    elif get_map_name(num) == "nuke":
        return 3
    elif get_map_name(num) == "train":
        return 4
    elif get_map_name(num) == "mirage":
        return 5
    elif get_map_name(num) == "cache":
        return 6
    elif get_map_name(num) == "cobblestone":
        return 7
    elif get_map_name(num) == "overpass":
        return 8

print("a")
mapid = 4580#matche_id
mapsid = 7867 #sets_id
tmp = 100
while 28000 > i: #28000

    urls2 = "http://www.hltv.org/?pageid=188&matchid=" + str(i)
    matches = get_parsed_page(urls2)
    print("atama")
    while get_urls_page() == "/match/0":
        urls2 = "http://www.hltv.org/?pageid=188&matchid=" + str(i)
        matches = get_parsed_page(urls2)

        i += 1

    urls = "http://www.hltv.org/" + get_urls_page()
    url1 = get_parsed_page(urls)
    nu = 0
    #m = 1
    count = 0
    while unkn() == "Unknown":
        urls2 = "http://www.hltv.org/?pageid=188&matchid=" + str(i)
        matches = get_parsed_page(urls2)

        i += 1


    #if(unkn() == "Unknown"):
    #    i += 1
    #else:
        #sql = "insert into matches(event, team_1_id, team_2_id, team_1_name, team_2_name, team_1_score, team_2_score, best_of, map_name_1, map_name_2, map_name_3, map_name_4, map_name_5, win_team, lose_tame) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"

        #connerctor.execute(sql,(event1(),get_team_1_id(),get_team_2_id(),get_team_1_name(),get_team_2_name(),get_team_1_1_score(),get_team_2_1_score(),get_best_of(),get_map_name(0),get_map_name(1),get_map_name(2),get_map_name(3),get_map_name(4),get_win_team(),get_lose_team()))

        #connerctor.commit()

        print("insert into matches") #######

   # mapid += 1
    if int(get_best_of()) == 1:
        if tmp == bag(int(get_team_1_1_score())+int(get_team_2_1_score()-1)):
            print("unti")
            i += 1
        else:
            mapid += 1
            sql = "insert into matches(event_id, team_1_id, team_2_id, team_1_score, team_2_score, best_of, date) VALUES(?,?,?,?,?,?,?);"

            connerctor.execute(sql,(event1(),get_team_1_id(),get_team_2_id(),get_team_1_1_score(),get_team_2_1_score(),get_best_of(),get_date()))

            #for a in range(1, int(get_team_1_1_score())+int(get_team_2_1_score()+1)):
            nu += 1
            i = int(bag(0))
            count += 1
            mapsid += 1
            urls2 = "http://www.hltv.org/?pageid=188&matchid=" + str(i)

            tmp = i
            matches = get_parsed_page(urls2)
            print("matchipage" + str(i))
            print("match_id" + str(mapid))
            print("map_id" + str(mapsid))

#####round_history
                    #print(get_round_first_score(0,0))
                    #print(get_round_second_score(1,0))

###map.db
            sql = "insert into sets(match_id, map_id, event_id, team_1_id, team_2_id, team_1_map_score, team_2_map_score, first_kills_team1, first_kills_team2, clutches_won_team1, clutches_won_team2, round3_1, round3_2) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?);"

            connerctor.execute(sql,(mapid,map_id(nu-1),event1(),get_team_1_id(),get_team_2_id(),get_team_1_map_score(count-1,0),get_team_2_map_score(count-1,1),first_kills_team1(),first_kills_team2(),clutches_1_won(),clutches_2_won(),None,None))

                    #connerctor.commit()
##top_player
            mvp =["",get_most_kills_score(), get_most_damage_score(), get_most_assists_score(), get_most_awp_kills_score(), get_most_first_kills_score(), get_best_rating_score() ]
            mvppr = ["",get_most_kills_user_id(), get_most_damage_user_id(), get_most_assists_user_id(), get_most_awp_kills_user_id(), get_most_first_kills_user_id(), get_best_rating_user_id()]

            ma=0
            while ma < 6:
                sql = "insert into top_players(player_id, sets_id, mvp_type, score) VALUES(?,?,?,?);"
                ma += 1
                connerctor.execute(sql,(mvppr[ma], mapsid,  ma, mvp[ma]))
                    #connerctor.commit()
            print("unti" + str(i))
            m = 1
            while 11 > m:
                sql = "insert into player_matches(match_id, sets_id, event_id, map_id, player_id,  kill, assist, death, kd_ratio, adr, rating) VALUES(?,?,?,?,?,?,?,?,?,?,?);"
                        #print(str(m))
                if get_adr(0) == None:

                    connerctor.execute(sql,(mapid, mapsid, event1(), map_id(nu-1),  get_player_id(1*m-1), get_kill(3*m-3), get_assist(2*m-2), get_death(2*m-2), get_kd_ratio(3*m-3), get_adr(m-1), get_rating(3*m-3)))

                else:
                    connerctor.execute(sql,(mapid, mapsid, event1(), map_id(nu-1), get_player_id(1*m-1), get_kill(m-1), get_assist(2*m-2), get_death(2*m-2), get_kd_ratio(2*m-3), get_adr(m-1), get_rating(2*m-3)))
                        #connerctor.commit()
                m+=1


            if i % 100 == 0:
                connerctor.commit()
                print("commit")
            i += 1


    else:
        if tmp == bag(int(get_team_1_1_score())+int(get_team_2_1_score())):
            i += 1
            print("unti")
        else:
            mapid += 1

            sql = "insert into matches(event_id, team_1_id, team_2_id, team_1_score, team_2_score, best_of, date) VALUES(?,?,?,?,?,?,?);"

            connerctor.execute(sql,(event1(),get_team_1_id(),get_team_2_id(),get_team_1_1_score(),get_team_2_1_score(),get_best_of(),get_date()))

            for a in range(1, int(get_team_1_1_score())+int(get_team_2_1_score()+1)):
                nu += 1
                i = int(bag(nu))
                mapsid += 1
                count += 1
                urls2 = "http://www.hltv.org/?pageid=188&matchid=" + str(i)
                tmp = i
                matches = get_parsed_page(urls2)
                print("matchipage" + str(i))
                print("match_id" + str(mapid))
                print("map_id" + str(mapsid))
####round_history
                    #print(get_round_first_score(0,0))
                    #print(get_round_second_score(1,0))

                    ###map.db

                sql = "insert into sets(match_id, map_id, event_id, team_1_id, team_2_id, team_1_map_score, team_2_map_score, first_kills_team1, first_kills_team2, clutches_won_team1, clutches_won_team2, round3_1, round3_2) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?);"

                connerctor.execute(sql,(mapid, map_id(nu-1),event1(),get_team_1_id(),get_team_2_id(),get_team_1_map_score(count-1,0),get_team_2_map_score(count-1,1),first_kills_team1(),first_kills_team2(),clutches_1_won(),clutches_2_won(),None,None))

                    #connerctor.commit()

##top_players
                mvp =["",get_most_kills_score(), get_most_damage_score(), get_most_assists_score(), get_most_awp_kills_score(), get_most_first_kills_score(), get_best_rating_score() ]
                mvppr = ["",get_most_kills_user_id(), get_most_damage_user_id(), get_most_assists_user_id(), get_most_awp_kills_user_id(), get_most_first_kills_user_id(), get_best_rating_user_id()]

                m =1
                ma=0
                while 6 > ma:
                    sql = "insert into top_players(player_id, sets_id, mvp_type, score) VALUES(?,?,?,?);"
                    ma += 1
                    connerctor.execute(sql,( mvppr[ma], mapsid, ma, mvp[ma]))

                    #connerctor.commit()
                #print("unti" +str(i))
                m = 1
                while 11 > m:
                    sql = "insert into player_matches(match_id, sets_id, event_id, map_id, player_id, kill, assist, death, kd_ratio, adr, rating) VALUES(?,?,?,?,?,?,?,?,?,?,?);"
                        #print(str(m))
                    if get_adr(0) == None:
                        connerctor.execute(sql,(mapid, mapsid, event1(), map_id(nu-1),  get_player_id(1*m-1), get_kill(3*m-3), get_assist(2*m-2), get_death(2*m-2), get_kd_ratio(3*m-3), get_adr(m-1), get_rating(3*m-3)))

                    else:
                        connerctor.execute(sql,(mapid, mapsid, event1(), map_id(nu-1), get_player_id(1*m-1), get_kill(m-1), get_assist(2*m-2), get_death(2*m-2), get_kd_ratio(2*m-3), get_adr(m-1), get_rating(2*m-3)))
                        #connerctor.commit()
                    m+=1
                if i % 10 == 0:
                    connerctor.commit()
                    print("commit")
                i += 1
print("end")
connerctor.commit()
connerctor.close()


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
###matches.db
sql = "insert into matches(event, team_1_id, team_2_id, team_1_name, team_2_name, team_1_score, team_2_score, best_of, map_name_1, map_name_2, map_name_3, map_name_4, map_name_5, win_team, lose_tame) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"

connerctor.execute(sql,(event1(),get_team_1_id(),get_team_2_id(),get_team_1_name(),get_team_2_name(),get_team_1_1_score(),get_team_2_1_score(),get_best_of(),get_map_name(0),get_map_name(1),get_map_name(2),get_map_name(3),get_map_name(4),get_win_team(),get_lose_team()))

connerctor.close()
connerctor.close()

###map.db
sql = "insert into maps(match_id, map_name, team_1_id, team_2_id, team_1_name, team_2_name, team_1_map_score, team_2_map_score, map_win_team, map_lose_team, date, first_kills_team1, first_kills_team2, clutches_won_team1, clutches_won_team2, round3_1, round3_2) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"

connerctor.execute(sql,(mapid,get_map_name(nu-1),get_team_1_id(),get_team_2_id(),get_team_1_name(),get_team_2_name(),get_team_1_map_score(count-1,0),get_team_2_map_score(count-1,1),map_win_team(count-1),map_lose_team(count-1),get_date(),first_kills_team1(),first_kills_team2(),clutches_1_won(),clutches_2_won(),None,None))

###top_players.db
sql = "insert into top_players(match_id, map_id, most_kills_user_id, most_kills_score, most_damage_user_id, most_damage_score, most_assists_user_id, most_assists_score, most_awp_kills_user_id, most_awp_kills_score, most_first_kills_user_id, most_first_kills_score, best_rating_user_id, best_rating_score) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?);"

connerctor.execute(sql,(mapid, mapsid, get_most_kills_userid(), get_most_kills_score(), get_most_damage_user_id(), get_most_damage_score(),get_ most_assists_user_id(), get_most_assists_score(), get_most_awp_kills_user_id(), get_most_awp_kills_score(), get_most_first_kills_user_id(), get_most_first_kills_score(), get_best_rating_user_id(), get_best_rating_score()))

###player_matches
sql = "insert into player_matches(match_id, map_id, player_id, kill, assist, death, kd_ratio, adr, rating) VALUES(?,?,?,?,?,?,?,?,?);"

##None
connerctor.execute(sql,(mapid, mapsid, get_player_id(1*m-1), get_kill(3*m-3), get_assist(2*m-2), get_death(2*m-2), get_kd_ratio(3*m-3), get_adr(m-1), get_rating(3*m-3)))

###adr++##
connerctor.execute(sql,(mapid, mapsid, get_player_id(1*m-1), get_kill(m-1), get_assist(2*m-2), get_death(2*m-2), get_kd_ratio(2*m-3), get_adr(m-1), get_rating(2*m-3)))

###player_matches##adr++##
print("match_id" + str(mapid))
print("map_id" + str(mapsid))
print(get_player_id(1*m-1)) #OK
print(get_kill(m-1)) #OK
print(get_assist(2*m-2)) #OK
print(get_death(2*m-2)) #OK
print(get_kd_ratio(2*m-3)) #OK
print(get_adr(m-1)) #OK
print(get_rating(2*m-3)) #OK




####player_matches#None
print(get_player_id(1*m-1)) #OK
print(get_kill(3*m-3))
print(get_assist(2*m-2)) #OK
print(get_death(2*m-2)) #OK
print(get_kd_ratio(3*m-3)) #OK
print(get_adr(m-1))
print(get_rating(3*m-3))

######top_players
print(get_most_kills_user_id())
print(get_most_kills_score())
print(get_most_damage_user_id())
print(get_most_damage_score())
print(get_most_first_kills_score())
print(get_most_assists_user_id())
print(get_most_assists_score())
print(get_most_awp_kills_user_id())
print(get_most_awp_kills_score())
print(get_most_first_kills_user_id())
print(get_most_first_kills_score())
print(get_best_rating_user_id())
print(get_best_rating_score())




##map
print(mapid)
print(get_map_name(nu - 1)) #OK
print(get_team_1_id())
print(get_team_2_id())
print(get_team_1_name()) #OK
print(get_team_2_name()) #OK
print(get_team_1_map_score(count-1,0))
print(get_team_2_map_score(count-1,1))
print(map_win_team(count-1))
print(map_lose_team(count-1))
print(first_kills_team1())
print(first_kills_team2())
print(clutches_1_won())
print(clutches_2_won())
print(get_date())


##matches
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
