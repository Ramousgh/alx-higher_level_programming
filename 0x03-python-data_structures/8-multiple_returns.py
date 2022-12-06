#!/usr/bin/python3
def multiple_returns(sentence):
    tup = tuple(sentence)
    if tup:
        for i in tup:
            return (len(tup), tup[0])
    else:
        return ( 0, None)
