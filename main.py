xcoord = 0
ycoord = 4

import csv

def fieldwrite(filename):
    with open(filename,"w") as f:
        writer = csv.writer(f)
        for x in range(0,7):
            templist = []
            for k in range(0,81):
                if(x%2==0):
                    templist.append("_")
                if(x%2==1):
                    templist.append(" ")
            writer.writerow(templist)

fieldwrite("field.csv")

'''def setplayer(filename):
    with open(filename) as f:
        with open(filename,"w") as w:
            reader = csv.reader(f)
            count = 0
            for line in reader:
                if(ycoord = count):
                    line[ycoord].append
                count+=1 

        
setplayer("field.csv")'''

def setfield(filename):
    with open (filename) as f:
        reader = csv.reader(f)
        for line in reader:
            temp = ""
            for index in line:
                temp += index
            print(temp)

setfield("field.csv")

'''forever = 1
while forever < 2:
    text = input()
    if text == "":
        print("amogus")
    elif text == "stop":
        forever += 1'''

