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

# Complexity: O(n*m) n words of length m
# Space: O(n*m) 
def transformation_steps(words,s,t):
	g={}
	jumps = 0
	for word in words:
		for i in xrange(len(word)):
			wild = word[:i]+'_'+word[i+1:]
			if wild in g: g[wild].append(word)
			else: g[wild] = [word]
	visited = set([s])
	next = [s]
	while t not in visited and next:
		temp = []
		for word in next:
			for i in xrange(len(word)):
				for path in g[word[:i]+'_'+word[i+1:]]:
					if path not in visited: 
						temp.append(path)
						visited.add(path)
		if not temp and t not in visited: return None
		next = temp
		jumps+=1
	return jumps

words = ['ace','cot','don','cog','cat','dog','con']
print transformation_steps(words,'cat','dog')==3
print transformation_steps(words,'cot','dog')==2
print transformation_steps(words,'ace','dog')==None
