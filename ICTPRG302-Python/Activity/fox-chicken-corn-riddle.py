"""
The Fox, Chicken, and Corn Problem
Ashby Scattini
File: fox_chicken_corn.py
CopyRight 2025, Ashby Scattini 2025

"""
"""
Possible Variables i may need.


boat_full = False
fox_in_boat = False
chicken_in_boat = False
corn_in_boat = False
fox_on_left = True
chicken_on_left = True
corn_on_left = True

def pick_up_item(fox, chicken, corn):
    need a user input to ask what they want to move over. 


def can_boat_move(left, right):
    need to check if the boat can move left or right or if they are on the same side already.
    need to check if the boat can move left or right or if they are on the same side already.
    need to check if the fox is on the same side as the chicken alone and if the chicken is on the same side as the corn alone.
    
def place_item(fox, chicken, corn):
    need to check if the corn, fox, and chicken are on the right side of the river. can only win when all are on the right side 
    of the river.
    if not player does not win they must continue to play until solved.

"""
# Setting up variables for the game. Corn starts on the boat.
user_input = ""
boat_full = False
fox_in_boat = False
chicken_in_boat = False
corn_in_boat = False
fox_on_right = False
chicken_on_right = False
corn_on_right = False
game_win = False
left = True
right = False
game_lose = False

# Welcome message and instructions for the game.
print("Welcome to the Fox, Chicken, and Corn Problem")
print("You will need to move the fox, chicken, and corn across the river to the right side.")
print("You can only move one item at a time.")
print("You cannot leave the fox alone with the chicken or the chicken alone with the corn.")
print("use the following commands to move items: pick up, fox, chicken, corn, left, right, place, exit")

# Function to check if the boat can move left or right or if they are on the same side already.
def boat_move(left, right):
    if user_input.lower() == "left" and left == True:
        print("The boat is already on the left side.")
        left = True
        right = False
    elif user_input.lower() == "left" and left == False:
        print("The boat is now on the left side.")
        left = True
        right = False
    elif user_input.lower() == "right" and right == True:
        print("The boat is already on the right side.")
        left = False
        right = True
    elif user_input.lower() == "right" and right == False:
        print("The boat is now on the right side.")
        left = False
        right = True
    return left, right

# Function to place current item in boat.
def place_item(fox_in_boat, chicken_in_boat, corn_in_boat, fox_on_right, chicken_on_right, corn_on_right, boat_full):
    if boat_full == True:
        if fox_in_boat == True:
            if left == True:
                print("The fox is now on the left side.")
                fox_on_right = False
                boat_full = False
            if right == True:
                print("The fox is now on the right side.")
                fox_on_right = True
                boat_full = False
        elif chicken_in_boat == True:
            if left == True:               
                print("The chicken is now on the left side.")
                chicken_on_right = False
                boat_full = False
            if right == True:
                print("The chicken is now on the right side.")
                chicken_on_right = True
                boat_full = False
        elif corn_in_boat == True:
            if left == True:
                print("The corn is now on the left side.")
                corn_on_right = False
                boat_full = False
            if right == True:
                print("The corn is now on the right side.")
                corn_on_right = True
                boat_full = False

    elif boat_full == False:
        print("The boat is empty.")
    
    return fox_in_boat, chicken_in_boat, corn_in_boat, fox_on_right, chicken_on_right, corn_on_right, boat_full

# Function to pick up item and check if they already have an item in the boat.
def pick_up_item(fox_in_boat, chicken_in_boat, corn_in_boat, boat_full, user_input):
    if boat_full == False:
        user_input = input("What would you like to pick up?(Fox, Chicken, Corn):> ")
        if user_input.lower() == "fox":
            print("Fox is now in the boat.")
            fox_in_boat = True
            boat_full = True
        if user_input.lower() == "chicken":
            print("Chicken is now in the boat.")
            chicken_in_boat = True
            boat_full = True
        if user_input.lower() == "corn":
            print("Corn is now in the boat.")
            corn_in_boat = True
            boat_full = True
    else:
        print("The boat is already full.")
    user_input = ""
    return fox_in_boat, chicken_in_boat, corn_in_boat, boat_full
    

# Function to check if the player has won the game.
def check_game_win(fox_on_right, chicken_on_right, corn_on_right, game_win):
    if fox_on_right == True and chicken_on_right == True and corn_on_right == True:
        game_win = True
        return game_win
    else:
        return fox_on_right, chicken_on_right, corn_on_right, game_win

# Function to check if the player has lost the game.
def lost_game(fox_on_right, chicken_on_right, corn_on_right, game_lose):
    # check if chicken and corn are on same side.
    if fox_on_right == False and chicken_on_right == True and corn_on_right == True:
        game_lose = True
        print("The chicken has eaten the corn.")
        print("You have lost the game.")
        exit()
        return game_lose
    # check if fox and chicken are on the same side.
    if fox_on_right == True and chicken_on_right == True and corn_on_right == False:
        game_lose = True
        print("The fox has eaten the chicken.")
        print("You have lost the game.")
        exit()
        return game_lose
    else:
        return fox_on_right, chicken_on_right, corn_on_right, game_lose

# Main game loop.
while game_win == False:
    # ask for user input and call in functions from abovce to move items.
    # check if the player has won the game.
    # inputs, Fox, Chicken, Corn, Left, Right, Exit, Place, Pick up.
    fox_on_right, chicken_on_right, corn_on_right, game_lose = lost_game(fox_on_right, chicken_on_right, corn_on_right, game_lose)
    user_input = input("what would you like to do?:> ")
    check_game_win(fox_on_right, chicken_on_right, corn_on_right, game_win)
    if user_input.lower() == "pick up":
       # pick_up_item(fox_in_boat, chicken_in_boat, corn_in_boat, boat_full, user_input)
        # Call the function and update the variables
        fox_in_boat, chicken_in_boat, corn_in_boat, boat_full = pick_up_item(fox_in_boat, chicken_in_boat, corn_in_boat, boat_full, user_input)
        print("fox_in_boat:", fox_in_boat)
        print("chicken_in_boat:", chicken_in_boat)
        print("corn_in_boat:", corn_in_boat)
        print("boat_full:", boat_full)
    elif user_input.lower() == "left":
        #boat_move(left, right)
        left, right = boat_move(left, right)
    elif user_input.lower() == "right":
        #boat_move(left, right)
        left, right = boat_move(left, right)
    elif user_input.lower() == "place":
        #place_item(fox_in_boat, chicken_in_boat, corn_in_boat, fox_on_right, chicken_on_right, corn_on_right)
        fox_in_boat, chicken_in_boat, corn_in_boat, fox_on_right, chicken_on_right, corn_on_right, boat_full = place_item(fox_in_boat, chicken_in_boat, corn_in_boat, fox_on_right, chicken_on_right, corn_on_right, boat_full)
    elif user_input.lower() == "exit":
        break
    