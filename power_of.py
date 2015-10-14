import math

def is_power(d, n):
	if n == 0 or n == 1: return 0
	r=math.log10(n)/math.log10(d)
	return 1 if (r-math.floor(r)) == 0 else 0

print is_power(3, 27) == 1
print is_power(3, 9) == 1
print is_power(3, 42) == 0
print is_power(3, 0) == 0
print is_power(3, 3486784401) == 1
print is_power(4, 64) == 1
