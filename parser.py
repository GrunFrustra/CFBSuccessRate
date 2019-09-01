# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 18:37:34 2019

@author: ryang
"""

import team
import play



def determine_info(data):
    start_line = data.split(" ")
    while("" in start_line) : 
        start_line.remove("") 
    #determine if a line is a valid team or play header.  Strips blank and
    #quarter announcements
    if len(start_line) < 3:
        return

    if start_line[0].lower() == start_line[1].lower() or \
        start_line[0].lower() == start_line[2].lower() or \
        start_line[0].lower() == start_line[3].lower():
        return 'team'
    elif 'and' in start_line or 'kicks' in start_line or \
    'point' in start_line:
        return 'play'
    else:
        return

def read_file(filename):
    #Verify the logic works and now play lines are skipped
    with open(filename, 'rt') as testfile:
        data = " "
        current_team = " "
        data = testfile.readline()
        #Attempt to remove title= from string before the while loop
        
        while data:
            #Change the team if a line is the start of a drive
            data = data.replace('title=','')
            print(data)
            if determine_info(data) == 'team':
                split_data = data.split()
                current_team = split_data[0]
                print("THIS IS A TEST")
                print(data)
                if split_data[0].lower() == split_data[2].lower():
                    current_team = split_data[0]+ " " + split_data[1]
                if split_data[0].lower() == split_data[3].lower():
                    current_team = split_data[0]+ " " + split_data[1] + \
                    " " + split_data[2]
            elif determine_info(data) == 'play':
                current_play = play.Play()
                current_play.play_values(data.lower())
                
                #Update yaml file
                if current_play.down != None:
                    current_play.determine_success()
                print("START DEBUG")
                print("Down: %s" % current_play.down)
                print("Yards to go: %s " % current_play.yards_left)
                print("Yards result: %s "% current_play.result)
                print("Success: %s"% current_play.success)
                print("END DEBUG")
                team.update_team(current_team, current_play)
            #prepare next line for start of loop
            data = testfile.readline()

read_file('example')

team.commitUpdates()
team.game_report()