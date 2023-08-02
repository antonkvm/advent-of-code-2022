import math
from functools import reduce

f = open("./day-11-input.txt")
input = [line.strip() for line in f]

class Monkey:
	def __init__(self, id: int, starting_items: list[int], operation: dict, test: int, action_if_true: int, action_if_false: int):
		self.id: int = id
		self.items: list[int] = starting_items
		self.operation: dict[str, int] = operation
		self.test: int = test
		self.recipient_if_true: int = action_if_true
		self.recipient_if_false: int  = action_if_false
		self.items_inspected: int = 0

monkey_dict: dict[int, Monkey] = {}

def safe_int(value) -> any:
	"""Tries to convert a value into a string. If not possible, returns the value untouched."""
	try:
		return int(value)
	except:
		return value

for i in range(0, len(input), 7):
	m_id = int(input[i].strip("Monkey :"))
	starting_items = [int(item) for item in input[i+1].split(": ")[1].split(", ")]
	operation = {}
	relevant_chunks = input[i+2].split(" = ")[1].split()
	operation["op"] = relevant_chunks[1]
	operation["val_a"] = safe_int(relevant_chunks[0])
	operation["val_b"] = safe_int(relevant_chunks[2])
	test = int(input[i+3].strip("Test: divisible by "))
	if_true = int(input[i+4][-1])
	if_false = int(input[i+5][-1])
	monkey_dict[m_id] = Monkey(m_id, starting_items, operation, test, if_true, if_false)

rounds = 20
for round in range(rounds):
	for monkey in monkey_dict.values():
		while 0 < len(monkey.items):
			monkey.items_inspected += 1
			val_b = monkey.operation["val_b"]
			if val_b == "old":
				val_b = monkey.items[0]
			else:
				val_b = int(val_b)
			if monkey.operation["op"] == "*":
				monkey.items[0] *= val_b
			else:
				monkey.items[0] += val_b
			monkey.items[0] = math.floor(monkey.items[0] / 3)
			if monkey.items[0] % monkey.test == 0:
				receiving_monkey = monkey_dict[monkey.recipient_if_true]
			else:
				receiving_monkey = monkey_dict[monkey.recipient_if_false]
			receiving_monkey.items.append(monkey.items.pop(0))

result = [monkey.items_inspected for monkey in monkey_dict.values()]
result = sorted(result)[-2:]
result = reduce(lambda a, b : a * b, result)
print(result)