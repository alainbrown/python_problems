# You are given a positive integer number N. 
#Return the minimum number K, such that N can be represented as K integer squares. 
# Examples: 
# 9 --> 1 (9 = 3^2) 
# 8 --> 2 (8 = 4^2 + 4^2) 
# 15 --> 4 (15 = 3^2 + 2^2 + 1^2 + 1^2) 
# First reach a solution without any assumptions, 
# then you can improve it using this mathematical lemma: 
# For any positive integer N, there is at least one representation of N as 4 or less squares.
import math

def min_squares(N):
	rem = N
	squares = 0
	while rem >0:
		squares += 1
		rem -= int(math.sqrt(rem))**2
	return squares

print min_squares(9) == 1
print min_squares(8) == 2
print min_squares(15) == 4
print min_squares(2**32-7) == 4
