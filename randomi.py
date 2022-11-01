import random

PelaajaVoitot = 0
BotiVoitot = 0

#Merkitykset
# 0 = kivi
# 1 = paperi
# 2 = sakset

while True:
    print("0 = kivi, 1 = paperi, 2 = sakset, 4 = exit")
    PelaajanLiike = int(input("Tee Liikkeesi: "))
    BotinLiike = random.randint(0, 2)
    
    if(PelaajanLiike == 4):
        break
    elif(PelaajanLiike == 0 and BotinLiike == 2):
        print("Kivi voittaa sakset! Pelaaja + 1")
    elif(PelaajanLiike == 1 and BotinLiike == 0):
        print("Paperi voittaa kiven! Pelaaja + 1")
    elif(PelaajanLiike == 2 and BotinLiike == 0):
        print