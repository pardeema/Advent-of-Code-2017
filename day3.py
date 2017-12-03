#!/usr/bin/env python

#Input data is a spiral maze with Point 1,1 in the center

#EX Data
# input= ("17  16  15  14  13"
# "18   5   4   3  12"
# "19   6   1   2  11"
# "20   7   8   9  10")

#Next line would be 21,22,23,24,25
inp = 312051

def make_map(size):
    m=[[5,4,3],[6,1,2],[7,8,9]] #initial seed to make my life easier
    m_sum = [[5,4,2],[10,1,1],[11,23,25]]
   
    row_i = 2
    pt2_row = 2
    loc = "e"
    top=0
    bot=0
    switch_sum=0
    for i in range(10,size+1):       
        if (row_i == 0) and top==1: # Fill in New Top Row
            m[0]=[i]+m[0]
            if len(m[0]) > len(m[1]): #Top Left
                loc="b"
                row_i+=1
                top=0

        elif (row_i==len(m)) and bot==1: #Fill in Bottom Row
            m[-1].append(i)
            if len(m[-1]) >= len(m[0]): #Bottom Right
                loc="e"
                row_i-=1
                bot=0

        elif (loc == "e"): #Right Column Fill in
            m[row_i].append(i)
            if row_i == 0 and len(m[0])==len(m[1]): #Hit the Top Right
                m = [[]] + m #Once we hit the top, add a new row 
                top =1
                loc=""

            if row_i != 0: 
                row_i-=1

        elif loc == "b": #Left Column Fill In
            if row_i+1 > len(m): #Bottom Left Detection
                m.append([i])
                m_sum.append([])
                loc=""
                bot=1
            else:
                m[row_i] = [i] + m[row_i]
            row_i+=1

    return m

def part_one(map_in):
    #Calculate Manhattan Distance to Point 1
    #EX: 12 to 1 == 3 (Down, Left, Left)
    #taxicab distance between (p1,p2) and (q1,q2) is abs(p1-q1) + abs(p2-q2) (From Wiki)
    m=map_in
    p1=0
    p2=0
    q1=0
    q2=0 #p1,p2 will be location of 1; q1,q2 will be location of inp 312051
    switch1, switch2 = False, False
    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c] == 1:
                p1=r
                p2=c
                switch1=True
            if m[r][c] == inp:
                q1=r
                q2=c
                switch2=True
            if switch1 and switch2:
                return ((abs(p1-q1)+abs(p2-q2)))

if __name__=="__main__":
    # m = make_map(35)
    # for r in m:
    #     print(r)    
    m = make_map(inp)
    ans1 = part_one(m)
    print("part_one: {}\npart_two{}".format(ans1, ''))
