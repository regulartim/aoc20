import time

begin = time.time()

###

def getRemainderById(message: str, rule_id: str):
	if isinstance(RULES[rule_id], str):
		if message and message[0] == RULES[rule_id]:
			yield message[1:]

	else:
		for rule in RULES[rule_id]:
			yield from getRemainderBySeqence(message, rule)


def getRemainderBySeqence(message: str, sequence: tuple):
	if not sequence:
		yield message

	else:
		for remainder in getRemainderById(message, sequence[0]):
			yield from getRemainderBySeqence(remainder, sequence[1:])


def match(message: str, rule_id: str) -> bool:
	return "" in getRemainderById(message, rule_id)


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

messages = blocks[1].split("\n")[:-1]
matching_messages = [m for m in messages if match(m, "0")]

print(f"Part 1: {len(matching_messages)}")

RULES["8"].append(("42","8"))
RULES["11"].append(("42","11","31"))

matching_messages = [m for m in messages if match(m, "0")]

print(f"Part 2: {len(matching_messages)}")

###

end = time.time()
print(f"Runtime: {end - begin}")
