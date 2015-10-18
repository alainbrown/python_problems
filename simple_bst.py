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
