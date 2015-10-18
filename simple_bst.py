class Node:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.val = val

	def insert(self, node):
		if self.val > node.val:
			if self.left is None: self.left = node
			else: self.left.insert(node)
		else:
			if self.right is None: self.right = node
			else: self.right.insert(node)

	def search(self, n):
		if self.val == n: return True
		if self.val > n:
			if self.left is None: return False
			else: return self.left.search(n)
		else:
			if self.right is None: return False
			else: return self.right.search(n)

	def ordered_array(self, arr):
		if self.left is not None: self.left.ordered_array(arr)
		arr.append(self.val)
		if self.right is not None: self.right.ordered_array(arr)

def test(A):
	root = Node(A[0])
	for i in xrange(1,len(A)): root.insert(Node(A[i]))
	print root.search(8)
	a =[]
	root.ordered_array(a)
	print a

test([2, 7, 5, 5, 2, 7, 0, 8, 1])
