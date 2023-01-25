import random
import os
import art
import Gamedata
change = {}

def get_two_random():
    if change == {}:
        return [Gamedata.data[random.randint(0,len(Gamedata.data)-1)],Gamedata.data[random.randint(0,len(Gamedata.data)-1)]]
    elif change != {}:
        return [change,Gamedata.data[random.randint(0,len(Gamedata.data)-1)]]

while True:
    
    score = 0
    
    while True:
        
        os.system("clear")
        print(art.logo)
        if score != 0:
            print(f"You're right! Current score {score}")
        getinfo = get_two_random()
        A = getinfo[0]
        B = getinfo[1]
        print(f"{A['name']}, a {A['description']}, From {A['country']}")
        print(art.vs)
        print(f"{B['name']}, a {B['description']}, From {B['country']}")
        gussed = input("Who has more followers? Type 'A' or 'b':\t").lower()
        if gussed == 'a':
            if A['follower_count'] > B['follower_count']:
                change = A
                score+=1
            else:
                print("You lose")
                break
        elif gussed == "b":
            if B['follower_count'] > A['follower_count']:
                change = B
                score+=1
            else:
                print("You lose")
                break
        else:
            print("Wrong key")
            break
            
    
    check   = input("Do you want Play again Y/n").lower()
    if check =="n":
        break
    
    
