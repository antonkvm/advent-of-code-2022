with open("./day-4-input.txt") as f:
	
	input = [line.strip() for line in f]
	input = [pair.split(",") for pair in input]

	count = 0
	count_2 = 0
	for row in range(len(input)):
		# input[row] = list(map(lambda x : x.split("-"), input[row]))
		input[row] = [x.split("-") for x in input[row]]
		input[row] = [[int(y) for y in x] for x in input[row]]
		start1 = input[row][0][0]
		end1 = input[row][0][1]
		start2 = input[row][1][0]
		end2 = input[row][1][1]

		if start1 >= start2 and end1 <= end2 or start2 >= start1 and end2 <= end1: count += 1
		if max(start1, start2) <= min(end1, end2): count_2 += 1

	print(count)
	print(count_2)