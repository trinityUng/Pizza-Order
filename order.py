##
#author: Trinity Ung
#date: October 25th, 2022
#This program gets the users input for their pizza order and prints out the receipt

#this conncets the two files together
from pizzaReceipt import *

#this function gets the users input for the size of their pizza
def pizzaSize():
    userSize = False
    size = input("\nChoose a size: S, M, L, or XL: ")
    upperSize = size.upper()
    #while loop created and stops until the user inputs the correct information
    while userSize == False:
        if (upperSize == "S" or upperSize == "M" or upperSize == "L" or upperSize == "XL"):
            userSize = True
        else:
            size = input("Choose a size: S, M, L, or XL: ")
            upperSize = size.upper()
            userSize = False
    #returns the size of the users pizza
    return upperSize


#function created to store the pizza toppings
#b is the tuple of all the toppings available so that the function will know what toppings the user can get
def pizzaToppings(b):
    userTopping = False
    toppingList = []
    topping = input("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter \"LIST\". When you are done adding toppings, enter \"X\"\n" )
    finalTopping = topping.upper()
    #while loop created so that the user keeps inputing the amount of toppings they want
    while userTopping == False:
        finalTopping = topping.upper()
        #if the user inputs X then the function will stop as the user is done inputing their toppings
        if finalTopping == "X":
            userTopping = True
        #if the user inputs LIST the program will print out the topping list
        elif finalTopping == "LIST":
            print(b)
            topping = input("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter \"LIST\". When you are done adding toppings, enter \"X\"\n" )
            userTopping = False
        #if the user inputs the correct toppping it will be added to a list and will print the topping so that the user knows it's been added to their pizza
        elif finalTopping in b:
            print("Added", finalTopping, "to your pizza")
            toppingList.append(finalTopping)
            topping = input("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter \"LIST\". When you are done adding toppings, enter \"X\"\n" )
            finalTopping = topping.upper()
            userTopping == False
        #if the user inputs an incorrect topping the program will let them know it is not valid
        else:
            print("Invalid topping")
            topping = input("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter \"LIST\". When you are done adding toppings, enter \"X\"\n" )
            finalTopping = topping.upper()
            userTopping == False
    #returns the list of the toppings on the pizza
    return toppingList



def main():
    #tuple of the toppings that the user can get on their pizza
    TOPPINGS = ("ONION", "TOMATO", "GREEN PEPPER", "MUSHROOM", "OLIVE", "SPINACH", "BROCCOLI", "PINEAPPLE", "HOT PEPPER", "PEPPERONI", "HAM", "BACON", "GROUND BEEF", "CHICKEN", "SAUSAGE")
    costumerOrder = []
    pizzaOrderList = []
    order = input("Do you want to order a pizza? ")
    keepGoing = True
    orderLower = order.lower()
    #if the user doesn't want to order a pizza then the program will call generateReceipt from the other file
    if orderLower ==  "q" or orderLower == "no":
        #converts the list to tuple
        costumerOrderTuple = tuple(costumerOrder)
        generateReceipt(costumerOrderTuple)
    #if the user does want to order a pizza the other functions will be called to get the users size of pizza and toppings
    else:
        finalSize = pizzaSize()
        costumerOrder.append(finalSize)
        finalPizzaTopping = pizzaToppings(TOPPINGS)
        costumerOrder.append(finalPizzaTopping)
        #converts the list to a tuple
        costumerOrderTuple = tuple(costumerOrder)
        pizzaOrderList.append(costumerOrderTuple)
        #while loop created so that multiple pizza can get ordered
        while keepGoing == True:
            keepOrdering = input("Do you want to continue ordering? ")
            keepOrderingLower = keepOrdering.lower()
            #if the user doesn't want to order anymore pizzas it will send the order to generateReceipt
            if keepOrderingLower ==  "q" or keepOrderingLower == "no":
                keepGoing = False
            #if the user wants to continue ordering then the process will restart of getting the size and topping on the pizza
            else:
                #list is reinitialized so that the information from the previous pizza order does not get mixed up with the new order
                costumerOrder = []
                finalSize = pizzaSize()
                costumerOrder.append(finalSize)
                finalPizzaTopping = pizzaToppings(TOPPINGS)
                costumerOrder.append(finalPizzaTopping)
                #converts the list to a tuple
                costumerOrderTuple = tuple(costumerOrder)
                pizzaOrderList.append(costumerOrderTuple)

        #once the user is done ordering, generateRecipt is called to create the recipt
        generateReceipt(pizzaOrderList)

#calls the main function so that the program will run everything
main()
