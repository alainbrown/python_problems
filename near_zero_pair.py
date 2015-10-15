#Given an array of numbers, find a pair whose sum is closest to zero.

#O(nlogn)
def near_zero_pair(arr):
	nex = sorted(arr)
	ans = None
	for i in xrange(len(nex)-1):
		s = abs(nex[i] + nex[i+1])
		if ans == None or s < ans[0]:
			ans = (s,nex[i],nex[i+1])
	return (ans[1],ans[2])

print near_zero_pair([1,-10,3,-8,12,13,80,20,2,-30])
