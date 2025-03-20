"""
How To Make Toast
Ashby Scattini / 20146307
File:
CopyRight 20205, Ashby Scattini 2025

"""
import sys
#This program will ask the user how many slices of bread they would like to toast, how toasted they would like the bread, and what topping they would like on the toast.
#The program will then return the order to the user.
bread_amount = int(input("How many slices of bread would you like to toast:> "))
toaster_level = int(input("How toasted would you like you toast (1-5):> "))
topping = input("What topping would you like:> ")

def toast_order(bread_amount, toaster_level, topping):
    result = ""
    make_toast = True
    if toaster_level <= 0:
        sandwich = input("So you want a sandwich?(Y/N):> ")
        if sandwich.upper() == "N":
            return
        
        if sandwich.upper() == "Y":
            print("Well this is a toast place, not a sandwich place.")
            make_toast = False
            if make_toast == False:
                sys.exit()
            return
    if toaster_level > 5:
        print("Toaster level does not go that high.")
        return
    if toaster_level == 1: 
        print("Your toast will be finished cooking shortly...")
        return
    if toaster_level == 2:
        print("Your toast will be finished cooking in a bit...")
        return
    if toaster_level == 5:
        print("Your toast will be finished cooking soon...")
        return

toast_order(bread_amount, toaster_level, topping)
print("Your toast is perfectly cooked and ready to eat.")
print("You have ordered", bread_amount, "slices of toast at level", toaster_level, "with", topping, "on top.")
print("Enjoy your meal!")
#if toaster_level > 5:
    #print("Toaster level does not go that high.")
    