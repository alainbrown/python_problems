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

# Complexity: O(n^2)
# Space: O(1)
def naive_max_surpasser(n):
	max_s = 0
	for i in xrange(len(n)):
		surpasser = 0
		for j in xrange(i+1,len(n)): 
			if n[i]<n[j]: surpasser += 1
		max_s = max(max_s,surpasser)
	return max_s

# Complexity: O(n log n)
# Space: O(n)
def max_surpasser(N):
	lis = [(N[i],i) for i in xrange(len(N))]
	lis.sort()
	max_s = 0
	top = len(N)-1
	max_s = 0
	for x in xrange(top): max_s=max(max_s, top-lis[x][1]-x-1)
	return max_s

print naive_max_surpasser([2, 7, 5, 5, 2, 7, 0, 8, 1]) == 5
print max_surpasser([2, 7, 5, 5, 2, 7, 0, 8, 1]) == 5
