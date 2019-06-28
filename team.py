# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 19:28:03 2019

@author: ryang
"""
import yaml
import collections
with open('teststats.yml') as fin:
    print("This is running")
    team_data = fin.read()
team_list = yaml.load(team_data)



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
    team_list['Team'][team_entry]['plays'] += 1
    print(current_play)
    if current_play.down == '1st':
        if current_play.success == True:
            team_list['Team'][team_entry]['firstdown_s'] += 1
        elif current_play.success == False:
            team_list['Team'][team_entry]['firstdown_f'] += 1
    elif current_play.down == '2nd':
        if current_play.success == True:
            team_list['Team'][team_entry]['seconddown_s'] += 1
        elif current_play.success == False:
            team_list['Team'][team_entry]['secondown_f'] += 1
    elif current_play.down == '3rd':
        if current_play.success == True:
            team_list['Team'][team_entry]['thirddown_s'] += 1
        elif current_play.success == False:
            team_list['Team'][team_entry]['thirddown_f'] += 1
    elif current_play.down == '4th':
        if current_play.success == True:
            team_list['Team'][team_entry]['fourthdown_s'] += 1
        elif current_play.success == False:
            team_list['Team'][team_entry]['fourthdown_f'] += 1
    
    
    #Parameters are retaining values they shouldn't.
    #Look into this.
    #spyder gui keeping values longer than I thought
    #rewrite files so that it saves and pulls data from safer locations

def commitUpdates():
    #team_list['Team']['Tulane'][0]['plays'] = 74
    with open('testwrite.yml', 'w') as fout:
        print("The dump is also running.")
        yaml.dump(team_list, fout)
       


