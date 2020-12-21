import time

begin = time.time()

###

def product(l: list):
	p = 1
	for val in l:
		p = p * val
	return p


def getBorderId(border: list) -> int:
	res = list()
	for b in (border, reversed(border)):
		binary_list = [0 if char == "." else 1 for char in b]
		integer = int("".join(str(binary) for binary in binary_list), 2)
		res.append(integer)
	return min(res)


def getIds(tile: list) -> list:
	borders = [
		tile[0],
		[line[-1] for line in tile],
		tile[-1],
		[line[0] for line in tile]
	]
	return [getBorderId(b) for b in borders]

with open("input.txt") as input_file:
	blocks = input_file.read().split("\n\n")

TILES = dict()
for block in blocks:
	block = block.split("\n")
	key = block.pop(0).split()[1][:-1]
	key = int(key)
	value = [list(b) for b in block if b != ""]
	TILES[key] = value

border_ids = {k: getIds(t) for k, t in TILES.items()}

corners = list()
for k, v in border_ids.items():
	tile_counter = 0
	for bid in v:
		id_counter = 0
		for other in border_ids.values():
			if bid in other:
				id_counter += 1
		if id_counter == 1:
			tile_counter += 1
	if tile_counter == 2:
		corners.append(k)

print(corners)
print(f"Part 1: {product(corners)}")


###

end = time.time()
print(f"Runtime: {end - begin}")
