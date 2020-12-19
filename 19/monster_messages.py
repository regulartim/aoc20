import time

begin = time.time()

###

def getPermutations(rule_id: str) -> set:
	res = set()

	rule = RULES[rule_id]
	if isinstance(rule, str):
		return set(rule)

	for tup in rule:
		perm = getPermutations(tup[0])
		for i in tup[1:]:
			tmp = set()
			for elem in getPermutations(i):
				for p in perm:
					s = p + elem
					tmp.add(s)

			perm = tmp

		res.update(perm)
	return res

def matches(message: str, rule_id: str) -> bool:
	return message in getPermutations(rule_id)

with open("input.txt") as input_file:
	blocks = input_file.read().split("\n\n")

RULES = dict()
for line in blocks[0].split("\n"):
	line = line.split(":")
	key, line = line[0], line[1].split("|")

	if len(line) > 1:
		value = [tuple(elem.split()) for elem in line]
	else:
		value = [tuple(line[0].split())]

	if value[0][0][0] == '"':
		value = value[0][0][1]

	RULES[key] = value

messages = [line for line in blocks[1].split("\n")[:-1]]


permutations = getPermutations("0")
print(f"Part 1: {len([m for m in messages if m in permutations])}")


exit()

RULES["8"].append(("42","8"))
RULES["11"].append(("42","11","31"))
permutations = getPermutations("0")
print(f"Part 2: {len([m for m in messages if m in permutations])}")

###

end = time.time()
print(f"Runtime: {end - begin}")
