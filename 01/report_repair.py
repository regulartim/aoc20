import itertools

def getSummands(l: list, result: int, tuple_size: int) -> tuple:
	for tup in itertools.combinations(l, tuple_size):
	 	if sum(tup) == result:
	 		return tup

with open("input.txt") as input_file:
	numbers = [int(line) for line in input_file]

a, b = getSummands(numbers, result=2020, tuple_size=2)
print(f"Part 1: {a*b}")

a, b, c = getSummands(numbers, result=2020, tuple_size=3)
print(f"Part 2: {a*b*c}")
