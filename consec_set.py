# Given a set of numbers, find the longest subset with 
# consecutive numbers be it any order. 

# Input: 
# S = { 5, 1, 9, 3, 8, 20, 4, 10, 2, 11, 3} 

# we have 2 consecutive sets 
# s1 = {1, 2, 3, 4, 5} 
# s2 = { 8, 9, 10, 11} 

# Ans. 
# s1 = {1, 2, 3, 4, 5}

# O(n log n)
def naive_consec_set(n):
	largest_set = []
	m = sorted(n)
	last = m[0]-1
	last_set = []
	for i in m:
		if i == last+1: last_set.append(i)
		elif i==last: continue
		else: last_set = []
		if len(last_set) > len(largest_set): largest_set=last_set
		last = i
	return largest_set

print naive_consec_set([5, 1, 9, 3, 8, 20, 4, 10, 2, 11, 3])==[1, 2, 3, 4, 5]
