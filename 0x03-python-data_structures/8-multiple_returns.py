#!/usr/bin/python3
def multiple_returns(sentence):
    len_s = len(sentence)
    if len_s == 0:
        return (0, None)
    return len_s, sentence[0]
