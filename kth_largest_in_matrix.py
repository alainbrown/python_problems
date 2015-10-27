# Given a N*N Matrix. 
# All rows are sorted, and all columns are sorted. 
# Find the Kth Largest element of the matrix.
import heapq

# Complexity: O(mlog N) where m is the max of k and N
# Space: O(N) in N*N matrix M
def kth_largest(M, k):
	for a in M:
		if len(M)!=len(a): raise ValueError('M must be NxN matrix')
	if k>1 and k > len(M)**2: raise ValueError('Invalid k, must 0 < k < NxN')
	h,kth_val = [],0
	for x in xrange(len(M)): heapq.heappush(h, (M[x][0],x,0))

	while h and k>0:
		kth_val,arr_ind,n = heapq.heappop(h)
		k-=1
		if n+1<len(M[arr_ind]): heapq.heappush(h, (M[arr_ind][n+1],arr_ind,n+1))
	return kth_val

m =[[0,5,8,10],
	[1,2,3,12],
	[5,6,7,14],
	[20,30,40,50]]

print kth_largest(m, 6) == 5
