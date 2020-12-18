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

def solve(eqation: list, part2=False) -> int:
	res = list()
	skip = 0
	changed = False

	for idx, elem in enumerate(eqation):
		if skip > 0:
			skip -= 1
			continue

		if not changed:
			try:
				a, b, c = elem, eqation[idx+1], eqation[idx+2]
				if a == "(" and c == ")":
					res.append(b)
					skip = 2
					changed = True
					continue

				if isinstance(a, int) and b in "+" and isinstance(c, int):
					res.append(a+c)
					skip = 2
					changed = True
					continue

				if not part2 and isinstance(a, int) and b in "*" and isinstance(c, int):
					res.append(a*c)
					skip = 2
					changed = True
					continue
			except:
				pass
		res.append(elem)
	
	if part2 and not changed:
		res = list()
		skip = 0
		for idx, elem in enumerate(eqation):
			if skip > 0:
				skip -= 1
				continue
			if not changed:
				a, b, c = elem, eqation[idx+1], eqation[idx+2]
				if isinstance(a, int) and b in "*" and isinstance(c, int):
					res.append(a*c)
					skip = 2
					changed = True
					continue
			res.append(elem)

		
	#print(res)
	if len(res) > 1:
		return solve(res, part2)

	return res[0]

def solveInner(eq):
	for idx, char in enumerate(eq):
		if char == "(":
			start = idx
		if char == ")":
			stop = idx
			break
	inner = eq[start+1:stop]
	res = solveOuter(inner)
	return eq[:start] + [res] + eq[stop+1:]

def doAddition(eq):
	res = list()
	skip = 0
	changed = False

	for idx, elem in enumerate(eq):
		if skip > 0:
			skip -= 1
			continue

		if not changed:
			a, b, c = elem, eq[idx+1], eq[idx+2]
			if isinstance(a, int) and b in "+" and isinstance(c, int):
				res.append(a+c)
				skip = 2
				changed = True
				continue

		res.append(elem)
	return res

def doMultiplication(eq):
	res = list()
	skip = 0
	changed = False

	for idx, elem in enumerate(eq):
		if skip > 0:
			skip -= 1
			continue

		if not changed:
			a, b, c = elem, eq[idx+1], eq[idx+2]
			if isinstance(a, int) and b in "*" and isinstance(c, int):
				res.append(a*c)
				skip = 2
				changed = True
				continue

		res.append(elem)
	return res

def solveOuter(eq: list):
	while "(" in eq:
		eq = solveInner(eq)
	while "+" in eq:
		eq = doAddition(eq)
	while "*" in eq:
		eq = doMultiplication(eq)
	return eq[0]





with open("input.txt") as input_file:
	lines = [line.strip().split() for line in input_file]

eqations = [makeEquation(line) for line in lines]
solutions = [solveOuter(e) for e in eqations]


print(f"Part 1: {sum([solve(e) for e in eqations])}")
print(f"Part 2: {sum([solveOuter(e) for e in eqations])}")

###

end = time.time()
print(f"Runtime: {end - begin}")
