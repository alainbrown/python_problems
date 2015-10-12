import sys

def power_of_two(n):
	if n < 2: return False
	return (n & (n-1)) == 0

if __name__ == "__main__":
	print power_of_two(int(sys.argv[1]))
