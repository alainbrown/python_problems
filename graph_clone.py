
class Node:
	def __init__(self, val, nodes=[]):
		self.val = val
		self.nodes = []

	def __hash__(self): 
		return hash(self.val)
	
	def __eq__(self, other): 
		return (self.val, self.nodes) == (other.val, other.nodes)

class Graph:
	def __init__(self, nodes): 
		self.nodes = nodes

	def clone(self):
		m = {}
		new_nodes = []
		for n in self.nodes: 
			new_node = Node(n.val)
			m[n] = new_node
			new_nodes.append(new_node)
		for i in self.nodes:
			for j in m[i].nodes: m[i].nodes.append(m[j])
		return Graph(new_nodes)

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')

a.nodes.append(b)
b.nodes.append(c)
c.nodes.append(d)
c.nodes.append(a)
d.nodes.append(e)
e.nodes.append(a)

g = Graph([a,b,c,d,e])
g_clone =g.clone()
