# Remove dups from linked list

class Node:
	def __init__(self,val,nex=None):
		self.val=val
		self.nex=nex

def dedup(n):
	s = set([])
	prev = None
	while n not None: 
		if n.val in s: 
			prev.nex = n.nex
		else: 
			s.add(n.val)
			prev = n
		n = n.nex

def dedup_no_buffer(n):
	prev = None
	while n not None: 
		temp = n
		while temp.nex not None:
			if temp.nex.val == n.val: temp.nex=temp.nex.nex
			else: temp=n.nex 
		n = n.nex
