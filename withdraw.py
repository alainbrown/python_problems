# You have some money in your bank account, the only function 
# to withdraw money is uint16 Withdraw(uint16 value), if the 
# value is greater than the money you have it returns 0, 
# otherwise it withdraws the requested amount and returns the 
# "value" 
#Write a function that withdraws all your money.

class Account():
	def __init__(self,v): self.v = v
	
	def withdraw(self,n):
		if n>self.v: return 0
		else: 
			self.v -= n
			return n

uint16 = (2**16)-1 

# O(nlogn)
def withdrawAll(a):
	top = uint16
	bottom = 1
	withdrawl = 0
	while bottom < top:
		mid = (top+bottom)/2
		r = a.withdraw(mid)
		if r > 0:
			top -= max(0,top-r)
			bottom = max(0, mid-r)
			withdrawl += r
		else: top = mid
	return withdrawl

for a in [Account(10000),Account(1000), Account(65000), Account(3)]:
	print (a.v == withdrawAll(a)) and (a.v ==0)
