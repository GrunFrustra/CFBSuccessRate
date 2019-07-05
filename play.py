# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 19:40:13 2019

@author: ryang
"""

import yaml

failwords = ['incomplete', 'false start', 'no gain', 'fumbles', 'intercepted']
ignorewords = ['kicks', 'punts', 'extra point', 'field goal', \
               'pass interference', 'penalty', 'No play', 'touchback']
downs = ['1st','2nd','3rd','4th']
zeroyards = ['incomplete', 'no gain', 'intercepted']

class Play():
    def __init__(self):
        self.down = None
        self.yards_left = None
        self.result = 0
        self.success = None
        
    def writetofile(self):
        #write to yaml file
        #need to figure out how to update file in specific section
        #read yaml documentation
        pass
    
    #Determine if a play succeeded in the appropriate down of the play.
    def determine_success(self):
        print("Current yards left: %s" %self.yards_left)
        print("Current result: %s" %self.result)
        post_result_yards = int(self.yards_left) - int(self.result)
        print("POST RESULT YARDS IS %f" %post_result_yards)
        #2nd and 10 at WMC15     
        #2-L.Bellamy pushed ob at WMC 23 for 8 yards (41-R.Guthrie).
        if self.down == '1st':
            print("I'M IN THE FIRST DOWN LOGIC")
            print("yards left * .5 is %f" %(.5 * float(self.yards_left)))
            if float(post_result_yards) <= .5 * float(self.yards_left):
                print("SUCCESS!!!!!!!!!")
                self.success =  True
            else:
                self.success = False
        if self.down == '2nd':
            if float(post_result_yards) <= .7 * float(self.yards_left):
                self.success = True
            else:
                self.success = False
        if self.down == '3rd' or '4th':
            if float(post_result_yards) <= 0.0:
                self.success = True
            else:
                self.success = False
    
    def play_values(self, play_line):
        #Check if a play should be ignored based on words used in description.
        if any(word in play_line for word in ignorewords):
            print("I found an ignored word.")
            return
        if any(word in play_line for word in failwords):
            self.success = False
            
        play_list = str.split(play_line)
        
        #Get what down it is.  Ignore if it doesn't fit the play format.
        if play_list[0] in downs:
            self.down = play_list[0]
        else:
            print("UNAVAILABLE STRING")
            print(play_list[0])
        
        #Get how many yards are left to a first down
        if play_list[play_list.index('and') + 1]:
            self.yards_left = play_list[play_list.index('and') + 1]
        
        if self.success == False:
            pass
        elif any(word in play_line for word in zeroyards):
            self.result = 0
        else:
            self.result = play_list[play_list.index('for') + 1]
            if self.result == 'a':
                self.result = play_list[play_list.index('for') - 2]
#        print("DOWN IS %s" % self.down)
#        print("YARDS LEFT IS %s" % self.yards_left)
#        print("RESULT IS %s " % self.result)
#        print(play_line)
            
            