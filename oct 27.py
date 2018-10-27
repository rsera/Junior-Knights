import random

def printHello():
    print("Hello")
    print("Bonjour")

#print("This is not part of the function")

#printHello()

def returnFive():
    print("I am returning five!")
    return 5

def returnFiveAlso():
    num = 5
    return num

def getName():
    return "Rachael"

def getNum(num):
    return num

result = getNum(5)
# result = 5
#print(result)

def fn(x):
    return 2 * x + 5

ans = fn(2)
#print(ans)

def getArea(length, width):
    area = length * width
    return area

area = getArea(7, 3)
#print(area)

#random.randint(1,6)

def get6Di():
    return random.randint(1,6)

dieResult = get6Di()
#print(dieResult)

def getDi(maxNum):
    return random.randint(1, maxNum)


res = getDi(20)













