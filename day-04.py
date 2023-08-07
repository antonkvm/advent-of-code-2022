with open("./day-04-input.txt") as f:
	
	input = f.readlines()
	input = [pair.split(",") for pair in input]

	count = 0
	count_2 = 0
	for row in input:
		row = [[int(y) for y in x.split("-")] for x in row]
		start1 = row[0][0]
		end1 = row[0][1]
		start2 = row[1][0]
		end2 = row[1][1]

		if start1 >= start2 and end1 <= end2 or start2 >= start1 and end2 <= end1:
			count += 1
		if max(start1, start2) <= min(end1, end2):
			count_2 += 1

	print(count)
	print(count_2)