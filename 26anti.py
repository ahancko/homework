# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax

dna = 'ACTGAAAAAAAAAAA'

s = '' #creates an empty string
for i in range(len(dna)): #all of this stores the compl. base to each given base
	if dna[i] == 'A': 
		s = s + 'T'
	elif dna[i] == 'T': 
		s = s + 'A'
	elif dna[i] == 'C': 
		s = s + 'G'
	else: s = s +'C'
	
print(s[::-1]) #prints the string but backwards

"""
python3 26anti.py
TTTTTTTTTTTCAGT

ideas:
make an empty string and if A then store T, etc.

"""
