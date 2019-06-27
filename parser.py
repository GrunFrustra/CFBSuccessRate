# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 18:37:34 2019

@author: ryang
"""

import team
import play



def determine_info(data):
    start_line = data.split(" ")
    #determine if a line is a valid team or play header.  Strips blank and
    #quarter announcements
    if len(start_line) < 3:
        return

    if start_line[0].lower() == start_line[1].lower() or \
        start_line[0].lower() == start_line[2].lower():
        print(start_line)
        return 'team'
    elif 'and' in start_line:
        print(start_line)
        return 'play'
    else:
        return

def read_file(filename):
    #Verify the logic works and now play lines are skipped
    with open(filename, 'rt') as testfile:
        data = " "
        while data:
            data = testfile.readline()
            if determine_info(data) == 'team':
                data = testfile.readline()
                
                #determine if the current line is a play
                #play functions will be called in this loop
                while determine_info(data) == 'play':
                    print("Team play")
#                    current_play = play.Play()
#                    current_play.play_values(data)

                    
                    
                    data = testfile.readline()

read_file('example')



#test_play = play.Play()
#test_play.play_values("1st and 15 at ND31	2-D.Williams to ND 31, \
#                      FUMBLES (19-T.Muse). 2-D.Williams to ND 31 for\
#                      no gain.")

#if(test_play.success != None):
#    test_play.determine_success()
#    print("Play is %s" %test_play.success)

#test = team.retrieve_team('Boston College')
#test2 = team.retrieve_team('Alabama')
#team.update_team('Clemson', test_play)
#team.update_team('Notre Dame', 0, 0, 445, 112,114, 118, 911, 112, 110)
#print(team.retrieve_team('Clemson'))
#print(team.retrieve_team('Notre Dame'))
#print(test)
team.commitUpdates()