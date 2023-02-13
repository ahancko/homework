# 31entropy.py

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# Store the values in a new list

# Note: make sure the command line values contain numbers
# Note: make sure the probabilities sum to 1.0
# Note: import math and use the math.log2()

# Hint: try breaking your program with erroneous input
import math
import sys

values = []

for val in sys.argv[1:]:
	values.append(float(val))
print(values)

assert(math.isclose(sum(values), 1.0))

m1 = []
for v in values:
	m1.append(v*math.log2(v))
print(-1*sum(m1))

	

"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
