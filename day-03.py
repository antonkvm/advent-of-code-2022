from functools import reduce


with open("./inputs/day-03-input.txt") as f:
	rucksacks = f.readlines()

	# print("Number of rucksacks:", len(rucksacks))

	print("--- Part One ---")

	duplicates = []
	for sack in rucksacks:
		# We assume len(sack) to be even. Still, we need to do // integer devision to guarantee an int as index.
		compA = sack[0:len(sack)//2]	# slicing includes the start index and excludes the end index!
		compB = sack[len(sack)//2:]

		for item in compA:
			duplicateIndex = compB.find(item)
			if duplicateIndex != -1:
				duplicates += item
				duplicateFound = True
				break
		
	# print("Number of duplicates:", len(duplicates))

	def convertItemToNumber(itemAsLetter: str):
		x = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		if itemAsLetter.islower(): return x.lower().find(itemAsLetter) + 1
		else: return x.find(itemAsLetter) + 1 + 26

	result_1 = list(map(convertItemToNumber, duplicates))
	# print("Number of converted duplicates:", len(result))
	result_1 = reduce(lambda a, b : a + b, result_1, 0)
	print(result_1)


	print("--- Part Two ---")

	# create a list of list: each inner list contains a group of 3 elves:
	all_groups = []
	for i in range(len(rucksacks) // 3):
		all_groups.append([])
		for j in range(3):
			all_groups[i].append(rucksacks[3*i+j])

	badges = []
	for group in all_groups:
		elf_1, elf_2, elf_3 = group[0], group[1], group[2]
		for item in elf_1:
			if item in elf_2 and item in elf_3:
				badges.append(item)
				break

	badges = map(convertItemToNumber, badges)
	result_2 = reduce(lambda a, b : a + b, badges)
	print(result_2)