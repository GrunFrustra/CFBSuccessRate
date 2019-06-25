# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 19:40:13 2019

@author: ryang
"""

import yaml

failwords = ['incomplete', 'false start', 'no gain', 'fumbles']
ignorewords = ['kicks', 'punts', 'extra point', 'field goal', \
               'pass interference', 'penalty']

class Play():
    def __init__(self):
        self.down = None
        self.yards_left = None
        self.play_type = None
        self.result = None
        self.success = None
        
    def writetofile(self):
        #write to yaml file
        #need to figure out how to update file in specific section
        #read yaml documentation
        pass
    
    def determine_success(self):
        post_result_yards = self.yards_left - self.result
        
        if self.down == 'first':
            if post_result_yards <= .5 * yards_left:
                self.success =  True
            else:
                self.success = False
        if self.down == 'second':
            if post_result_yards <= .7 * yards_left:
                self.success = True
            else:
                self.success = False
        if self.down == 'third' or 'fourth':
            if post_result_yards <= 0:
                self.success = True
            else:
                self.success = False
    
    def play_values(self, play_line):
        if any(word in play_line for word in ignorewords):
            print("I found an ignored word.")
            return
        
        if any(word in play_line for word in failwords):
            self.success = False
            
        print(play_line)
            
            