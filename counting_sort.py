#Space: O(k) where k = max(n)
#Complexity: O(n)
def counting_sort(A):
	B = [0]*len(A)
	k = max(A)+1
	C = [0]*k
	for j in xrange(k): C[A[j]]+=1
	for i in xrange(1,k): C[i]+=C[i-1]
	for j in xrange(len(A)-1,-1,-1):
		B[C[A[j]]-1] = A[j]
		C[A[j]] -= 1
	return B

print counting_sort([2, 7, 5, 5, 2, 7, 0, 8, 1])
