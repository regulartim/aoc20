import time

begin = time.time()

###

def product(l: list) -> int:
	acc = 1
	for val in l:
		acc = acc * val
	return acc

def isInSingleInterval(n: int, interval: tuple) -> bool:
	a, b = interval
	return a <= n <= b

def isInIntervals(n: int, intervals: list) -> bool:
	return True in (isInSingleInterval(n, i) for i in intervals)

def isValidNumber(n: int) -> bool:
	return True in (isInIntervals(n, intervals) for intervals in FIELDS.values())

def findInvalidNumbers(ticket: list) -> list:
	return [n for n in ticket if not isValidNumber(n)]

def isValidTicket(ticket: list) -> bool:
	return not findInvalidNumbers(ticket)

def findValidPositions(tickets: list) -> dict:
	res = dict()
	for k, v in FIELDS.items():
		for pos, _ in enumerate(tickets[0]):
			numbers = [t[pos] for t in tickets]
			valid_numbers = [n for n in numbers if isInIntervals(n, v)]
			if len(numbers) == len(valid_numbers):
				res.setdefault(k, set()).add(pos)
	return res

def reducePositions(d: dict) -> dict:
	unique = set()
	while len(unique) < len(d):
		for v in d.values():
			if len(v) > 1:
				v.difference_update(unique)
			else:
				unique.update(v)
	return d


with open("input.txt") as input_file:
	blocks = input_file.read().split("\n\n")

FIELDS = dict()
for line in blocks[0].split("\n"):
	key, values = line.split(":")
	values = values.split()
	values = [values[0].split("-"), values[-1].split("-")]
	values = [(int(a), int(b)) for a, b in values]
	FIELDS[key] = values

my_ticket = [int(n.strip()) for n in blocks[1].split(":")[1].split(",")]
ticket_lines = blocks[2].split("\n")[1:]
nearby_tickets = [[int(n) for n in line.split(",")] for line in ticket_lines if line != ""]

valid_tickets = [my_ticket] + [t for t in nearby_tickets if isValidTicket(t)]
valid_positions = findValidPositions(valid_tickets)
valid_positions = reducePositions(valid_positions)
depature_indices = [v.pop() for k, v in valid_positions.items() if "departure" in k]

print(f"Part 1: {sum([sum(findInvalidNumbers(t)) for t in nearby_tickets])}")
print(f"Part 2: {product([my_ticket[idx] for idx in depature_indices])}")

###

end = time.time()
print(f"Runtime: {end - begin}")
