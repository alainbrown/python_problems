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
	#edge cases
	if len(s) != len(t): return None
	if s not in words: return None
	if t not in words: return None
	if s == t: return 0
	
	g={}
	jumps = 0
	for word in words:
		if len(word) == len(s): #ignore other word lengths
			for i in xrange(len(word)):
				wild = word[:i]+'_'+word[i+1:]
				if wild in g: g[wild].append(word)
				else: g[wild] = [word]
	visited = set([s])
	bfs = [s]
	while t not in visited and bfs:
		paths = []
		for parent in bfs:
			for i in xrange(len(parent)):
				for word in g[parent[:i]+'_'+parent[i+1:]]:
					if word not in visited: 
						paths.append(word)
						visited.add(word)
		if not paths and t not in visited: return None
		bfs = paths
		jumps+=1
	return jumps

words = ['ace','cot','don','cog','cat','dog','con']
print transformation_steps(words,'cat','dog')==3
print transformation_steps(words,'cot','dog')==2
print transformation_steps(words,'ace','dog')==None
