# Given an infinite stream of characters and a list L of strings, 
# create a function that calls an external API when a word in L 
# is recognized during the processing of the stream. 

# Example: 
# L = ["ok","test","one","try","trying"] 
# stream = a,b,c,o,k,d,e,f,t,r,y,i,n,g............. 

# the call to external API (let's call it some function callAPI()) 
# would be called when the 'k' is encountered, again when the 'y' 
# is encountered, and again at 'g'.

class Trie:
	def __init__(s,letter):
		s.letter=letter
		s.children={}
		s.last=False

	def insert(s,word):
		if len(word)>0:
			l = word[0]
			if l not in s.children: s.children[l]=Trie(l)
			s.children[l].insert(word[1:])
			if len(word)==1: s.children[l].last=True

# Complexity: O(1)
# Space: O(n) n number of words in L
def stream_contains(L, stream):
	top = Trie(None)
	for word in L: top.insert(word)
	test = top
	while stream:
		l = stream.read_letter()
		if l in test.children: 
			test = test.children[l]
			if test.last: callAPI()
		else: test = top
