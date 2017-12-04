#!/usr/bin/env python
import os
FILE = os.path.dirname(os.path.realpath(__file__)) + "/day4_input.txt"


def part_one():
    #Determine number of valid passphrases in a given file
    #Pass phrase is valid if no word appears more than once
    reject = 0
    with open(FILE, 'r') as f:
        size = 0
        for line in f:
            size+=1
            l = line.split()
            while len(l) > 0:
                test = l.pop()
                for word in l:
                    if test == word:
                        reject+=1
                        l=[]
                        break
    valid = size-reject
    print("Pt 1 Size: {}\tReject: {}\tValid:{}".format(size,reject, valid))
    return valid

def part_two():
    #Valid pass phrases cannot be an anagram of each other (not just reverse!)
    reject = 0 
    with open(FILE, 'r') as f:
        size = 0
        for line in f:
            size+=1
            l = line.split()
            while len(l) > 0:
                test = l.pop()
                for word in l:
                    if sorted(test) == sorted(word):
                        reject+=1
                        l=[]
                        break
    valid = size - reject
    print("Pt 2 Size: {}\tReject: {}\tValid:{}".format(size,reject, valid))
    return valid

if __name__=="__main__":
    ans1 = part_one()
    ans2 = part_two()
    print("Ans1: {}\tAns2: {}".format(ans1, ans2))