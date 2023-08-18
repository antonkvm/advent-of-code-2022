from functools import reduce


with open("./inputs/day-03-input.txt") as f:
	rucksacks = f.readlines()

	print("--- Part One ---")

	duplicates = []
	for rucksack in rucksacks:
		compA = rucksack[:len(rucksack)//2]
		compB = rucksack[len(rucksack)//2:]
		for item in compA:
			if compB.find(item) != -1:
				duplicates += item
				break
		
	def convertItemToNumber(itemAsLetter: str):
		x = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		if itemAsLetter.islower():
			return x.lower().find(itemAsLetter) + 1
		else:
			return x.find(itemAsLetter) + 1 + 26

	result_1 = list(map(convertItemToNumber, duplicates))
	result_1 = reduce(lambda a, b : a + b, result_1, 0)
	print(result_1)


	print("--- Part Two ---")

	# create a list of list: each inner list contains a group of 3 elves:
	all_groups = []
	for i in range(0, len(rucksacks), 3):
		all_groups.append([x for x in rucksacks[i : i + 3]])

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