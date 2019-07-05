# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 19:28:03 2019

@author: ryang
"""
import yaml
import collections
#File used to keep historical success rate
with open('testwrite.yml') as fin:
    print("This is running")
    team_data = fin.read()
team_list = yaml.load(team_data)

#File used to calculate game-by-game success rate
#teststats is all 0 data
with open('teststats.yml') as game_fin:
    print("Opening second gamedata file")
    game_data = game_fin.read()
game_list = yaml.load(game_data)
game_report_teams = set()
    

with open('backup.yml', 'w') as backup:
    print("The dump is also running.")
    yaml.dump(team_list, backup)
       

class Team():
    def __init__(self, name):
        self.name = name
        self.plays = 0
        self.firstsuccess = 0
        self.firstfail = 0
        self.secondsuccess = 0
        self.secondfail = 0
        self.thirdsuccess = 0
        self.thirdfail = 0
        self.fourthsuccess = 0
        self.fourthfail = 0

def retrieve_team(team_needed):
    return team_list['Team'][team_needed]

def update_team(team_entry, current_play):
    game_report_teams.add(team_entry)
    
    #Remove white space in broken team names.
    team_entry = team_entry.strip()
    
    team_list['Team'][team_entry]['plays'] += 1
    game_list['Team'][team_entry]['plays'] += 1
    print(current_play)
    if current_play.down == '1st':
        if current_play.success == True:
            team_list['Team'][team_entry]['firstdown_s'] += 1
            game_list['Team'][team_entry]['firstdown_s'] += 1
        elif current_play.success == False:
            team_list['Team'][team_entry]['firstdown_f'] += 1
            game_list['Team'][team_entry]['firstdown_f'] += 1
    elif current_play.down == '2nd':
        if current_play.success == True:
            team_list['Team'][team_entry]['seconddown_s'] += 1
            game_list['Team'][team_entry]['seconddown_s'] += 1
        elif current_play.success == False:
            team_list['Team'][team_entry]['secondown_f'] += 1
            game_list['Team'][team_entry]['secondown_f'] += 1
    elif current_play.down == '3rd':
        if current_play.success == True:
            team_list['Team'][team_entry]['thirddown_s'] += 1
            game_list['Team'][team_entry]['thirddown_s'] += 1
        elif current_play.success == False:
            team_list['Team'][team_entry]['thirddown_f'] += 1
            game_list['Team'][team_entry]['thirddown_f'] += 1
    elif current_play.down == '4th':
        if current_play.success == True:
            team_list['Team'][team_entry]['fourthdown_s'] += 1
            game_list['Team'][team_entry]['fourthdown_s'] += 1
        elif current_play.success == False:
            team_list['Team'][team_entry]['fourthdown_f'] += 1
            game_list['Team'][team_entry]['fourthdown_f'] += 1
    
def game_report():
    i = 0
    team1 = ''
    team1srate = 0.0
    team1scount = 0
    team1fcount = 0
    
    team2 = ''
    team2srate = 0.0
    team2scount = 0
    team2fcount = 0
    
    for x in game_report_teams:
        if i == 0:
            team1 = x.strip()
        elif i == 1:
            team2 = x.strip()
        i += 1
    print("----------")
    print("%s vs. %s" % (team1, team2))
    print("----------")
    team1scount = game_list['Team'][team1]['firstdown_s'] + \
                game_list['Team'][team1]['seconddown_s'] + \
                game_list['Team'][team1]['thirddown_s'] + \
                game_list['Team'][team1]['fourthdown_s']
    team1fcount = game_list['Team'][team1]['firstdown_f'] + \
                game_list['Team'][team1]['secondown_f'] + \
                game_list['Team'][team1]['thirddown_f'] + \
                game_list['Team'][team1]['fourthdown_f']
    team2scount = game_list['Team'][team2]['firstdown_s'] + \
                game_list['Team'][team2]['seconddown_s'] + \
                game_list['Team'][team2]['thirddown_s'] + \
                game_list['Team'][team2]['fourthdown_s']
    team2fcount = game_list['Team'][team2]['firstdown_f'] + \
                game_list['Team'][team2]['secondown_f'] + \
                game_list['Team'][team2]['thirddown_f'] + \
                game_list['Team'][team2]['fourthdown_f']
                
    team1srate = team1scount / team1fcount
    team2srate = team2scount / team2fcount
    
    #Print to console
    print(team1 + "\n")
    print("Successful Plays: %d \n" % team1scount)
    print("Failed Plays: %d \n" % team1fcount)
    print("Success Rate: %f \n" % team1srate)
    print(team2 + "\n")
    print("Successful Plays: %d \n" % team2scount)
    print("Failed Plays: %d \n" % team2fcount)
    print("Success Rate: %f \n" % team2srate)
    print("\n")
    
    #Append to files
    file_name = team1 + " vs. " + team2
    write_to_files = [team1, team2]
    for x in write_to_files:
        with open('./Games/' + x + ".txt", 'a') as fout:
            fout.write(team1 + "\n")
            fout.write("Successful Plays: %d \n" % team1scount)
            fout.write("Failed Plays: %d \n" % team1fcount)
            fout.write("Success Rate: %f \n" % team1srate)
            fout.write(team2 + "\n")
            fout.write("Successful Plays: %d \n" % team2scount)
            fout.write("Failed Plays: %d \n" % team2fcount)
            fout.write("Success Rate: %f \n" % team2srate)
            fout.write("\n")

def commitUpdates():
    #team_list['Team']['Tulane'][0]['plays'] = 74
    with open('testwrite.yml', 'w') as fout:
        print("The dump is also running.")
        yaml.dump(team_list, fout)
        
    with open('gamestats.yml', 'w') as fout:
        print("Second dump")
        yaml.dump(game_list, fout)
       


