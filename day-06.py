with open('./inputs/day-06-input.txt') as f:
	input = f.read()

	# traverse string from the left and check if that char is repeated in remaining string to the right:
	def all_chars_unique(s: str):
		for i in range(len(s) - 1):
			for j in range(i+1, len(s)):
				if s[i] == s[j]:
					return False
		return True
	
	# traverse string, starting at provided sequence length, and look back at the number of chars set by seq_len.
	# returns the position in the string at which the first sequence of 4 unique chars ends (position == index + 1).
	def first_unique_sequence(s: str, seq_len: int):
		for pos in range(seq_len, len(s)+1):
			if all_chars_unique(s[pos - seq_len : pos]):
				return pos

	print("First sequence of 4 unique characters ends at position:", first_unique_sequence(input, 4))
	print("First sequence of 14 unique characters ends at position:", first_unique_sequence(input, 14))

	# value:	1 2 3 4 5 6 7 8 9 10
	# index:	0 1 2 3 4 5 6 7 8 9