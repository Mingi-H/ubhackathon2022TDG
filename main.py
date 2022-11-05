column = 0
row = 3

import csv

def fieldwrite(filename):
    with open(filename,"w",newline = "") as f:
        writer = csv.writer(f)
        for x in range(0,7):
            templist = []
            for k in range(0,81):
                if(x%2==0):
                    templist.append("-")
                if(x%2==1):
                    templist.append(" ")
            writer.writerow(templist)

fieldwrite("field.csv")

def setplayer(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        out = []
        count = 0
        for line in reader:
            if(line[0] == "P"):
                line.remove("P")
                line.insert(0," ")
            if(row == count):
                temp = line[column]
                line.remove(temp)
                line.insert(0,"P")
            count += 1
            out.append(line)
    with open(filename,"w",newline = "") as w:
        writer = csv.writer(w)
        for list in out:
            writer.writerow(list)

setplayer("field.csv")


def setfield(filename):
    with open (filename) as f:
        reader = csv.reader(f)
        for line in reader:
            temp = ""
            for index in line:
                temp += index
            print(temp)

setfield("field.csv")

print("Welcome to one of the tower defense games(?) of all time! To review the rules and controls, please type rules. If you understand them or want to skip them, just start playing.")

forever = True
while forever == True:
    text = input()
    if text == "stop":
        forever = False
    elif text == "up":
        if(row - 2 >= 1):
            row += -2
            setplayer("field.csv")
            print("you moved up!")
        else:
            print("can't move up any further!")
    elif text == "down":
        if(row + 2 <= 6):
            row += 2
            setplayer("field.csv")
            print("you moved down!")
        else: 
            print("can't move down any further!")
    elif text == "rules":
        with open ("rules.txt") as r:
            for line in r:
                print(line)
    setfield("field.csv")

