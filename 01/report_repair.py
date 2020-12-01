import itertools

def get2020(l: list, tuple_size: int) -> tuple:
	for tup in itertools.combinations(l, tuple_size):
	 	if sum(tup) == 2020:
	 		return tup

numbers = []
with open("input.txt") as input_file:
	for line in input_file:
		numbers.append(int(line))

a, b = get2020(numbers, 2)
print(f"Part 1: {a*b}")

a, b, c = get2020(numbers, 3)
print(f"Part 2: {a*b*c}")
