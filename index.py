# Assignment 4B
# Redo the programs on assignment2 but now with functions that return multiple values 
# (move all user inputs in one function)

apple_Price = 20
orange_Price = 25

apple_Amount = 0
orange_Amount = 0

def getInputs():
    global apples_quantity
    global orange_quantity

    apples_quantity = int(input("How many apples you want to buy: "))
    orange_quantity = int(input("How many oranges you want to buy: "))

    return apples_quantity, orange_quantity

def solve(aq, oq): #aq = apple quantity, oq = orange quantity
    if apples_quantity < 0 or orange_quantity < 0:
        print("Quantity cannot be less than zero")
    else :
        apple_Amount = apples_quantity * apple_Price
        orange_Amount = orange_quantity * orange_Price
        print("The total amount is: " + str(apple_Amount + orange_Amount))

AQ, OQ = getInputs()
solve(AQ, OQ)