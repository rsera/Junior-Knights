# Junior Knights Day 2 - if statement examples

# you always have a Boolean condition in your if statement
# if the condition evaluates to true, you will execute any code that follows it that is indented in one level
# any following lines that are not indented with the if statement are executed regardless of if the condition is true or not
if 5 < 10:
    print("This will print if the condidition is true (and it is in this case, so this prints)")
print("This will always print")

if 5 > 10:
    print("This will print if the condition is true (in this case, it's not)")
print("This will print regardless.")

# we also have Boolean values in python: True and False
if True:
    print("Since True is always true, this will always print")
if False:
    print("Since False is always false, it doesn't print")

# often, you'll evaluate variables in print statements
num = 5
if num < 10:
    print("The condition is true, so this prints")
    print("You can print multiple lines as long as they're all indented at the same level")
    print("You can also write other statements like variable assignment")
    x = 57
    print("Let's print x:", x)

if num > 10:
    print("The condition is not true, so this doesn't print")

# this can also be a variable that's set from user input:
num = int(input("Enter a number "))
if num < 10:
    # the message below will only print if you entered a number less than 10
    print("The number you entered is less than 10")

# now let's look at if and else
# if and else are mutually exclusive--exactly one of them will execute
num2 = int(input("Enter another number [1-50] "))
if num2 < 25:
    print("The number is less than 25")
else:
    print("The number is greater than or equal to 25")
# see how only one of those options can be true? since we have 2 mutually exclusive options, "if" and "else" are a good choice here

# now let's look at if and elif
# elif is like "else" but with another condition to check (instead of just catching everything that is not the "if" condition
num3 = int(input("Enter yet another number [1-100] "))

if num3 < 33:
    print("The number is less than 33")
elif num3 < 67:
    print("The number is between 33 and 66")
else:
    print("The number is greater than or equal to 67")

# now let's look at "and"
# when you have "and" in your if statement, BOTH conditions must be true for the statement to evaluate to true
num4 = int(input("Enter another number again! ")

if num3 < 50 and num4 > 50:
    print("Num 3 is less than 50 and num4 is greater than 50")
else
    print("Num3 is >= 50 or num4 is <= 50; at least 1 of the conditions was false")

# when you have "or", if EITHER condition is true, the statement evaluates to true
if num3 < 50 or num4 > 50:
    print("Num3 is < 50 or num4 is > 50")
else
    print("neither condition was true")

    
