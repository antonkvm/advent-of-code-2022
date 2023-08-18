with open("./inputs/day-01-input.txt", 'r') as f:
	# list = f.readlines()
	input = [line.strip() for line in f]

	list_of_sums = []
	temp_sum = []
	for i in input:
		if i:
			temp_sum.append(int(i))
		else:
			list_of_sums.append(sum(temp_sum))
			temp_sum = []

	print("--- Part One ---")
	print(max(list_of_sums))

	print("-- Part Two ---")	
	list_of_sums.sort(reverse = True)
	print(sum(list_of_sums[0:3]))
