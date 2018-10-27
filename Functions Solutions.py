import random

def printHello():
    print("Hello")
    print("Guten tag")

def getBday():
    return "Jan 1"

def printNames(num):
    print("Rachael" * num)

def getPi():
    return 3.14

def sumNums(a, b):
    return a + b

def calcCircumference(radius):
    return 2 * getPi() * radius

def power(a, b):
    return a**b

def getArea(radius):
    return getPi() * power(radius, 2)

def printRandom(end):
    print(random.randint(1,end))

def printDiceRolls():
    print("The first die rolls:", random.randint(1, 6))
    print("The second die rolls:", random.randint(1,6))

def movieCost(adult, child):
    return adult*15+child*10

def getGallons(mpg, miles):
    return miles/mpg

def getDollarsLeft(dollars, exRate, spent):
    foreignMoney = dollars * exRate
    leftover = foreignMoney - spent
    return leftover
        
dollarsLeft = getDollarsLeft(100, .88, 50)
print(dollarsLeft)




