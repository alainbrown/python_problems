# Given an array of positive, unique, increasingly sorted numbers A, 
# e.g. A = [1, 2, 3, 5, 6, 8, 9, 11, 12, 13]. 
# Given a positive value K, e.g. K = 3. Output all pairs in A that differ exactly by K. 
# e.g. 
# 2, 5 
# 3, 6 
# 5, 8 
# 6, 9 
# 8, 11 
# 9, 12 
# what is the runtime for your code?

# Complexity: O(n) 
# Space: O(n)
def naive_diff_sum(A,k):
	m = set([])
	for i in xrange(len(A)): m.add(A[i])
	for i in xrange(len(A)): 
		if A[i]+k in m: print (A[i],A[i]+k)

# Complexity: O(n) 
# Space: O(1)
def diff_sum(A,k):
	front = 0
	back = 1
	while back<len(A)-1 and front < back:
		if abs(A[front]-A[back]) == k: 
			print (A[front],A[back])
			back += 1
			front += 1
		elif abs(A[front]-A[back]) < k: back += 1
		else: front += 1

naive_diff_sum([1, 2, 3, 5, 6, 8, 9, 11, 12, 13],3)
diff_sum([1, 2, 3, 5, 6, 8, 9, 11, 12, 13],3)
