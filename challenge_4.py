#challenge #247 [Easy] Secret Santa
#Take input, pair random people together, but make sure they are not in the same family. Families will be indicated by people on the same line.

import sys
import random

f = open('santa_file.txt')

def make_list(file):
    list = []
    for line in f:
        list.append(line.strip('\n').split(' '))
    return list


the_list = make_list(f)
#print the_list
#print type(the_list)
#print len(the_list)
f.close()

def match_up(list):
    print "Starting len(list):",len(list)
    while len(list) > 0:
        print "Current len(list):", len(list)
        num = random.randint(0, len(list)-1)
        num2 = random.randint(0, len(list)-1)
        if num == num2:
            num2 = random.randint(0, len(list)-1)
        else:
            continue
        if len(list[num])>=1:
            print "This is list[num]", list[num]
            print "This is  len(list[num])-1", len(list[num])-1
            len1= len(list[num])-1
            in_num = random.randint(0, len1)
            print "This is random integer of some number <= len list", in_num
            name1 = list[num][in_num]
            
            print "Try, name1", name1
            innerlist = list[num]
            
            b = innerlist.pop(in_num)
            print "Hopefully i removed this same name", b
        elif len(list[num]) == 0:
            list.pop(num)

        else:
           # print "not in the try loop now"
            name1 = list[num]
            print "Not try, name1", name1
            list.pop(num)

        #if len(list[num2])>1:
        #    in_num2 = random.randint(0, len(list[num])-1)
        #    name2 = list[num2][in_num2]
         #   print "Try, name2:", name2
          #  innerlist2 = list[num2]
           
           # a = innerlist2.pop(num2)
            #print "Hopefully i removed this same name", a
            
        if len(list[num2])>= 1:
            print "This is list[num2]", list[num2]
            print "This is  len(list[num2])-1", len(list[num2])-1
            len2= len(list[num2])-1
            in_num2 = random.randint(0, len2)
            print "This is random integer of some number <= len list", in_num2
            name2 = list[num2][in_num2]
            
            print "Try, name2", name2
            innerlist2 = list[num2]
            
            a = innerlist2.pop(in_num2)
            print "Hopefully i removed this same name", a
            
        elif len(list[num2]) == 0:
            list.pop(num2)

        else:
           # print "not in try loop2 now"
            name2 = list[num2]
            print "Not try, name2", name2
            list.pop(num2)
        

match_up(the_list)

## next step, randomly pick two people from the list, they buy things for each other, pop them off the list and do it again.

#random.randint(a, b), maybe try random.randint(1, len(list))
## how to randomize the people within the list within the list?
        
