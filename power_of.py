
#O(log log n)
def is_power(d, n):
	if n == 0 or n == 1:
		return 0
	power = 1
	m = d
	while m < n:
		if m==n:
			return 1
		power *= 2
		m = d**power

	top = power
	bottom = top/2

	while bottom <= top:
		mid = (top+bottom)/2
		m = d**mid
		if m == n:
			return 1
		else:
			if m > n:
				top = mid-1
			else:
				bottom = mid+1
	return 0

print is_power(3, 27) == 1
print is_power(3, 9) == 1
print is_power(3, 42) == 0
print is_power(3, 0) == 0
print is_power(3, 3486784401) == 1
