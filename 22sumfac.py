# 22sumfac.py

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# Use the same loop for both calculations

# Note: you may not import math or any other library

n=5
a=0
b=1

for i in range(n):
	#print(i+1)
	a = a + i +1
	b = b * (i +1)
	print(a)
print(a)
print(b)

#Questions: do you want the running sum printed (1, 3, 6, 10, 15) or just 15?

"""
python3 22sumfac.py
5 15 120
take n and make it into a list of the numbers before (5 -> 1 2 3 4 5)
could go backwards. 
for i length (n) 
"""
