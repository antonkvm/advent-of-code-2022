from functools import reduce


with open("./day-1-input.txt", 'r') as f:
	# list = f.readlines()
	list = [line.strip() for line in f]

	print("--- Part One ---")

	listOfSums = []
	tempList = []
	for i in range(len(list)):
		if list[i] != "":
			tempList.append(int(list[i]))			
		if list[i] == "" or i == len(list) - 1:
			listOfSums.append(reduce(lambda a, b : a + b, tempList, 0))
			tempList = []
	print(reduce(lambda a, b : a if a > b else b, listOfSums))

	print("-- Part Two ---")
	
	listOfSums.sort(reverse = True)
	print(reduce(lambda a, b : a + b, listOfSums[0:3]))