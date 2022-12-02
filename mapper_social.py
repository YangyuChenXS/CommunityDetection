#!/usr/bin/python3

import sys

for line in sys.stdin:
    line = line.strip()
    data = line.split()
    print('{0}\t{1}'.format(data[1], data[0]))



