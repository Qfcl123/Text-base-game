# The intro
import time
import random
def intro():
    print("You have just returned from fighting the evil dragon that thretens the land")
    time.sleep(3)
    print("you were sucsesfull!")
    print("Evrybody thanks you!")
    
# the chosing of the path
def chose():
    print("there are 3 paths")
    print("1 leads to the castle, the second one leads back to the dragons layer,")
    time.sleep(3)
    print("the the third one leads to your house")
    
#the loop
def choese():
    path = ""
    while path != "1" and path != "2" and path != "3":
         path = input("wich path do you go through (1-3):")
        
    return path

def checkpath():
    print("You begin heading down the path")
    time.sleep(2)
    print("You see a fellow knight that congragelates you on slaying the dragon")
    time.sleep(2)
    print("You see a dragon in the distance your muscles tense up...")
    print("")
    time.sleep(2)
    
    corectPath = random.randint(1, 2, 3)
    
    if path == str(corectPath):
       print("That dragon you saw was just a parade for you!")
       time.sleep(2)
       print("Evryone is so happy!")
    else:
       print("A dragon comes and attakes you you die")
    
    
intro()
chose()
choese()
checkpath()g