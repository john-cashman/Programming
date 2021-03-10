#This program generates 10 random numbers between 0 and 100
#It then prints out the 10 numbers and also prints out the top three
#Author: John Cashman


import random #This imports a random set of numbers
#creates the variables needed for the program
howMany = 10
topHowMany = 3 
rangeFrom = 0
rangeTo = 100

numbers = []

for i in range(0,10):
    numbers.append(random.randint(rangeFrom,rangeTo))
print (" {} random numbers\t {}".format(howMany,numbers))

topOnes = numbers.copy()
topOnes.sort(reverse = True)
print ("The top {} are \t\t {}".format(topHowMany,topOnes[0:topHowMany]))