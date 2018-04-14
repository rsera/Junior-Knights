import random

def randNoun(which):
    if which == 1:
        return "car"
    elif which == 2:
        return "park"
    elif which == 3:
        return "potato"
    else:
        return "movie theater"
def randVerb(which):
    if which == 1:
        return "drove"
    elif which == 2:
        return "threw"
    elif which == 3:
        return "mashed"
    else:
        return "watched"

'''print("I went to the " + randNoun(random.randint(1,4)) + " and then I "
      + randVerb(random.randint(1,4)) + " a " + randNoun(random.randint(1,5))
      + " to the " + randNoun(random.randint(1,4)))'''

def printChars1(string):
    length = len(string)
    for i in range(length):
        print(string[i])

def printChars2(string):
    for char in string:
        print(char)

def printItems1(listy):
    for i in range(len(listy)):
        print(listy[i])

def printItems2(listy):
    for item in listy:
        print(item)

def calcDamage(health, damage):
    if (health-damage <= 0):
        return "x_x"
    else:
        return ">_<"

def multNums(a,b):
    ans = 0
    while a>0:
        ans += b
        a-=1
    return ans

def isFactor(a, b):
    if (a % b == 0):
        return True
    else:
        return False

def strLen(str):
    count = 0
    for ch in str:
        count += 1
    return count

def sumList(listy):
    sum = 0
    for i in range(len(listy)):
        sum += listy[i]
    return sum

def makeFreq(length):
    listy = []
    for i in range(length):
        listy.append(0)
    return listy

def mostFreq(listy):
    maxTimes = 0
    maxVal = 0
    freqList = makeFreq(10)
    
    for i in range(len(listy)):
        freqList[listy[i]] += 1

    for i in range(len(freqList)):
        if freqList[i] > maxTimes:
            maxTimes = freqList[i]
            maxVal = i
    return maxVal

def stringRep(string):
    new = ""
    for i in range(len(string)):
        new+=string[0:i+1]
    return new
        
def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)




