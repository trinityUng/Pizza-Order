#function created to print out the receipt
def generateReceipt(pizzaOrder):
    toppingTotal = 0
    pizzaCost = 0
    counter = 0
    finalPrice = 0


    #if the user did not order anything the program will print out that they did not order anything
    if len(pizzaOrder) == 0:
        print("You did not order anything")
    #if the user did order something the program will print out the order
    else:
        print("Your order:")
        #for loop created so that it can go through the list to print out the order
        for i in range(len(pizzaOrder)):
            #the program finds what the size of the pizza is and prints it out by checking the index
            pizza = pizzaOrder[i][0]
            if pizza == "S":
                print("Pizza", i + 1, ":", pizza, "\t\t", "7.99")
            elif pizza == "M":
                print("Pizza", i + 1, ":", pizza, "\t\t", "9.99")
            elif pizza == "L":
                print("Pizza", i + 1, ":", pizza, "\t\t", "11.99")
            elif pizza == "XL":
                print("Pizza", i + 1, ":", pizza, "\t\t", "13.99")
            #this prints out the list of all the toppings in the order
            print("- ", end = "")
            print(*pizzaOrder[i][1], sep = "\n- ")

            #counter created so that the program knows how many toppings are on a pizza
            counter = len(pizzaOrder[i][1])
            #if the toppins are more than 3 toppings addtional fees will be added also based on the size of the pizza
            if pizza == "S":
                if counter <= 3:
                    toppingTotal = 0
                    pizzaCost = 7.99
                elif counter > 3:
                    toppingTotal = (counter - 3) * 0.50
                    pizzaCost = 7.99
                    for i in range(counter - 3):
                        print("Extra Topping (S) \t 0.50")
            elif pizza == "M":
                if counter <= 3:
                    toppingTotal = 0
                    pizzaCost = 9.99
                elif counter > 3:
                    toppingTotal = (counter - 3) * 0.75
                    pizzaCost = 9.99
                    for i in range(counter - 3):
                        print("Extra Topping (M) \t 0.75")
            elif pizza == "L":
                if counter <= 3:
                    toppingTotal = 0
                    pizzaCost = 11.99
                elif counter > 3:
                    toppingTotal = (counter - 3) * 1
                    pizzaCost = 11.99
                    for i in range(counter - 3):
                        print("Extra Topping (L) \t 1.00")
            elif pizza == "XL":
                if counter <= 3:
                    toppingTotal = 0
                    pizzaCost = 13.99
                elif counter > 3:
                    toppingTotal = (counter - 3) * 1.25
                    pizzaCost = 13.99
                    for i in range(counter - 3):
                        print("Extra Topping (XL) \t 1.25")

            #calculates the pirce of the whole order
            finalPrice = (pizzaCost + toppingTotal) + finalPrice

            tax = finalPrice * 0.13
            totalPrice = finalPrice + tax

        #prints the tax
        roundTax = "%.2f" % round(tax, 2)
        #prints the final total with tax
        roundPrice = "%.2f" % round(totalPrice, 2)
        print("Tax: \t\t\t\t",roundTax)
        print("Total: \t\t\t\t", roundPrice)
