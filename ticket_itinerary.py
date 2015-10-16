# Given an bunch of airline tickets with [from, to], for example 
# [MUC, LHR], [CDG, MUC], [SFO, SJC], [LHR, SFO], 
# please reconstruct the itinerary in order, 
# for example: [ CDG, MUC, LHR, SFO, SJC ]. 
# tickets can be represented as nodes

#O(n) space and O(n) time
def itinerary(tickets):
	it = {}
	with_parents = set([])
	# from to map
	for ticket in tickets:
		it[ticket[0]] = ticket[1]
		with_parents.add(ticket[1])

	#find start
	starting = None
	for t in it: 
		if t not in with_parents: starting = t
	
	#trace path from start
	itin =[starting]
	while starting in it:
		starting = it[starting]
		itin.append(starting)
	return itin

print itinerary([["MUC","LHR"],["CDG","MUC"],["SFO","SJC"],["LHR","SFO"]])
