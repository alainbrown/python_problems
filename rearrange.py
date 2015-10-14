import heapq,sys

def rearrange(word):
	count = {}
	for l in word:	#O(n)
		if l in count: count[l] -= 1
		else: count[l] = -1
	tupes = []
	for l in count: heapq.heappush(tupes,(count[l],l))
	rword = ''
	last = ''
	altupes = []
	while len(tupes) > 0:
		c,l = heapq.heappop(tupes) #O(log n)
		if last == l:
			heapq.heappush(altupes, (c,l)) #O(log n)
		else:
			rword += l
			if c < -1:
				heapq.heappush(tupes, (c+1,l)) #O(log n)
			if len(altupes) > 0:
				heapq.heappush(tupes, heapq.heappop(altupes)) #O(log n)
		if len(altupes) > 0 and len(tupes) == 0:
			return None #No solution
		last = l
	return rword

if __name__ == "__main__":
	print rearrange(sys.argv[1])
