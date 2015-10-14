import sys

def power_of_two(n):
	return (n>0) and (n & (n-1)) == 0

if __name__ == "__main__":
	print power_of_two(int(sys.argv[1]))
