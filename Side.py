import random
from time import sleep
from termcolor import colored
import cv2



def BeginGame(): #This function starts the game and returns the username entered by the user
    print(colored("\n       BagGame","red", attrs=["bold"])+":"+colored(" A Random Tradition       \n","green", attrs=["bold"]))
    sleep(1)
    while True:
        username = input("Enter your username: ").strip()
        if(len(username)<4):
            print("You need to enter a "+colored("valid","red")+" username")
        else:
            break
    print(f"\nHello " + colored(username,"yellow", attrs=["bold"])+", this is " + colored("BagGame","red", attrs=["bold"]) + "..\n")
    sleep(2)
    print("The ancient rules are simple and known in the whole realm, there are three bags that each contain "+colored("10 coins\n","yellow", attrs=["bold"]) +"Your mission is to be the last one that takes coins out of the last bag..\n")
    sleep(2)
    print("Your oponnent is the " + colored("Reigning Legendary Champion", "cyan", attrs=["bold"])+ " of this game..\n")
    sleep(2)
    print("You will be facing " + colored("The Evil Dice","red", attrs=["bold"]) + " of the superior"+ colored(" Wizard of Oz","blue", attrs=["bold"])+"..\n")
    print("\n\n\n")
    sleep(4)
    return username


def HumanTurn(username,Bags): #This function contains the logic of the turn of the player, it takes a username string object and a bags list object to check for it, it returns the bags object and a string object called LastTurn to check for the last turn played
    print("It is now your turn, " + colored(username,"yellow", attrs=["bold"]) + ", choose a bag and a number of coins that doesn't exceed 5\n")
    sleep(1)
    while True:
        try:
            BagChosen = int(input(colored("Bag ","green") +"chosen: "))
            if(BagChosen<1 or BagChosen>3 or Bags[BagChosen-1] == 0):
                raise Exception
            else:
                break
        except:
            print("Please Enter a "+colored("valid","red")+" bag number")
            continue
    sleep(1)
    print("\n")
    while True:
        try:
            NumberOfCoins = int(input("Number of "+ colored("coins","yellow", attrs=["bold"]) +" to take: "))
            if(NumberOfCoins<1 or NumberOfCoins>5 or NumberOfCoins>Bags[BagChosen-1]):
                raise Exception
            else:
                break
        except:
            print("Please Enter a "+colored("valid","red")+" number of coins")
            continue
    Bags[BagChosen-1] = Bags[BagChosen-1] - NumberOfCoins
    LastTurn = username
    return Bags,LastTurn
        

def DiceTurn(Bags): #This function contains the logic of the turn of the evil dice, it takes a bags list object to check for it, it returns the bags object and a string object called LastTurn to check for the last turn played
    print("It is now "+colored("The Evil Dice","red", attrs=["bold"])+"'s turn to choose a bag and a number of coins..\n")
    sleep(1)
    while True:
        BagChosen = random.randint(1,3)
        if(Bags[BagChosen-1]!=0):
            break
    while True:
        NumberOfCoins = random.randint(1,5)
        if(NumberOfCoins<=Bags[BagChosen-1]):
            break
    if(3<Bags[BagChosen-1]<6):
        NumberOfCoins = random.randint(1,3)
        print(colored("The Evil Dice","red", attrs=["bold"])+": I saw this line before..\n")
        sleep(1)
    elif(1<Bags[BagChosen-1]<3):
        NumberOfCoins = Bags[BagChosen-1]
        print(colored("The Evil Dice","red", attrs=["bold"])+": Hmmmm.. Let me try this..\n")
        sleep(1)
    if(Bags[BagChosen-1] < 6 and Bags[BagChosen-1] == max(Bags)):
        NumberOfCoins = Bags[BagChosen-1]
        print(colored("The Evil Dice","red", attrs=["bold"])+": You seem to be better than the last one, though..\n")
        sleep(1)  
    print(colored("The Evil Dice","red", attrs=["bold"])+" chose to take "+colored(f"{NumberOfCoins} coins","yellow")+" from "+colored(f"bag number {BagChosen}","green")+"..\n")
    Bags[BagChosen-1] = Bags[BagChosen-1] - NumberOfCoins
    LastTurn = "Dice"
    return Bags,LastTurn


def CheckGameState(Bags): #This function checks the state of the game, it takes the bags list object as an argument to check for its items
    if(max(Bags)==0):
        return False
    else:
        return True


def EndGame(LastTurn,username):  #This function Ends the game and shows the user who won and end the story in an authentic manner, its arguments are two strings {LastTurn and username}
    print("\n\n\n")
    sleep(1)
    if LastTurn == username:
        image = cv2.imread("Won.jpg")
        print(colored(username+ " WINS AND HE IS THE NEW CHAMPION OF THE REALM !!","red", attrs=["bold"]))
        sleep(3)
        cv2.imshow("You won",image)
        cv2.waitKey(0)
    else:
        image = cv2.imread("Lost.jpg")
        print(colored("The puny human lost..\n","cyan", attrs=["bold"]))
        sleep(1)
        print(colored("The Evil Dice:","red", attrs=["bold"])+colored(" I've beaten you before in all the possible infinite universes and in all of the upcoming and past timelines.\n\n","magenta", attrs=["bold"]))
        sleep(3)
        cv2.imshow("You Lost",image)
        cv2.waitKey(0)
    

def ShowBags(Bags): #This function prints the current Bags and their specific coins
    print("\n")
    for items in Bags:
        sleep(1)
        if(items<10):
            print(colored("*"*5,"green", attrs=["bold"]))
            print(colored("*   *","green", attrs=["bold"]))
            print(colored("* ","green", attrs=["bold"])+colored(items,"yellow", attrs=["bold"])+colored(" *","green", attrs=["bold"]))
            print(colored("*   *","green", attrs=["bold"]))
            print(colored("*"*5,"green", attrs=["bold"]))
        else:
            print(colored("*"*6,"green", attrs=["bold"]))
            print(colored("*    *","green", attrs=["bold"]))
            print(colored("* ","green", attrs=["bold"])+colored(items,"yellow", attrs=["bold"])+colored(" *","green", attrs=["bold"]))
            print(colored("*    *","green", attrs=["bold"]))
            print(colored("*"*6,"green", attrs=["bold"]))
    print("\n")
    
