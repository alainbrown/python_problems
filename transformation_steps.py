# Given a dictionary containing a list of words, a starting word, 
# and an ending word, return the minimum number of steps to 
# transform the starting word into the ending word. 

# A step involves changing one letter at a time to a valid word 
# that is present in the dictionary. 

# Return null if it is impossible to transform the starting word 
# into the ending word using the dictionary. 

# Example: 

# Starting word: cat 
# Ending word: dog 

# cat -> cot -> cog -> dog ('cot' and 'cog' are in the dictionary) 

# return 3

# Complexity: O(n^2)
# Space: O(n) 
def transformation_steps(words,s,t):
	parents = [i for i in xrange(len(words))]
	for i in xrange(len(words)):
		for j in xrange(i,len(words)):
			if one_change(words[i],words[j]):
				parents[i] = j
	p = words.index(s)
	q = words.index(t)
	jumps = set([])
	while p != parents[p]: 
		p = parents[p]
		jumps.add(p)
	while q != parents[q]: 
		q = parents[q]
		jumps.add(q)
	return None if len(jumps)==0 else len(jumps)

def one_change(s,t):
	if len(s)!=len(t): return False
	diff = 0
	for i in xrange(len(s)):
		if s[i]!=t[i]: diff+=1
	return diff==1

words = ['ace','cat','cot','don','con','cog','dog']
print transformation_steps(words,'cat','dog')==3
print transformation_steps(words,'cot','dog')==2
print transformation_steps(words,'ace','dog')==None
