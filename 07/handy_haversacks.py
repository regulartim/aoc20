import time
import re

begin = time.time()

###

def getBagInfo(bag: str) -> dict:
	bag = bag.split()
	qty = int(bag[0])
	color = " ".join(bag[1:3])
	return {"color": color, "qty": qty}


def buildDict(lst: list) -> dict:
	res = dict()
	for l in lst:
		bag = " ".join(l.pop(0).split()[:2])
		content = [getBagInfo(bag) for bag in l if bag.strip()[:2] != "no"]
		res[bag] = content
	return res


def getPossibleBags(containing: str, d: dict) -> set:
	res = set()
	for k, v in d.items():
		if containing in {bag["color"] for bag in v}:
			res.add(k)
			res.update(getPossibleBags(containing=k, d=d))
	return res


def countBagsInside(bag: str, d: dict) -> int:
	res = 0
	for b in d[bag]:
		color, qty = b["color"], b["qty"]
		if d[color] is None:
			continue
		res += qty + qty * countBagsInside(color, d)
	return res


with open("input.txt") as input_file:
	lines = [re.split("contain|,", line) for line in input_file]

contents = buildDict(lines)

print(f"Part 1: {len(getPossibleBags(containing='shiny gold', d=contents))}")
print(f"Part 2: {countBagsInside('shiny gold', contents)}")

###

end = time.time()
print(f"Runtime: {end - begin}")
