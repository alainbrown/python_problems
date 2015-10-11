import sys

moves = {
		1:[6,8],
		2:[7,9],
		3:[4,8],
		4:[3,0,9],
		5:[],
		6:[1,7,0],
		7:[2,6],
		8:[1,3],
		9:[2,4],
		0:[4,6]
		}
# O(n)
def knight_bfs_comp(start, digits):
	if start ==5 and digits > 1:
		return 0
	paths = {start:1}
	if start != 5:
		for i in xrange(digits-1): #max n
			nex = {}
			for m in paths: #max 9 ops
				for n in moves[m]: #max 3 ops
					if n in nex:
						nex[n] += paths[m]
					else:
						nex[n] = paths[m]
			paths = nex
	return sum(paths.values())

if __name__ == "__main__":
	start = int(sys.argv[1])
	digits = int(sys.argv[2])
	print knight_bfs_comp(start, digits)
