# Given an array of integer, find the maximum drop between two array elements, 
# given that second element comes after the first one.

# Complexity: O(n)
# Space: O(1)
def max_drop(N):
	drop = 0
	x = N[0]
	y = N[1]
	for i in xrange(len(N)-1):
		x = max(x,N[i])
		y = min(y,N[i+1])
		drop = max(drop, x-y)
	return drop

print max_drop([1,3,7,10,1,3,90,3,-10]) == 100
