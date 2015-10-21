# Given a set of numbers, find the longest subset with 
# consecutive numbers be it any order. 

# Input: 
# S = { 5, 1, 9, 3, 8, 20, 4, 10, 2, 11, 3} 

# we have 2 consecutive sets 
# s1 = {1, 2, 3, 4, 5} 
# s2 = { 8, 9, 10, 11} 

# Ans = 5 i.e {1, 2, 3, 4, 5} 

# Complexity: O(n log n)
# Space: O(n)
def naive_consec_set(n):
	largest_set = 0
	m = sorted(n)
	last = m[0]-1
	last_set = 0
	for i in m:
		if i == last+1: last_set+=1
		elif i==last: continue
		else: last_set = 0
		if last_set > largest_set: largest_set=last_set
		last = i
	return largest_set

print naive_consec_set([5, 1, 9, 3, 8, 20, 4, 10, 2, 11, 3])==5

# Complexity: O(n)
# Space: O(n)
def consec_set(N):
	largest_set = 0	
	visited = {}
	for i in N: visited[i] = False
	for i in N:
		if not visited[i]:
			large_set = 1
			p,n=i-1,i+1
			while p in visited: 
				large_set+=1
				visited[p]=True
				p-=1
			while n in visited:
				large_set+=1
				visited[n]=True
				n+=1
			if large_set > largest_set: largest_set = large_set
	return largest_set

print consec_set([5, 1, 9, 3, 8, 20, 4, 10, 2, 11, 3])==5
