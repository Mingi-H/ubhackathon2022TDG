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

'''forever = 1
while forever < 2:
    text = input()
    if text == "":
        print("amogus")
    elif text == "stop":
        forever += 1'''

