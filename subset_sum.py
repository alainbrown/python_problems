# Given an array (A) find if there is a subset that sum to x

# Complexity: O(A*x)
# Space: O(x)
def subsetSum(A, x):
	if x<0 or x>sum(A): return False

	sub_sum=[False]*(x+1)
	sub_sum[0]=True
	for p in xrange(len(A)):
		for q in xrange(x,A[p]-1,-1):
			if not sub_sum[q] and sub_sum[q-A[p]]: sub_sum[q]=True
	return sub_sum[x]

print subsetSum([2,7,3,8,1,8,5,4,1,9], 30)==True
print subsetSum([2,7,3,8,1,8,5,4,1,9],10000)==False
