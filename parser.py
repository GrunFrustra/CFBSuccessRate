# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 18:37:34 2019

@author: ryang
"""

from html.parser import HTMLParser
import team
import play



def determine_info(data):
    start_line = data.split(" ")
    #determine if a line is a valid team or play header.  Strips blank and
    #quarter announcements
    if len(start_line) < 2:
        return

    if start_line[0].lower() == start_line[1].lower():
        return 'team'
    elif 'and' in start_line:
        return 'play'
    else:
        return

def read_file(filename):
    with open(filename, 'rt') as testfile:
        data = " "
        while data:
            data = testfile.readline()
            determine_info(data)

read_file('example')

test_play = play.Play()
test_play.play_values("1st and 10 at ND25	\
                      2-D.Williams to ND 36\
                      for 11 yards (34-K.Joseph,1-T.Mullen).")

test = team.retrieve_team('Boston College')
test2 = team.retrieve_team('Alabama')
#team.update_team('Clemson', 42, 14, 45, 12,14, 8, 9, 2, 0)
#team.update_team('Notre Dame', 0, 0, 445, 112,114, 118, 911, 112, 110)
#print(team.retrieve_team('Clemson'))
#print(team.retrieve_team('Notre Dame'))
#print(test)
team.commitUpdates()
