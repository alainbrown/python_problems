# You are given a double linked list and an array of pointers 
# to elements in this list (no assumptions can be made on the 
# 	array - number of pointers, order and duplicates allowed). 
# Return the number of sequences of elements (groups of consecutive 
# 	elements), pointed by the array. 

# For example, if this is the array (number relates to index in 
# 	the list, not the actual pointer value): 9,1,3,7,8,5,2. 
# Then output is 3, representing these sequences: [1,2,3], [5], [7,8,9]

class Node:
	def __init__(self,val,pre=None,nex=None):
		self.val=val
		self.pre=pre
		self.nex=nex

# Complexity: O(n)
# Space: O(n)
def num_sequences(head, pointers):
	visited = {}
	num_seq = 0
	for i in pointers: visited[i] = False
	for i in pointers:
		if not visited[i]:
			left,right = i,i
			while left-1 in visited:
				left -= 1
				visited[left] = True
			while right+1 in visited:
				right += 1
				visited[right] = True
			num_seq += 1
	return num_seq

print num_sequences(None, [9,1,3,7,8,5,2]) == 3
