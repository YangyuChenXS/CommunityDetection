import re

if __name__ == "__main__":
    big_data = []
    data = "1558  ['107', '123']".split()
    for i in range(len(data)):
        data[i] = data[i].strip("[").strip("]").strip("]").strip(",").strip("'")
    big_data.append(data)
    data = "1558  ['106', '123']".split()
    for i in range(len(data)):
        data[i] = data[i].strip("[").strip("]").strip("]").strip(",").strip("'")
    big_data.append(data)
    print(big_data)
    big_data_follower = big_data[0][1:]
    print(big_data_follower)

    data_followee_one = [1, 0, 2]
    data_followee_two = [0, 1, 3]
    same_data = []
    same_data = [temp_data for temp_data in data_followee_two if temp_data in data_followee_one]
    print(len(same_data))

    # !/usr/bin/python

    from operator import itemgetter
    import sys

    current_follower_one = None
    current_follower_two_similarity = []
    follower = None

    for line in sys.stdin:
        line = line.strip()
        follower_one, follower_two, similarity = line.split('\t', 2)
        print('{0}\t{1}\t{2}'.format(data_follower_one, data_follower_two, similarity))


'''
big_dict_mapper = {5: 5}
words = [5, 8]
dict_mapper = {}
dict_mapper[words[0]] = words[1]
temp = []
temp.append(big_dict_mapper.get(5))
temp.append(dict_mapper.get(5))
dict_temp = {}
dict_temp[5] = temp
print(dict_temp)
'''

'''
if not line:
    continue
data = line.split('\t', 2)
if len(data) <= 1:
    continue
'''