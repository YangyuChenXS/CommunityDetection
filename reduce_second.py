#!/usr/bin/python3

from operator import itemgetter
import sys

current_follower_one = None
current_follower_two_similarity = []
follower = None

for line in sys.stdin:
    line = line.strip()
    follower_one, follower_two, similarity = line.split('\t', 2)
    if current_follower_one == follower_one:
        current_follower_two_similarity_temp = []
        current_follower_two_similarity_temp.append(follower_two)
        current_follower_two_similarity_temp.append(similarity)
        current_follower_two_similarity.append(current_follower_two_similarity_temp)
    else:
        if current_follower_one:
            sort_list = sorted(current_follower_two_similarity, key=lambda x: x[1])
            print(current_follower_one, end=' ')
            temp_list = []
            j = 0
            for i in range(len(sort_list)):
                if j < 10:
                    temp_list.append(sort_list[len(sort_list)-1-i][0])
                    #print(sort_list[len(sort_list)-1-i][0], end=' ')
                    j = j + 1
                else:
                    break
            print(temp_list)
        current_follower_one = follower_one
        current_follower_two_similarity = []
        temp_list = []
if current_follower_one == follower_one:
    sort_list = sorted(current_follower_two_similarity, key=lambda x: x[1])
    print(current_follower_one, end=' ')
    '''
    j = 0
    for i in range(len(sort_list)):
        if j < 10:
            print(sort_list[len(sort_list) - 1 - i][0], end=' ')
            j = j + 1
        else:
            break
    '''
    temp_list = []
    j = 0
    for i in range(len(sort_list)):
        if j < 10:
            temp_list.append(sort_list[len(sort_list) - 1 - i][0])
            # print(sort_list[len(sort_list)-1-i][0], end=' ')
            j = j + 1
        else:
            break
    print(temp_list)



