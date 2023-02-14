# 32xcoverage.py

# Write a program that simulates a shotgun resequencing project
# How uniformly do the reads "pile up" on a chromosome?
# How much of that depends on sequencing depth?

# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line

# Hint: make the problem smaller, so it's easier to visualize and debug
# Hint: if you don't understand the context of the problem, ask for help
# Hint: if you are undersampling the ends, do something about it

# Note: you will not get exactly the same results as the command line below
import sys
import math
import random

# turn the argument characters into integers
refL = int(sys.argv[1]) #reference length
readN = int(sys.argv[2]) #number of reads
readL = int(sys.argv[3]) #read length

ref = [0] * refL 

for read in range(0,readN):
	r = random.randint(0,refL-readL)
	for eachRead in range(0, readL):
		ref[r+eachRead] += 1

refNoEnds = ref[readL:-readL]
maxC = 0
for val in range(len(refNoEnds)):
	if ref[val] > maxC:
		maxC = ref[val]
#print(maxC)

minC = ref[0]
for val in range(len(refNoEnds)):
	if ref[val] < minC:
		minC = ref[val]
#print(minC)

aveC = 0

for val in range(len(refNoEnds)):
	aveC += refNoEnds[val]
aveC = aveC/len(refNoEnds)
#print(refNoEnds)
print(minC, ' ', maxC, ' ', aveC)
print(refNoEnds)
"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375

first is reference length
second is number of reads
third is read length


could: make a container with 0s as long as first number
then I could do a for loop and use the rwandom generator to make a number
within the range of the ref length, and as many times as the read # is
for each of those I change the reference string at that location + the 
read length-1 to have 1 added onto the values

then i am left with a container with 1's and maybe even 2's or 3's etc.
then i find the lowest number and the highest number

what is below is not the actual min coverage
report out the first time the value =/= 0 (location) and the last time
then I sum up all of the values and divide by the length of the ref
"""
