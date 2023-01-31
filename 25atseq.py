# 25atseq.py

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# Note: set random.seed() if you want repeatable random numbers

length = 30 #want a 30 base long strand
AT = 0 #will count the number of AT but we start with 0
s = '' #will save each base to the s string
import random
for i in range(length):
	r = random.choice('AAATTTCCGG') #giving a choice to pull from something that is 60% AT already
	if r == 'A' or r == 'T': 
		AT = AT + 1
		s = s + r
print(length, AT/length, s)

"""
need to figure out how to do random choice and random seed and then also 
not print the r but save it to print at once

for i in range(length):
	r = random.randint(1,4)
	for i in range(length-10):
		if r == 1:
			print('A', end= '')
			AT = AT +1
		elif r == 2: 				
			print('T', end ='')
			AT = AT + 1
		elif r == 3: print('C', end='')
		else: print('G', end ='')
print()
print(AT/length)
"""
"""
How to get the random to be mostly AT? Do i make a 60 AT string and pull
random letters from there? 
could i use random.choice and give it AAATTTCCGG (60%)
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC

could start with 15 then find the average AT and if it is too high then add CG 
and if too low add AT
if 
"""
