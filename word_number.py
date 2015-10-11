import math, sys

# O(n)
def dist_perms(word):
	letter_counts = {}
	for l in word:
		c = 0
		if l in letter_counts:
			c = letter_counts[l]
		letter_counts[l] = c+1
	denom = 1
	for l in letter_counts:
		num = letter_counts[l]
		denom *= math.factorial(num)
	return math.factorial(len(word))/denom

# O(n^2)
def word_number(original):
	count = 1
	permutation = ''
	next_letters = sorted(original)
	position = 0
	while permutation != original:
		last = None
		for i in range(len(next_letters)):
			if last != next_letters[i]:
				last = next_letters[i]
				ori = original[position]
				nex = next_letters[:i] + next_letters[i+1:]
				if last == ori:
					permutation += last
					position += 1
					next_letters = nex
					break
				else:
					count += dist_perms(nex)
	return count

if __name__ == "__main__":
	print word_number(sys.argv[1])
