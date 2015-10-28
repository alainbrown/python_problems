# Assume you have a method isSubstring which checks if one word
# is a substring of another: Given two strings, s1 and s2, write
# code to check if s2 is a rotation of s1 using only one call to
# isSubstring.

def isRotation(s1,s2):
	if s1 and len(s1)==len(s2): return isSubstring(s1+s2,s2)
	return False
