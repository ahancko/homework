# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys
import sys

values = []
for val in sys.argv[1:]:
	values.append(float(val))

values.sort()
print(values)
length = len(values)
print('Count: ', length)
print('Minimum: ', values[0])
print('Maximum: ', values[-1])
mean = sum(values)/len(values)
print('Mean: ', mean)
median = len(values)/2
#print('Std. dev: ', 
# for dstd dev make a vector with the mean
meanV = values[:]
for i in range(len(values)):
	meanV[i] -= mean
	meanV[i] = meanV[i] ** 2
STdev = (sum(meanV)/length) ** 0.5
#print(meanV)
print('Std. dev: ',  STdev)
mid = length // 2
if length % 2 == 0: 
	print('Median: ', (values[mid] + values[mid-1]) /2)
else: 
	print('Median: ', values[mid])

"""
minimum = min(sys.argv[1:])
maximum = max(sys.argv[1:])

print('Count: ', len(sys.argv[1:]))
print('Minimum: ', float(minimum))
print('Maximum:', float(maximum))
"""
"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
