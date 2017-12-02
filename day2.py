#!/usr/bin/env python
import os
FILE = os.path.dirname(os.path.realpath(__file__)) + "/day2_input.txt"


def part_one():
    # For example, given the following spreadsheet:

    # 5 1 9 5
    # 7 5 3
    # 2 4 6 8
    # The first row's largest and smallest values are 9 and 1, and their difference is 8.
    # The second row's largest and smallest values are 7 and 3, and their difference is 4.
    # The third row's difference is 6.
    # In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

    # What is the checksum for the spreadsheet in your puzzle input?
    sum = 0
    with open(FILE, 'r') as f:
        for line in f:
            nums = line.split()
            greatest = int(nums[0])
            lowest = int(nums[0])
            for num in nums:
                if int(num) > greatest:
                    greatest = int(num)
                if int(num) < lowest:
                    lowest = int(num)
            sum+=(greatest-lowest)
    print("part one sum is: {}".format(sum))

def part_two():
    # It sounds like the goal is to find the only two numbers in each row where one evenly divides the other - 
    #that is, where the result of the division operation is a whole number. They would like you to find those numbers 
    #on each line, divide them, and add up each line's result.

    # For example, given the following spreadsheet:

    # 5 9 2 8
    # 9 4 7 3
    # 3 8 6 5
    # In the first row, the only two numbers that evenly divide are 8 and 2; the result of this division is 4.
    # In the second row, the two numbers are 9 and 3; the result is 3.
    # In the third row, the result is 2.
    # In this example, the sum of the results would be 4 + 3 + 2 = 9.
    sum = 0
    with open(FILE, 'r') as f:
        for line in f:
            nums = line.split()
            #Iterate through -- if we find num%len(nums) is even, let's flip flop and see if we can find mod == 0 faster:
            for num in nums:
                switch = 0
                if switch == 0:
                    for i in range(len(nums)):
                        denom = int(nums[i])
                        #print("Num is: {}\t num[i] is: {}\tNum Mod i is: {}".format(num,nums[i],int(num)%denom))
                        if nums.index(num) == i: #This is matching itself; keep moving
                            continue
                        if int(num)%denom == 0: #This is the winner; stop evaluating the loop
                            sum+=(int(num)/denom)
                            switch=1
                            break
                else:
                    break
        print("part two sum: {}".format(sum))

if __name__ == "__main__":
    print(FILE)
    part_one()
    part_two()