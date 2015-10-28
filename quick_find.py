class WQUF:
	def __init__(self,N):
		self.count = N
		self.parents = [i for i in xrange(N)]
		self.sizes = [i for i in xrange(N)]

	def find(self, p):
		while p != self.parents[p]: p = self.parents[p]
		return p

	def is_connected(self,p,q): return self.find(p)==self.find(q)

	def union(self,p,q):
		rootP, rootQ = self.find(p), self.find(q)
		if rootP==rootQ: return
		if self.sizes[rootP] < self.sizes[rootQ]:
			self.parents[rootP] = rootQ
			self.sizes[rootQ] += self.sizes[rootP]
		else:
			self.parents[rootQ] = rootP
			self.sizes[rootP] += self.sizes[rootQ]
		self.count -=1
