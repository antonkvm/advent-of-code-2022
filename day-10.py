f = open("./day-10-input.txt")
input = f.read().split()

x = 1
signal_sum = 0
output = ""

for index, word in enumerate(input):
    cycle = index + 1
    if cycle in [20, 60, 100, 140, 180, 220]:
        signal_sum += (index + 1) * x
    sprite_range = range(x - 1, x + 2)
    index_in_row = index % 40
    end_of_row: bool = index_in_row == 39
    if index_in_row in sprite_range:
        output += "█"
    else:
        output += " "
    if end_of_row:
        output += "\n"
    try:
        v = int(word)
        x += v
    except ValueError:
        continue

print(f"Sum of relevant signal strengths: {signal_sum}")
print(output)