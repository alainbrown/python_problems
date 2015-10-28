# Write an algorithm such that if an element in an MxN matrix is 0, 
# its entire row and column are set to 0.

def matrix_zero(matrix):
	row = set([])
	column = set([])

	for i in xrange(len(matrix)):
		for j in xrange(len(matrix[i])):
			if matrix[i][j] == 0:
				row.add(i)
				column.add(j)

	for i xrange(len(matrix)):
		for j in xrange(len(matrix[i])):
			if i in row or j in column: matrix[i][j]=0

