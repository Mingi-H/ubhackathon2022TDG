column = 0
row = 3

import random
import csv

def fieldwrite(filename):
    with open(filename,"w",newline = "") as f:
        writer = csv.writer(f)
        for x in range(0,7):
            templist = []
            for k in range(0,81):
                if(x%2==0):
                    if(k%2 == 0):
                        templist.append("-")
                    if(k%2 == 1):
                        templist.append(" ")
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

def spawnenemy(filename, enemylist):
    with open(filename) as f:
        reader = csv.reader(f)
        out = []
        spawnlocation = {}
        spawnlane = [1,3,5]
        count = 0
        for enemy in enemylist:
            spawnlocation[enemy] = spawnlane[random.randint(0,2)]
        for line in reader:
            for x in range(1,6,2):
                if(count == x):
                    for enemy in spawnlocation:
                        if spawnlocation[enemy] == x:
                            line.pop()
                            line.append(enemy)
            count += 1
            out.append(line)
    with open(filename,"w",newline = "") as w:
        writer = csv.writer(w)
        for list in out:
            writer.writerow(list)

spawnenemy("field.csv",["BR"])

def setfield(filename):
    with open (filename) as f:
        reader = csv.reader(f)
        for line in reader:
            temp = ""
            for index in line:
                temp += index
            print(temp)

setfield("field.csv")

print("Welcome to one of the tower defense games(?) of all time! To review the rules and controls, please type rules. This game was designed around a big enough console screen, so if the field looks wacky, extend the console by a bit and then reload the program. If you understand them or want to skip them, just start playing. Also, type stop to stop the game.")

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

