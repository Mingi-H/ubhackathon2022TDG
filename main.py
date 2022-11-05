xcoord = 0
ycoord = 4

import csv

def fieldwrite(filename):
    with open(filename,"w") as f:
        writer = csv.writer(f)
        for x in range(0,7):
            temp = ""
            templist = []
            for k in range(0,81):
                if(x%2==0):
                    temp +="_"
                if(x%2==1):
                    temp +=" "
            templist.append(temp)
            writer.writerow(templist)

fieldwrite("field.csv")

'''def setplayer(filename):
    with open(filename,"a") as f:
        count = 0
        for line in f:
            if(ycoord == )'''

        

'''setplayer("field.txt")'''

def setfield(filename):
    with open (filename) as f:
        reader = csv.reader(f)
        for line in reader:
            for thing in line:
                print(thing)

setfield("field.csv")

'''forever = 1
while forever < 2:
    text = input()
    if text == "":
        print("amogus")
    elif text == "stop":
        forever += 1'''

