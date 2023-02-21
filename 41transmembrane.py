# 41transmembrane.py

# Write a program that predicts which proteins in a proteome are transmembrane

# Transmembrane proteins are characterized by having
#    1. a hydrophobic signal peptide near the N-terminus
#    2. other hydrophobic regions to cross the plasma membrane

# Both the signal peptide and the transmembrane domains are alpha-helices
# Therefore, they do not contain Proline

# Hydrophobicity can be measured by Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot

# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

# Hint: copy mcb185.py to your homework repo and import that
# Hint: create a function for KD calculation
# Hint: create a function for hydrophobic alpha-helix
# Hint: use the same function for both signal peptide and transmembrane
import sys
import gzip
import mcb185

aas = 'ACDEFGHIKLMNPQRSTVWY' #all amino acid protein name shortcuts
KDa = 1.8, 2.5, -3.5, -3.5, 2.8, -0.4, -3.2, 4.5, -3.9, 3.8, 1.9, -3.5, -1.6, -3.5, -4.5, -0.8, -0.7, 4.2, -0.9, -1.3

def kd(seq):
	score = 0
	for aa in range(len(seq)):
		score += KDa[aas.find(seq[aa])]
	return score/len(seq)
	
	
def hah(seq, w, t):
	for i in range(len(seq) - w +1):
		win = seq[i:i+w]
		akd = kd(win)
		if akd >= t and 'P' not in win: return True
		else: return False
		
		
for name, seq in mcb185.read_fasta(sys.argv[1]):
	words = name.split()
	vid = words[0]
	nterm = seq[0:30]
	cterm = seq[30:]
	if hah(nterm, 8, 2.0) and hah(cterm, 11, 2.5): print(name)
	
"""
filename = sys.argv[1]

pName = [] #place to store protein names

sPep = [] #store if signal peptide
aHelix = [] #place to store if a helix or not
hDomain = [] #store other hydrophobic domains

test = 'ACDE'

aas = 'ACDEFGHIKLMNPQRSTVWY' #all amino acid protein name shortcuts
KDa = 1.8, 2.5, -3.5, -3.5, 2.8, -0.4, -3.2, 4.5, -3.9, 3.8, 1.9, -3.5, -1.6, -3.5, -4.5, -0.8, -0.7, 4.2, -0.9, -1.3

#for KDv we want to know the window length, think I need to simplify this
testa = 'ACDP'
def KDv(length, start, stop):
	for defline, seq in mcb185.read_fasta(f'{filename}'):
		words = defline.split()
		name = words[0:]
		for p in range(start,stop+1):
			sumt = 0
			s = seq[start+p:start+length+p]
			sumt += KDa[aas.find(s[p])]
			KDV = sumt/length
			print(seq, s, sumt)
		
print(KDv(8,0,30))
"""
"""
def KDv(seq):
	for defline, seq in mcb185.read_fasta(f'{filename}'):
		words = defline.split()
		name = words[0:]
		sumt = 0
		print(defline)
		for p in range(len(seq)):
			sumt += KDa[aas.find(seq[p])]
		print(sumt/len(seq))
"""
"""

#print(KDv(test))
#for alpha helix def we need to determine if the window has proline, t = alhel
def alhel(seq):
	for defline, seq in mcb185.read_fasta(f'{filename}'):
		words = defline.split()
		name = words[0:]
		prol = False
		for p in range(len(seq)):
			if seq.rfind('P') < 0: prol = True #only true when there is no P
		print(prol)
	
#check if there is a signal pep in the first 30
sigl = 8 #in first 30 KD >2.5
hyrl = 11 #after first 30 KD >2.0

for protein in range(30):
	w = seq[protein:protein+sigl]
	
#print(alhel(8))

"""

"""


#test 8 in first 30 then KD > 2.5 then test if alhel
#then move window 11 30: KD >2 if true then test alhel
"""
"""
for defline, seq in mcb185.read_fasta(f'{filename}'):
	if alhel(11, seq[0:11]) == True: print('yes')
test = 'ABC'
print(1 ==2)
tup = '3', 'four'
print(f"{', '.join(tup)}")
	"""
	

"""
need to determine KD
need to look at window
need to sum up KD then divide by readL
inputs: sequence, readL. do I also do sart and end?
"""



"""
with gzip.open(filename, 'rt') as fp:
	for line in fp.readlines():
		if line.startswith('>'):
			words = line.split()
			id = words[0][1:]
			jd = words[1:][:]
			pName.append(words)
		#print(words)
		#print(pName)
		
		
		

"""
"""
python3 41transmembrane.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
NP_414560.1 Na(+):H(+) antiporter NhaA [Escherichia coli str. K-12 substr. MG1655]
NP_414568.1 lipoprotein signal peptidase [Escherichia coli str. K-12 substr. MG1655]
NP_414582.1 L-carnitine:gamma-butyrobetaine antiporter [Escherichia coli str. K-12 substr. MG1655]
NP_414607.1 DedA family protein YabI [Escherichia coli str. K-12 substr. MG1655]
NP_414609.1 thiamine ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414653.1 protein AmpE [Escherichia coli str. K-12 substr. MG1655]
NP_414666.1 quinoprotein glucose dehydrogenase [Escherichia coli str. K-12 substr. MG1655]
NP_414695.1 iron(III) hydroxamate ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414699.1 PF03458 family protein YadS [Escherichia coli str. K-12 substr. MG1655]
NP_414717.2 CDP-diglyceride synthetase [Escherichia coli str. K-12 substr. MG1655]
...
"""
