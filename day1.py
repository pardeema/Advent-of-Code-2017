#!/usr/bin/env python

input="428122498997587283996116951397957933569136949848379417125362532269869461185743113733992331379856446362482129646556286611543756564275715359874924898113424472782974789464348626278532936228881786273586278886575828239366794429223317476722337424399239986153675275924113322561873814364451339186918813451685263192891627186769818128715595715444565444581514677521874935942913547121751851631373316122491471564697731298951989511917272684335463436218283261962158671266625299188764589814518793576375629163896349665312991285776595142146261792244475721782941364787968924537841698538288459355159783985638187254653851864874544584878999193242641611859756728634623853475638478923744471563845635468173824196684361934269459459124269196811512927442662761563824323621758785866391424778683599179447845595931928589255935953295111937431266815352781399967295389339626178664148415561175386725992469782888757942558362117938629369129439717427474416851628121191639355646394276451847131182652486561415942815818785884559193483878139351841633366398788657844396925423217662517356486193821341454889283266691224778723833397914224396722559593959125317175899594685524852419495793389481831354787287452367145661829287518771631939314683137722493531318181315216342994141683484111969476952946378314883421677952397588613562958741328987734565492378977396431481215983656814486518865642645612413945129485464979535991675776338786758997128124651311153182816188924935186361813797251997643992686294724699281969473142721116432968216434977684138184481963845141486793996476793954226225885432422654394439882842163295458549755137247614338991879966665925466545111899714943716571113326479432925939227996799951279485722836754457737668191845914566732285928453781818792236447816127492445993945894435692799839217467253986218213131249786833333936332257795191937942688668182629489191693154184177398186462481316834678733713614889439352976144726162214648922159719979143735815478633912633185334529484779322818611438194522292278787653763328944421516569181178517915745625295158611636365253948455727653672922299582352766484"

def part_one():
    #Sum of all Digits that match the next digit in the sequence
    #i.e. 1122 = 3 (1 matches 1, 1 does not match 2, 2 matches 2, 2 does not match 1) --> Circular list
    sum=0
    #We'll hand-jam the last number, so only iterate through the rest first

    for num in range(len(input)-1):
            #print("Is {} equal to {}?".format(input[num], input[num+1]))
            if input[num] == input[num+1]:
                sum+=int(input[num])
                #print("Sum is now {}".format(sum))
    #Last case:
    if input[-1]==input[0]:
        sum+=int(input[-1])
    print ("Part one final sum is {}".format(sum))

def part_two():
    #instead of considering the next digit, 
    #it wants you to consider the digit halfway around the circular list. 
    #That is, if your list contains 10 items, 
    #only include a digit in your sum if the digit 10/2 = 5 steps forward matches it. 
    #Fortunately, your list has an even number of elements.
    #i.e. 1212 == 6; 1 matches the value that is (4/2=) 2 steps ahead
    sum = 0

    #We can just double once we hit the halfway point
    halfway = len(input)/2 
    for num in range(halfway):
        if input[num] == input[num+halfway]:
            sum+=int(input[num])
    print("Final sum is: {}".format(sum*2))

if __name__=="__main__":
    part_one()
    part_two()