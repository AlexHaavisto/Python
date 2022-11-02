import random

PlayerWins = 0
BotWins = 0

#Meanings
# 0 = rock
# 1 = paper
# 2 = scissors

while True:
    print("0 = rock, 1 = paper, 2 = scissors, 4 = exit")
    Player movement = int(input("Make your move: "))
    Bot movement = random.randint(0, 2)
    
    if(Player movement == 4):
        break
    elif(Player movement == 0 and Bot movement == 2):
        print("Rock beats scissors! Player + 1")
    elif(Player movement == 1 and Bot movement == 0):
        print("Paper beats rock! Player + 1")
    elif(Player movement == 2 and Bot movement == 0):
        print
