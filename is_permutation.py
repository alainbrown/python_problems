# Given two strings, write a method to decide if one is 
# a permutation of the other.

def is_permutation(s,t):
	if len(s) != len(t): return False
	perms = {}
	for i in xrange(len(s)):
		if s[i] in perms: perms[s[i]] += 1
		else: perms[s[i]] = 1
	for j in xrange(len(t)):
		if t[j] in perms and perms[t[j]]>0: perms[t[j]] -= 1
		else: return False
	return True
