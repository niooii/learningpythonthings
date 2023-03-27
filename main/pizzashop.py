def calcPrice(aList, priceDict):
    priceMap = priceDict
    cost = 13
    for item in aList:
        if priceMap.__contains__(item):
            cost += priceMap.get(item)
    return cost


def getOrder(prompt, promptAgain, type, emptyAllowed, allowMultiple):
    global totalCost
    totalCost = 0
    cont = True
    while cont:
        x = input(prompt)
        if not emptyAllowed and len(x) == 0:
            print("must input an option!")
        else:
            aList = x.split(", ")
            if type == "pizza":
                totalCost += calcPrice(aList, dict(pepperoni=1, mushroom=0.5, olive=0.5, anchovy=2, ham=1.5))
            elif type == "drink":
                totalCost += calcPrice(aList, dict(small=2, medium=3, large=3.5, tub=3.75))
            elif type == "wing":
                totalCost += calcPrice(aList, dict([("10", 5), ("20", 9), ("40", 17.5), ("100", 48)]))
            if not allowMultiple:
                return
            if input(promptAgain) != 'y':
                cont = False
    return


global totalCost
print("Toppings: pepperoni, mushroom, olive, anchovy, ham")
getOrder("enter toppings separated by a comma and a space (enter if none): ", "order another pizza? (y)", "pizza", True,
         True)
print("Drink sizes: small, medium, big, tub")
getOrder("enter drink sizes: ", "", "drink", False, False)
print("Wing sizes: 10, 20, 40, 100")
getOrder("enter wing sizes: ", "", "wing", False, False)
coupon = (100 - int(input("enter a coupon by the percentage off (eg. 10 = 10% off): "))) / 100
print("Your total cost: " + str(round((totalCost * 1.0625) * coupon, 2)))
