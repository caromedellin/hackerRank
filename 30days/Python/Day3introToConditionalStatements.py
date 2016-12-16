#!/bin/python

import sys

N = int(raw_input().strip())
def evaluateWeird(input):
    if (input%2 != 0):
        print "Weird"
    elif(input > 2 and input < 5):
        print "Not Weird"
    elif(input >= 6 and input <= 20):
        print "Weird"
    elif(input > 20):
        print "Not Weird"
evaluateWeird(N)