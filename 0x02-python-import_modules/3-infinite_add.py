#!/usr/bin/python3

import sys

if __name__ == "__main__":

    agv = sys.argv
    sum = 0

    if len(agv) > 1:
        for i in range(1, len(agv)):

             sum += int(agv[i])

    print(sum)
