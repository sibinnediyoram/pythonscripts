import datetime
print "this is work for character input excercises"
now = datetime.datetime.now()
year = now.year
a = raw_input("enter your name: ")
b = int(raw_input("enter your age: "))
c = (100 - b) + year
print a + "you will turn hundred on: " + str(c)


