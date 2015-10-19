# Check if two integers are equal without using any comparison operators.

def equals(n,m): return not (n ^ m)

print equals(3,3) == True
print equals(2,1) == False
print equals(-2,-2) == True
print equals(3,7) == False
