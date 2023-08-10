import copy


with open('./inputs/day-05-input.txt') as f:
	input = f.readlines()

	# -- 1: extract initial crate and stack positions ---

	number_of_stacks = 0
	initial_stack_height = 0

	for line in input:
		if line[1] == "1":
			# next line assumes number of stacks is a single digit int <= 9:
			number_of_stacks = int(line.strip()[-1])
			# if number of stacks could exceed 9:
			# number_of_stacks = line.split(" ")
			# number_of_stacks = list(filter(lambda a : a.isdigit(), number_of_stacks))
			# number_of_stacks = int(number_of_stacks[-1])
			initial_stack_height = input.index(line)
			break

	stacks = []

	# position of crateID in line in input text file: 1,5,9,13,17...
	# pos_x(n) = (n-1)*4+1  | n is number of stacks
	# next line is dependent on number of stacks not exceeding 9
	x_pos_all = [n * 4 + 1 for n in range(number_of_stacks)]
	y_pos_all = [n for n in range(initial_stack_height - 1, -1, -1)]

	for pos_x in x_pos_all:
		this_stack = []
		for pos_y in y_pos_all:
			if input[pos_y][pos_x].isalpha():
				this_stack.append(input[pos_y][pos_x])
		stacks.append(this_stack)

	# --- 2: execute rearrangement procedures ---

	# Assigning a list to another variable does not duplicate the list, it's just a reference to the same list.
	# Using some_list.copy() solves this problem, but only for the first layer in a list.
	# If a list contains another list, that same second layer list will still just be referenced twice.
	# To make a full deep copy of a multi-dimensional list, import the copy module and use it's deepcopy() method. 
	stacks_cp_1 = copy.deepcopy(stacks)
	stacks_cp_2 = copy.deepcopy(stacks)

	for y in range(initial_stack_height + 2, len(input)):
		cmd = map(lambda l : l if l.isdigit() else " ", input[y])
		cmd = "".join(cmd)
		cmd = cmd.split()
		cmd = [int(x) for x in cmd]
		quantity, origin, destination = cmd[0], cmd[1], cmd[2]
		tmp_stack = []
		for q in range(quantity):
			# grab each crate one by one:
			stacks_cp_1[destination-1].append(stacks_cp_1[origin-1].pop())
			# grab all crates together:
			tmp_stack.insert(0, stacks_cp_2[origin-1].pop())
		stacks_cp_2[destination-1].extend(tmp_stack)

		
	
	result_1 = [x[-1] for x in stacks_cp_1]
	result_1 = "".join(result_1)
	print(result_1)
	
	result_2 = [x[-1] for x in stacks_cp_2]
	result_2 = "".join(result_2)
	print(result_2)
