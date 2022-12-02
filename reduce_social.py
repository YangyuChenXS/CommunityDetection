#!/usr/bin/python3

from operator import itemgetter
import sys

current_follower = None
current_followee = []
follower = None

for line in sys.stdin:
    line = line.strip()
    follower, followee = line.split('\t', 1)
    if current_follower == follower:
        current_followee.append(followee)
    else:
        if current_follower:
            print('{0}\t{1}'.format(current_follower, current_followee))
        current_followee = []
        current_followee.append(followee)
        current_follower = follower
if current_follower == follower:
    print('{0}\t{1}'.format(current_follower, current_followee))
