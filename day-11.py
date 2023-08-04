import math
from functools import reduce

f = open("./day-11-input.txt")
input = [line.strip() for line in f]

class Monkey:
	def __init__(self, id: int, starting_items: list[int], operation: str, operand: str, test: int, action_if_true: int, action_if_false: int):
		self.id: int = id
		self.items: list[int] = starting_items
		self.operation: str = operation
		try:
			self.operand = int(operand)
		except:
			self.operand = None
		self.test: int = test
		self.recipient_if_true: int = action_if_true
		self.recipient_if_false: int  = action_if_false
		self.items_inspected: int = 0

def create_monkeys(input: list[str]) -> dict[int, Monkey]:
	all_monkeys: dict[int, Monkey] = {}
	for i in range(0, len(input), 7):
		m_id = int(input[i].strip("Monkey :"))
		starting_items = [int(item) for item in input[i+1].split(": ")[1].split(", ")]
		operation_substring = input[i+2].split("= old")[1].split()
		operation = operation_substring[0]
		operand = operation_substring[1]
		test = int(input[i+3].strip("Test: divisible by "))
		if_true = int(input[i+4][-1])
		if_false = int(input[i+5][-1])
		all_monkeys[m_id] = Monkey(m_id, starting_items, operation, operand, test, if_true, if_false)
	return all_monkeys
	
def play(rounds: int, part_2_mod: bool):
	all_monkeys = create_monkeys(input)
	super_modulo = reduce(lambda a, b : a * b, [monkey.test for monkey in all_monkeys.values()])
	for round in range(rounds):
		for monkey in all_monkeys.values():
			while 0 < len(monkey.items):
				monkey.items_inspected += 1
				current_operand = monkey.operand if monkey.operand is not None else monkey.items[0]
				if monkey.operation == "*":
					monkey.items[0] *= current_operand
				else:
					monkey.items[0] += current_operand
				# avoid huge numbers by masking the part of the number that is divisible by all test numbers:
				if not part_2_mod: 
					monkey.items[0] = math.floor(monkey.items[0] / 3)
				else:
					monkey.items[0] %= super_modulo
				if monkey.items[0] % monkey.test == 0:
					receiving_monkey = all_monkeys[monkey.recipient_if_true]
				else:
					receiving_monkey = all_monkeys[monkey.recipient_if_false]
				receiving_monkey.items.append(monkey.items.pop(0))
	result = [monkey.items_inspected for monkey in all_monkeys.values()]
	result = sorted(result)[-2:]
	result = reduce(lambda a, b : a * b, result)
	print(result)
	
play(rounds=20, part_2_mod=False)
play(rounds=10000, part_2_mod=True)