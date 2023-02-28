# 50dust.py

# Write a better version of your 42dust.py program
# Your program must have the following properties

# 1. y the entropy of each window is centered (N's in the middle of windows, entire window) 
# 2. y  has option and default value for window size 
# 3. y  has option and default value for entropy threshold
# 4. partially done has a switch for N-based or lowercase (soft) masking
# 5. y but exports as uppercase works with uppercase or lowercase input files
# 6. idk what this means works as an executable

# Optional: make the algorithm faster (see 29gcwin.py for inspiration)
# Optional: benchmark your programs with different window sizes using time

# Hint: make a smaller file for testing (e.g. e.coli.fna in the CLI below)
import mcb185
import math
import sys
import argparse

parser = argparse.ArgumentParser(description='Entropy calculator for sequence')
parser.add_argument('-s', type=str, metavar = '<string>', help = 'some file')
parser.add_argument('-w', required=False, type = int, default = 11,
	metavar = '<int>', help = 'optional window size argument [%(default)i]')
parser.add_argument('-t', required = False, type = float, default = 1.4,
	metavar = '<float>', help = 'optional entropy argument [%(default)i]')
parser.add_argument('-hard', action='store_true', help='on/off switch')
parser.add_argument('-soft', action='store_true', help='on/off swtich')
arg = parser.parse_args()


print(arg.s)
print(arg.w, arg.t, arg.hard)
if arg.hard: print('switch on')
else: print('swtich off')

wsize = int(arg.w)
ethresh = float(arg.t)

def seqentropy(seq):
	seq = seq.upper()
	seql = list(seq)
	A = seq.count('A')/len(seq)
	C = seq.count('C')/len(seq)
	T = seq.count('T')/len(seq)
	G = seq.count('G')/len(seq)
	vals = [A, C, T, G]
	assert(math.isclose(1.0, sum(vals)))
	h = 0
	for p in vals:
		if p != 0: h -= p * math.log2(p)
	return h
	

for name, seq in mcb185.read_fasta(arg.s):
	seql = list(seq.upper())
	for i in range(len(seq) - wsize +1):
		if seqentropy(seq[i:i+wsize]) < ethresh: 
			for b in range(wsize):
				if arg.hard:
					seql[i+b] = 'N'
				else:
					seql[i+b] = seq[i+b].lower()
	seqa = ''.join(seql)
	#if arg.hard: print("Switch is on Arielle!")
	#else: print("Switch is not on Arielle")
	print(seqa)

#print(seqentropy(arg.s), arg.s)

"""
mask the whole window with "N's instead of just a single base
python3 50dust.py -w 11 -t 1.4 -s e.coli.fna  | head
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGCTTTTcATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTaaaaaaaGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAattaaaattttATTGACTTAGG
TCACTAAATacTTTAACCAATATAGGCATAGCGCACAGACAGAtAaaaaTTACAGAGTAC
ACAacATCCATGAAACGCATTAGCACCACCATTACCAccaccatCACCATTACCACAGGT
AACGGTGCgGGCTGACGCGTACAGGAAACacagaaaaAAGCCCGCACCTGACAGTGCGGG
CTttttttTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
AGGCAGggGCaGGTGGCCACCGTCcTCtctgcccCcgcCAAAatcaccaacCACCTGGTG
GCGATGATTGaAAAAacCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA

Timings
win alg1 alg2
11  28.7 25.8
25  30.4 26.1
100 33.2 26.1
200 37.4 25.9
"""
