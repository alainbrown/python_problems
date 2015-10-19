# Give you an array which has n integers,it has both positive 
# and negative integers.Now you need sort this array in a 
# special way.After that,the negative integers should in the front,
# and the positive integers should in the back.Also the relative 
# position should not be changed. 
# eg. -1 1 3 -2 2 ans: -1 -2 1 3 2. 
# o(n)time complexity and o(1) space complexity is perfect.

# O(n) time and space
def sign_sort(arr):
	neg = 0
	sort = [0 for i in xrange(len(arr))]
	for i in xrange(len(arr)):
		if arr[i] < 0: 
			sort[neg] = arr[i]
			neg += 1
	for i in xrange(len(arr)):
		if arr[i] > 0:
			sort[neg] = arr[i]
			neg += 1
	return sort

print sign_sort([-1,1,3,-2,2]) == [-1,-2,1,3,2]
