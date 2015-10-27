# Three strings say A,B,C are given to you. 
# Check weather 3rd string is interleaved from string A and B. 
# Ex: A="abcd" B="xyz" C="axybczd". answer is yes. o(n)

def interleaved(A,B,C):
	x = 0
	y = 0
	for i in xrange(len(C)):
		if C[i] == A[x]: x += 1
		elif C[i] == B[y]: y +=1
		else: return False
	return True

print interleaved("abcd","xyz","axybczd")
