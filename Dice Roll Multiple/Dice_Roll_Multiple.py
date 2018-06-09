import random

def prompt():
    x = input("How many dice would you like to roll? ")
    y = input("How many rolls would you like to simulate? ")
    roll(x, y)

def roll(numDice, numRolls):
    print
    rollResults = []
    for i in range(numRolls):
        total = 0
        for i in range(numDice):
            total += random.randint(1, 6)
        rollResults.append(total)
    #print(rollResults)

    for i in range(numDice, 6*numDice+1):
        count = float(rollResults.count(i))
        percent = (count / len(rollResults))*100
        if count == 1:
            timeString = " time ("
        else:
            timeString = " times ("

        print(str(i) + " was rolled " + str(int(count)) + timeString + str(round(percent, 3)) + "%)")
    print

print("       Dice Rolling Simulator")
print("--------------------------------------")
print
prompt()
