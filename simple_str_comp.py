# Implement a method to perform basic string compression 
# using the counts of repeated characters. 

# aabcccccaaa -> a2b1c5a3

def compress(s):
	n = ""
	last = s[0]
	count = 0
	for i in xrange(len(s)):
		if last == s[i]: count +=1
		else: 
			n+=last+str(count)
			count = 1
		last = s[i]

	n+=last+str(count)
	if len(n)<len(s): return n
	else: return s

print compress("aabcccccaaa")
