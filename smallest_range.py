# You have k lists of sorted integers. Find the smallest 
# range that includes at least one number from each of the k lists. 

# For example, 
# List 1: [4, 10, 15, 24, 26] 
# List 2: [0, 9, 12, 20] 
# List 3: [5, 18, 22, 30] 

# The smallest range here would be [20, 24] as it contains 24 
# from list 1, 20 from list 2, and 22 from list 3.

import sys

#O(n*m) complexity, O(n) space for n lists of length m
def smallest_range(arr):
	current = {}
	min_range = {}
	for i in xrange(len(arr)): 
		current[i] = 0 
		min_range[i] = 0

	old_range = sys.maxint
	while True:
		# find minimum of each list
		small_num = sys.maxint
		small_index = 0
		for i in current:
			if arr[i][current[i]] < small_num:
				small_num = arr[i][current[i]]
				small_index = i

		# calculate new range 
		new_range_min = sys.maxint
		new_range_max = 0
		for i in current: 
			new_range_min = min(new_range_min, arr[i][current[i]]) 
			new_range_max = max(new_range_max, arr[i][current[i]])
		if (new_range_max-new_range_min) < old_range:
			for i in current: min_range[i] = current[i]
			old_range = new_range_max-new_range_min

		# move lowest index
		if current[small_index]+1 < len(arr[small_index]):
			current[small_index] += 1
		#smallest minimum achieved i.e. best solution
		else: break 
	
	# find min and max of range dictionary
	new_range_min = sys.maxint
	new_range_max = 0
	for i in min_range: 
		new_range_min = min(new_range_min, arr[i][min_range[i]]) 
		new_range_max = max(new_range_max, arr[i][min_range[i]])
	return (new_range_min,new_range_max)

print smallest_range([
	[4,10,15,24,26],
	[0,9,12,20],
	[5,18,22,30]
	])
