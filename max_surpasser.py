# The "surpasser" of an element in an array is defined as 
# the number of elements that are to the "right" and bigger than itself. 

# Example: 
# Array: 
# [2, 7, 5, 5, 2, 7, 0, 8, 1] 
# The "surpassers" are 
# [5, 1, 2, 2, 2, 1, 2, 0, 0] 

# Question: Find the maximum surpasser of the array. 
# In this example, maximum surpasser = 5
import heapq

#O(n^2)
def naive_max_surpasser(n):
	surs = [0] * len(n)
	for i in xrange(len(n)):
		for j in xrange(i+1,len(n)): 
			if n[i] < n[j]: surs[i] += 1
	max_s = 0
	for x in xrange(len(n)): max_s = max(max_s,surs[x])
	return max_s

print naive_max_surpasser([2, 7, 5, 5, 2, 7, 0, 8, 1]) == 5
