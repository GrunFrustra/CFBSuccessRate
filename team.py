# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 19:28:03 2019

@author: ryang
"""
import yaml
import collections
with open('teamstats.yml') as fin:
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
    #print(team_list['Team'][team_needed])
    return team_list['Team'][team_needed]

def update_team(team_entry, plays, first_s, first_f, second_s, second_f, third_s, third_f, fourth_s, fourth_f):
    team_list['Team'][team_entry]['plays'] += plays
    team_list['Team'][team_entry]['firstdown_s'] += first_s
    team_list['Team'][team_entry]['firstdown_f'] += first_f
    team_list['Team'][team_entry]['seconddown_s'] += second_s
    team_list['Team'][team_entry]['secondown_f'] += second_f
    team_list['Team'][team_entry]['thirddown_s'] += third_s
    team_list['Team'][team_entry]['thirddown_f'] += third_f
    team_list['Team'][team_entry]['fourthdown_s'] += fourth_s
    team_list['Team'][team_entry]['fourthdown_f'] += fourth_f
    #RUN SOME TESTS FIRST

def commitUpdates():
    #team_list['Team']['Tulane'][0]['plays'] = 74
    with open('testwrite.yml', 'w') as fout:
        yaml.dump(team_list, fout)
       


