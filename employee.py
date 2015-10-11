class Employee():
	def __init__(self,id,name,reports=[]):
		self.id = id
		self.name = name
		self.reports = reports

class EmployeeTree():
	def __init__(self, boss ={}):
		self.boss = boss
	
	def insert(self, employee):
		for e in employee.reports:
			self.boss[e.id] = employee
			self.insert(e)

	def common_manager(self, employee1,employee2):
		e1 = employee1
		while e1.id in self.boss:
			e1 = self.boss[e1.id]
			e2 = employee2
			while e2.id in self.boss:
				e2 = self.boss[e2.id]
				if e2 == e1:
					return e1

e1 = Employee(7,"L")
e2 = Employee(4,"Pop")
e3 = Employee(2,"Bob")
e4 = Employee(3,"Alex", [e1])
e = Employee(1,"Al",[e3, e4, e2])

t = EmployeeTree()
t.insert(e)
print t.common_manager(e1,e2).name
