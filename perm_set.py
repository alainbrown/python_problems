# Given a set of values 0-9, return all permutations of that set of length n. 
# Example: n=2, set ={2,3,4} 
# Return: {2,2}, {3,3}, {4,4}, {2,3}, {3,2}, {3,4}, {4,3}, {2,4}, {4,2}

def perms(N, n, x):
	if n==0: return x
	p = []
	for i in N:
		y = x[:]
		y.append(i)
		p.append(perms(N, n-1, y))
	return p

start = []
print perms([2,3,4],2,start)
