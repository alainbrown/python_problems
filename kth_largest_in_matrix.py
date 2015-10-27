# Given a N*N Matrix. 
# All rows are sorted, and all columns are sorted. 
# Find the Kth Largest element of the matrix.
import heapq

# Complexity: O(k log N)
# Space: O(N)
def kth_largest(M, k):
	count,N = 0,len(M)
	if N*N < k: return None
	h = []
	for x in xrange(len(M)): heapq.heappush(h, (M[x][0],x,0))
	kth_val = h[0]

	while h and count < k:
		kth_val,arr_ind,n = heapq.heappop(h)
		count+=1
		if n+1<N: heapq.heappush(h, (M[arr_ind][n+1],arr_ind,n+1))
	return kth_val

m =[[0,5,8],
	[1,2,3],
	[5,6,7]]

print kth_largest(m, 6) == 5
