with open("./day-02-input.txt") as f:

	guide = [line.split() for line in f]

	# part one:
	points = 0
	for round in guide:
		match round[0]:
			case "A":
				match round[1]:
					case "X": points += 1 + 3	# rock
					case "Y": points += 2 + 6	# paper
					case "Z": points += 3 + 0	# scissors
			case "B":
				match round[1]:
					case "X": points += 1 + 0
					case "Y": points += 2 + 3
					case "Z": points += 3 + 6
			case "C":
				match round[1]:
					case "X": points += 1 + 6
					case "Y": points += 2 + 0
					case "Z": points += 3 + 3
	print(points)

	# part two:
	points = 0
	for round in guide:
		match round[0]:
			case "A":
				match round[1]:
					case "X": points += 0 + 3	# lose
					case "Y": points += 3 + 1	# draw
					case "Z": points += 6 + 2	# win
			case "B":
				match round[1]:
					case "X": points += 0 + 1
					case "Y": points += 3 + 2
					case "Z": points += 6 + 3
			case "C":
				match round[1]:
					case "X": points += 0 + 2
					case "Y": points += 3 + 3
					case "Z": points += 6 + 1
	print(points)