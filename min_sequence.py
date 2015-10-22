# Determine minimum sequence of adjacent values in the 
# input parameter array that is greater than input parameter sum. 

# Eg 
# Array 2,1,1,4,3,6. and Sum is 8 
# Answer is 2, because 3,6 is minimum sequence greater than 8.

# Naive, finds all subsequences totaling to Sum 
# Complexity: O(n^2)
# Space: O(1)
def naive_min_sequence(N, Sum):
	m_seq = (1, N[0]) #seq_count,sum
	for x in xrange(1,len(N)): 
		m_seq = (m_seq[0]+1,m_seq[1]+N[x])
		if m_seq[1] > Sum: break

	for i in xrange(len(N)):
		m = (1, N[i]) 
		for j in xrange(i+1,len(N)):
			m = (m[0]+1, N[j]+m[1])
			if N[j]+m[1] > 8: break
		if m[0]<m_seq[0] and m[1]>Sum: m_seq = m

	return m_seq[0]

# Finds size of minimal subsequence totaling to Sum 
# Complexity: O(n)
# Space: O(1)
def min_sequence(N, Sum):
	if sum(N) < Sum: return None
	front = 0
	back = 0
	final_seq = len(N)
	last_sum = N[0]
	while back+1<len(N) or front+1<back:
		if last_sum > Sum and front+1<len(N):
			front += 1
			last_sum -= N[front-1]
			final_seq = min(final_seq,back-front+1)
		elif back+1<len(N):
			back += 1
			last_sum += N[back]
	return final_seq

print naive_min_sequence([2,1,1,4,3,6], 8) == 2
print min_sequence([2,1,1,4,3,6], 8) == 2
print min_sequence([1,1,1,1,1,1], 8) == None
