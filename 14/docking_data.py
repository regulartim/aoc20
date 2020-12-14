import time
import itertools

begin = time.time()

###

def toBinary(n: int, length=36) -> str:
	return "{0:b}".format(n).zfill(length)

def toDecimal(binary: str) -> int:
	return int(binary, 2)

def applyMaskToValue(binary: str, mask: str) -> str:
	res = ""
	for m_char, b_char in zip(mask, binary):
		res += b_char if m_char == "X" else m_char
	return res

def applyMaskToAddress(address: int, mask: str) -> str:
	res = ""
	for m_char, a_char in zip(mask, toBinary(address)):
		res += a_char if m_char == "0" else m_char
	return res

def getPossibleAdresses(address: int, mask: str):
	address = applyMaskToAddress(address, mask)
	floating = address.count("X")
	for tup in itertools.product("01", repeat=floating):
		res = address
		for n in tup:
			res = res.replace("X", n, 1)
		yield toDecimal(res)


def emulate(l: list, v2=False) -> int:
	mask = ""
	mem = dict()

	for line in l:
		if line[0] == "mask":
			mask = line[2]
			continue

		address = int(line[0][4:-1])
		value = int(line[2])

		if not v2:
			binary = toBinary(value)
			binary = applyMaskToValue(binary, mask)
			mem[address] = toDecimal(binary)
		else:
			for a in getPossibleAdresses(address, mask):
				mem[a] = value

	return sum(mem.values())


with open("input.txt") as input_file:
	lines = [line.split() for line in input_file]

print(f"Part 1: {emulate(lines)}")
print(f"Part 2: {emulate(lines, v2=True)}")

###

end = time.time()
print(f"Runtime: {end - begin}")
