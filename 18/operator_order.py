import time
import itertools

begin = time.time()

###

def makeEquation(l: list) -> list:
	res = list()
	for elem in l:
		tmp = list()
		while elem[0] == "(":
			res.append("(")
			elem = elem[1:]
		while elem[-1] == ")":
			tmp.append(")")
			elem = elem[:-1]
		if elem not in "+*":
			elem = int(elem)
		res += [elem] + tmp
	return res


def solveInner(eq: list, same_precedence: bool) -> list:
	for idx, char in enumerate(eq):
		if char == "(":
			start = idx
		if char == ")":
			stop = idx
			break
	inner = eq[start+1:stop]
	res = solve(inner, same_precedence)
	return eq[:start] + [res] + eq[stop+1:]


def doOperation(eq: list, add=True, mul=True) -> list:
	res = list()
	skip = 0
	changed = False

	for idx, elem in enumerate(eq):
		if skip > 0:
			skip -= 1
			continue

		if not changed:
			a, b, c = elem, eq[idx+1], eq[idx+2]

			if add and isinstance(a, int) and b in "+" and isinstance(c, int):
				res.append(a+c)
				changed = True
			if mul and isinstance(a, int) and b in "*" and isinstance(c, int):
				res.append(a*c)
				changed = True

			if changed:
				skip = 2
				continue

		res.append(elem)

	return res


def solve(eq: list, same_precedence: bool) -> int:
	while "(" in eq:
		eq = solveInner(eq, same_precedence)

	if same_precedence:
		while "+" in eq or "*" in eq:
			eq = doOperation(eq)
	else:
		while "+" in eq:
			eq = doOperation(eq, mul=False)
		while "*" in eq:
			eq = doOperation(eq, add=False)

	return eq[0]


with open("input.txt") as input_file:
	lines = [line.strip().split() for line in input_file]

eqations = [makeEquation(line) for line in lines]

print(f"Part 1: {sum([solve(e, same_precedence=True) for e in eqations])}")
print(f"Part 2: {sum([solve(e, same_precedence=False) for e in eqations])}")

###

end = time.time()
print(f"Runtime: {end - begin}")
