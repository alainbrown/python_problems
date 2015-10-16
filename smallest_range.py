# You have k lists of sorted integers. Find the smallest 
# range that includes at least one number from each of the k lists. 

# For example, 
# List 1: [4, 10, 15, 24, 26] 
# List 2: [0, 9, 12, 20] 
# List 3: [5, 18, 22, 30] 

# The smallest range here would be [20, 24] as it contains 24 
# from list 1, 20 from list 2, and 22 from list 3.

import heapq

#O(n*klogk) time and O(k) space for k lists of length n
def smallest_range(arr):
	current = []
	range_max = 0
	for i in xrange(len(arr)): 
		heapq.heappush(current,(arr[i][0],i,0))
		range_max = max(arr[i][0], range_max)
	answer = [current[0][0], range_max]
	while True:
		val,lis,ind = current[0]
		if (range_max-val) < (answer[1]-answer[0]):	answer = [val, range_max]
		if ind+1 < len(arr[lis]):
			heapq.heappushpop(current, (arr[lis][ind+1],lis,ind+1))
			range_max = max(range_max, arr[lis][ind+1])
		else: break
	return answer

print smallest_range([
	[4,10,15,24,26],
	[0,9,12,20],
	[5,18,22,30]
	]) == [20,24]
