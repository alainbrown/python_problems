# Given two strings, find number of discontinuous matches.
# Example: "cat", "catapult"
# #Output: 3

def discont_match_dfs(sub,word,path="",pos=0):
	if path == sub: return 1
	if len(path) >= len(sub): return 0

	count = 0
	for i in xrange(len(word)):
		if word[i] == sub[pos]:
			count += discont_match_dfs(sub, word[i+1:],path+word[i], pos+1)
	return count

def discont_match_bfs(sub,word):
	if sub == word: return 1
	
	paths = {0:1} 
	for i in xrange(len(sub)): 
		nex = {}
		for m in paths:
			for n in xrange(m,len(word)):
				if sub[i] == word[n]:
					if n in nex: nex[n] += paths[m]
					else: nex[n] = paths[m]
		paths = nex
	return sum(paths.values())

#O(m+n) m letters in sub, n letters in word
def discont_match(sub,word):
	if sub == word: return 1

	sub_map = {}
	for i in xrange(len(sub)): sub_map[sub[i]] = i
	paths = {}
	for i in xrange(len(word)):
		if word[i] in sub_map:
			s = sub_map[word[i]]
			if s == 0: 
				if s in paths: paths[s] += paths[s]
				else: paths[s] = 1
			elif s-1 in paths:
				if s in paths: paths[s] += paths[s-1]
				else: paths[s] = 1
	return paths[len(sub)-1]

print discont_match_dfs("cat", "catapult") == 3
print discont_match_bfs("cat", "catapult") == 3
print discont_match("cat", "catapult") == 3
