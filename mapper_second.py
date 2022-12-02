#!/usr/bin/python3

import sys

big_data = []
for line in sys.stdin:
    line = line.strip()
    data = line.split()
    for i in range(len(data)):
        data[i] = data[i].strip("[").strip("]").strip("]").strip(",").strip("'")
    big_data.append(data)
length_big_data = len(big_data)
for i in range(length_big_data):
    data_follower_one = big_data[i][0]
    data_followee_one = big_data[i][1:]
    for j in range(0, length_big_data):
        data_follower_two = big_data[j][0]
        data_followee_two = big_data[j][1:]
        if data_follower_one == data_follower_two:
            continue
        same_data = []
        same_data = [temp_data for temp_data in data_followee_two if temp_data in data_followee_one]
        length_same_data = len(same_data)
        print('{0}\t{1}\t{2}'.format(data_follower_one, data_follower_two, length_same_data))


