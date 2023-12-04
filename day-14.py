f = open("./inputs/day-14-input.txt")

input = [[tuple([int(num) for num in pos.split(",")]) for pos in line.strip().split(" -> ")] for line in f]

for i in input:
    print(i)