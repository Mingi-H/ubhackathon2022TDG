column = 0
row = 3
player_dmg = 3
import random
import csv
import os

#This line of code exists to just reset the enemy file every time a new run starts. Otherwise, it keeps the enemies from last game and things get really weird.
with open("enemy.csv","w",newline = "") as f:
    temp = 3

#This code creates the "field", or basically the battle arena where the player has to shoot down the robots.

def fieldwrite(filename):
    with open(filename,"w",newline = "") as f:
        writer = csv.writer(f)
        for x in range(0,7):
            templist = []
            for k in range(0,81):
                if(x%2==0):
                    if(k%4 == 0):
                        templist.append("-")
                    else:
                        templist.append(" ")
                if(x%2==1):
                    templist.append(" ")
            writer.writerow(templist)

#this code creates the player. Basically, it copies the field that is active right now, adds a P to the left, and then overwrites the field.

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

#This code spawns the enemy, which basically much like creating the player, copies the field.csv and then puts an enemy on the far right.

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
                            enemyregister(enemylist,spawnlocation[enemy],80)
            count += 1
            out.append(line)
    with open(filename,"w",newline = "") as w:
        writer = csv.writer(w)
        for list in out:
            writer.writerow(list)

#What this code does is it basically puts the enemy into an enemy.csv file, so that we can now keep track of which enemies have what health, are on what location, etc.

def enemyregister(enemylist,y,x):
    out = []
    with open("enemydictionary.csv") as f:
        reader = csv.reader(f)
        for line in reader:
            for enemy in enemylist:
                if(enemy == line[1]):
                    out.append([line[1],line[2],line[3],y,x])
    with open ("enemy.csv","a",newline = "") as f:
        writer = csv.writer(f)
        for list in out:
            writer.writerow(list)

#This code looks at what is currently in field.csv, and then copies it to the console to make it readable for the player.

def setfield(filename):
    with open (filename) as f:
        reader = csv.reader(f)
        for line in reader:
            temp = ""
            for index in line:
                temp += index
            print(temp)

def fieldupdate():
    out = []
    with open("field.csv") as f:
        reader = csv.reader(f)
        for line in reader:
            out.append(line)
    for list in out:
        for index in range(len(list)):
            if list[index] == "R":
                list[index]= " "
    with open("enemy.csv") as f:
        reader = csv.reader(f)
        for line in reader:
            out[int(line[3])][int(line[4])] = line[0]
    with open ("field.csv","w",newline = "") as f:
        writer = csv.writer(f)
        for list in out:
            writer.writerow(list)
    
def updateenemyposition():
    with open("enemy.csv") as e:
        out = []
        readerenemy = csv.reader(e)
        for line in readerenemy:
            line[4] = int(line[4]) - int(line[2])
            out.append(line)
    with open ("enemy.csv","w",newline = "") as f:
        writer = csv.writer(f)
        for list in out:
            writer.writerow(list)

def updateenemyhealth(xcoord):
    with open("enemy.csv") as e:
        out = []
        readerenemy = csv.reader(e)
        for line in readerenemy:
            if(int(line[3]) == xcoord):
                line[1] = int(line[1]) - player_dmg
            out.append(line)
    with open ("enemy.csv","w",newline = "") as f:
        writer = csv.writer(f)
        for list in out:
            writer.writerow(list)

def enemywalk():
    emptycheck()
    with open("field.csv") as f:
        with open("enemy.csv") as e:
            out = []
            reader = csv.reader(f)
            readerenemy = csv.reader(e)
            for lineenemy in readerenemy:
                for line in reader:
                    if lineenemy[0] in line:
                        temp = line.index(lineenemy[0])
                        line.remove(lineenemy[0])
                        line.insert(temp, " ")
                        line.remove(line[temp - int(lineenemy[2])])
                        line.insert(temp-int(lineenemy[2]),lineenemy[0])
                    out.append(line)
    with open("field.csv","w",newline = "") as w:
        writer = csv.writer(w)
        for list in out:
            writer.writerow(list)
    updateenemyposition()
    fieldupdate()

def searchenemy():
    with open("field.csv") as f:
        with open("enemy.csv") as e:
            reader = csv.reader(f)
            readerenemy = csv.reader(e)
            for lineenemy in readerenemy:
                count = 0
                for line in reader:
                    if(lineenemy[0] in line and int(lineenemy[3]) == count and row == count):
                        updateenemyhealth(count)
                        return True
                    count += 1
                
def shoot():
    with open("field.csv") as f:
        reader = csv.reader(f)
        count = 0
        for line in reader:
            if(row == count):
                print("Bang!")
                if(searchenemy() == True):
                    print("nice shot! You dealt " + str(player_dmg) + " damage!")
                else:
                    print("Aww... you missed...")
            count += 1

def enemydeath():
    out = []
    with open("enemy.csv") as f:
        reader = csv.reader(f)
        count = 0
        for line in reader:
            if (int(line[1]) > 0):
                out.append(line)
            else: 
                enemyunregister(line[3],count)
            count += 1
    with open("enemy.csv","w",newline = "") as w:
        writer = csv.writer(w)
        for list in out:
            writer.writerow(list)
    emptycheck()

def enemyunregister(num1,num2):
    with open("field.csv") as f:
        with open("enemy.csv") as e:
            enemyreader = csv.reader(e)
            reader = csv.reader(f)
            out = []
            count = 0
            for enemyline in enemyreader:
                if(num2 == count):
                    position = int(enemyline[4])
                count += 1
            count = 0
            for line in reader:
                if(int(num1) == count):
                    line.pop(position)
                    line.insert(position," ")
                out.append(line)
                count += 1
    with open("field.csv","w",newline = "") as w:
        writer = csv.writer(w)
        for list in out:
            writer.writerow(list)

def emptycheck():
    with open("enemy.csv") as f:
        if(os.stat("enemy.csv").st_size == 0):
            spawnenemy("field.csv",["R"])

def checkplayerdeath():
    with open("enemy.csv") as f:
        reader = csv.reader(f)
        for line in reader:
            if(int(line[4]) <= 0):
                print("Nooo! The Robots learned Obama's last name, and you got fired from your job for not being able to protect it... Game Over :(")
                return True
    return False

fieldwrite("field.csv")
setplayer("field.csv")
spawnenemy("field.csv",["R"])
print("Welcome to one of the tower defense games of all time! To review the rules and controls, please type rules. To see how to read the enemy stats, type enemy. This game was designed around a big enough console screen, so if the field looks wacky, extend the console by a bit and then reload the program. If you understand the rules or want to skip them, just start playing. Also, type stop to stop the game. Remember that typing help at any time will cause this to be printed again!")
setfield("field.csv")

forever = True
turn = 0

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
    elif text == "enemy":
        with open ("readingenemy.txt") as r:
            for line in r:
                print(line)
    elif text == "help":
        print("Welcome to one of the tower defense games of all time! To review the rules and controls, please type rules. To see how to read the enemy stats, type enemy. This game was designed around a big enough console screen, so if the field looks wacky, extend the console by a bit and then reload the program. If you understand the rules or want to skip them, just start playing. Also, type stop to stop the game. Remember that typing help at any time will cause this to be printed again!")
    elif text == "":
        enemydeath()
        enemywalk()
        turn += 1
    elif text == "shoot":
        shoot()
        enemydeath()
        enemywalk()
        turn += 1
    print("it is currently turn " + str(turn) + " out of 50.")
    if(turn == 5):
        spawnenemy("field.csv",["R"])
    if(turn == 8):
        spawnenemy("field.csv",["R"])
    if(turn == 9):
        spawnenemy("field.csv",["R"])
    if(turn == 14):
        spawnenemy("field.csv",["R"])
    if(turn == 15):
        spawnenemy("field.csv",["R"])
    if(turn == 16):
        spawnenemy("field.csv",["R"])
    if(turn == 20):
        spawnenemy("field.csv",["R"])
    if(turn == 25):
        spawnenemy("field.csv",["R"])
    if(turn == 26):
        spawnenemy("field.csv",["R"])
    if(turn == 27):
        spawnenemy("field.csv",["R"])
    if(turn == 50):
        forever = False
        print("You've survived the day... congratulations on finishing the demo! I was getting sick of looking at csv files also it's 3:00 AM, so that's it for now! cya!")
    if(checkplayerdeath() == True):
        forever = False
    setfield("field.csv")
    

