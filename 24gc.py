# 24gc.py

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'

GC = 0.0
for i in range(len(dna)):
	if dna[i] == 'G' or dna[i] == 'C': GC = GC +1
	
a = GC / len(dna)
print(f'{a:.2f}')

"""
python3 24gc.py
0.42
add together all occurrances of G and C then divide that by the length
"""
