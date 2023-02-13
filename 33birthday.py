# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list
import sys
import math
import random

days = int(sys.argv[1])
people = int(sys.argv[2])
precision = 1000
shared = 0
for j in range(precision):
	bdays = []
	for i in range(people):
		d = random.randint(1, days)
		if d in bdays:
			shared += 1
			break
		bdays.append(d)
print(shared/precision)
	
#but what is the output supposed to be? 
# how do i get the probability of the likiehood of same birthdays based on
#whether or not the list contains two of the same birthdays
"""
create a list of length (people + 1)
then make this days-list
1 - (product of list/days)
"""

"""
python3 33birthday.py 365 23
0.571

ideas:
take the system args and make a list of zeros the length of first arguments
then take the second arg and tell computer to randomly go through the list of
zeros and add one to the value 

probability ?


then check 
"""

