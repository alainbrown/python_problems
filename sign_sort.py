# Give you an array which has n integers,it has both positive 
# and negative integers.Now you need sort this array in a 
# special way.After that,the negative integers should in the front,
# and the positive integers should in the back.Also the relative 
# position should not be changed. 
# eg. -1 1 3 -2 2 ans: -1 -2 1 3 2. 
# o(n)time complexity and o(1) space complexity is perfect.

# O(n) time
# O(1) space
def sign_sort(arr):
	neg = 0
	pos = 0
	for i in xrange(len(arr)):
		print arr
		if arr[i] < 0: 
			arr[neg],arr[i] = arr[i],arr[neg]
			arr[pos],arr[i] = arr[i],arr[pos]
			neg += 1
		else:
			pos += 1

a=[-1,1,3,-2,2]
sign_sort(a) 
print a == [-1,-2,1,3,2]
