# Write all solutions for a^3+b^3 = c^3 + d^3, 
# where a, b, c, d lie between [0, 10^5] in at least O(n^2) complexity

# Complexity: O(n^2)
# Space: O(n^2)
def solve(x,y):
	left = {}
	for a in xrange(x,y):
		for b in xrange(x,y):
			m = a**3+b**3
			if m in left: left[m].append((a,b))
			else: left[m] = [(a,b)]
	for c in xrange(x,y):
		for d in xrange(x,y): 
			n = c**3+d**3
			if n in left:
				for s in left[n]: print (s[0],s[1],c,d)

solve(0,10**5)
