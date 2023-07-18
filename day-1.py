with open("./day-1-input.txt", 'r') as f:
	# list = f.readlines()
	list = [line.strip() for line in f]

	listOfSums = []
	tempList = []
	for i in range(len(list)):
		if list[i] != "":
			tempList.append(int(list[i]))			
		if list[i] == "" or list[i] is None:
			listOfSums.append(sum(tempList))
			tempList = []

	print("--- Part One ---")
	print(max(listOfSums))

	print("-- Part Two ---")	
	listOfSums.sort(reverse = True)
	print(sum(listOfSums[0:3]))
