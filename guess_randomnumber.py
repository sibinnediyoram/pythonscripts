import random

a = random.randint(1, 9)
b = 0
count = 0
while b != a and b != "exit":
    b = raw_input("guess your number: ")
    if b == "exit":
        break
    b = int(b)
    count += 1
    if a < b:
        print "your guess is very high"+str(a)
    elif a > b:
        print "your guess is too low"
    else:
        print "your guess is exactly equal to system"

