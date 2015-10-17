# Determine minimum sequence of adjacent values in the 
# input parameter array that is greater than input parameter sum. 

# Eg 
# Array 2,1,1,4,3,6. and Sum is 8 
# Answer is 2, because 3,6 is minimum sequence greater than 8.

# Naive, finds all subsequences totaling to Sum 
# Complexity: O(n^2)
# Space: O(1)
def min_sequence_count(N, Sum):
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

print min_sequence_count([2,1,1,4,3,6], 8) == 2
