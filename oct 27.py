import random

def printHello():
    print("Hello")
    print("Bonjour")

printHello()

#print("This is not part of the function")

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


#print("Hello!")

num = 5
#print(num)

#sprint("Hi -$num")

res = getDi(20)

#print("hi")

# string: ""
# int (integer)
# float (floating point number - decimal)

size = 5
pi = 3.14
animal = "dog"
strNum = "1"

#print(strNum)
'''
name = input("Type your name ")
print(name)

num1 = int("5")

num = int(input("Enter a number "))

#print(5+4)

answer = 6+3
#print(answer)

length = 2
width = 7
area = length * width
#print(area)

cost = 2.99
taxRate = 0.065

total = (cost*taxRate) + cost

totalTax = cost*taxRate
total = cost + totalTax

print(total)
'''


print("Rachael" * 3)



















