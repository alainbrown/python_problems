# You have an array of integers(size N), such that each integer 
# is present an odd number of time, except 3 of them(which are 
# present even number of times). Find the three numbers. 

# Goal:
# Time Complexity: O(N) 
# Space Complexity: O(1) 

# Sample Input: 
# {1,6,4,1,4,5,8,8,4,6,8,8,9,7,9,5,9} 
# Sample Output: 
# 1 5 6 8

# Complexity: O(n)
# Space: O(n)
def naive_odd_count(N):
	m = {}
	for i in N:
		if i in m: m[i] += 1
		else: m[i] = 1
	ans = []
	for j in m:
		if m[j] % 2 == 0: ans.append(j)
	return ans

print naive_odd_count([1,6,4,1,4,5,8,8,4,6,8,8,9,7,9,5,9])==[1,5,6,8]
