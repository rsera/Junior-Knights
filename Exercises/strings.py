#goo.gl/44s4dN

# 1 print specified character
'''
word = input("Enter a word: ")
print(word[-1])
if len(word) > 3:
    print(word[2])
'''

# 2 substring
'''
word = input("Enter a word: ")
substring = input("Enter a substring: ")

if substring in word:
    print(substring, "is in", word)
else:
    print(substring, "is not in", word)
'''

# 3 consecutive letters
'''
word = input("Enter a word: ")
prev = ''
flag = False

for ch in word:
    if ch == prev:
        flag = True
    prev = ch

if flag:
    print(word, "has consecutive repeated letters.")
else:
    print(word, "doesn't have consecutive repeated letters.")
'''   

# 4 similar strings
'''
s1 = input("Enter the 1st string: ")
s2 = input("Enter the 2nd string: ")

i = 0
l1 = len(s1)
l2 = len(s2)
same = 0

if l1 != l2:
    print(0)
else:
    while i < l1:
        if s1[i] == s2[i]:
            same +=1
        i +=1
    print(same)
'''

# 4a similar strings with different lengths
'''
s1 = input("Enter the 1st string: ")
s2 = input("Enter the 2nd string: ")

i = 0
l1 = len(s1)
l2 = len(s2)
same = 0

if l1>l2:
    l1=l2

while i < l1:
    if s1[i] == s2[i]:
        same +=1
    i +=1
print(same)
'''

#5 palindrome checker
'''
s = input("Enter the word to check: ")
length = len(s)
isPal = True
i = 0
j = length - 1

while i < length:
    if s[i] != s[j]:
        isPal = False
        break
    i += 1
    j -= 1

if isPal:
    print("It is a palindrome")
else:
    print("It is NOT a palindrome")
'''

#6 letter frequency
'''
word = input("Enter a word: ")
letter = input("Enter a letter: ")
count = 0

for ch in word:
    if ch == letter:
        count += 1

print(letter, "occurs", count, "time(s) in", word)
'''

#7a print list of colors
'''
colors = ["purple", "black", "aqua", "teal", "seafoam"]
print(colors)
'''

#7b print list of colors on new lines
'''
colors = ["purple", "black", "aqua", "teal", "seafoam"]
for color in colors:
    print (color)
'''

#7c contains color
'''
colors = ["purple", "black", "aqua", "teal", "seafoam"]
color = input("What color do you want to find? ")

if color in colors:
    print(color, "is in the list")
else:
    print(color, "is not in the list")
'''

#7d contains color # of times
'''
colors = ["purple", "black", "aqua", "teal", "seafoam"]
userColor = input("What color do you want to find? ")
count = 0

for color in colors:
    if color == userColor:
        count +=1

print(userColor, ": ", count, sep="")
'''

#7e 3rd color or 2nd to last color?
'''
colors = ["purple", "black", "aqua", "teal", "seafoam"]
userColor = input("What color do you want to find? ")

if colors[2] == userColor:
    print(userColor, "is the 3rd item in the list.")
if colors[-2] == userColor:
    print(userColor, "is the 2nd to last item in the list.")
'''

#8 sort students
'''
numStudents = int(input("How many students are in your class? "))
i = 0
students = []

while i < numStudents:
    name = input("Enter a student's name: ")
    students.append(name)
    i += 1

students.sort()

for student in students:
    print(student)
'''

#8 alphabetic words
'''
i = 0
words = []
while i < 10:
    word = input("Enter a word: ")
    words.append(word)
    i += 1
words.sort()
print(words[0])
'''

#9 magic 8 ball
'''
import random

numResponses = 6

responses = ["It is certain.",
 "Is it decidedly so.",
 "Outlook good.",
 "Reply hazy, try again.",
 "Very doubtful",
 "Don't count on it"]

question = input("Enter your question: ")

index = random.randint(0, numResponses-1)
print(responses[index])
'''

#10 movie cast
'''
movie = "Wonder Woman"
cast = ["Gal Gadot",
        "Chris Pine",
        "Robin Wright",
        "Connie Nielson",
        "David Thewlis"]
actor = input("Enter an actor: ")

if actor in cast:
    print("Yes,", actor, "is in", movie)
else:
    print("No,", actor, "is not in", movie)
'''

#11 only vowels
'''
string = input("Enter a word: ")
vowels = ['a', 'e', 'i', 'o', 'u']
flag = True

for ch in string:
    if ch not in vowels:
        flag = False

if flag:
    print(string, "is all vowels")
else:
    print(string, "has consonants")
'''  

#12 alternating vowels and consonants
'''
string = input("Enter a word: ")
vowels = ['a', 'e', 'i', 'o', 'u']
i = 0
length = len(string)
flag = True

while i < length:
    if i%2 == 0:
        if string[i] in vowels:
            flag = False
    else:
        if string[i] not in vowels:
            flag = False
    i += 1

print(flag)
'''

#13 duplicates in list
'''
numbers = [1, 3, 6, 4, 2]
freq = []
dupes = False

for i in range(11):
    freq.append(0)

for num in numbers:
    freq[num] += 1

for i in freq:
    if i>1:
        dupes = True

if dupes:
    print(numbers, "has duplicates.")
else:
    print(numbers, "doesn't have duplicates.")
'''
    


