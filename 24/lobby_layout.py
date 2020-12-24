import time

begin = time.time()

###

DIRECTIONS = {
	"ne": (1,0,-1),
	"e": (1,-1,0),
	"se": (0,-1,1),
	"sw": (-1,0,1),
	"w": (-1,1,0),
	"nw": (0,1,-1)
}


def addTuples(t1: tuple, t2: tuple) -> tuple:
	res = list()
	for a, b in zip(t1,t2):
		res.append(a+b)
	return tuple(res)


def getTilePosition(instructions: str, start=(0,0,0)) -> tuple:
	if not instructions:
		return start

	if instructions[0] in {"e","w"}:
		di, instructions = instructions[0], instructions[1:]
	else:
		di, instructions = instructions[:2], instructions[2:]

	new_pos = addTuples(start, DIRECTIONS[di])
	return getTilePosition(instructions, new_pos)


def getNeighbours(tile: tuple) -> set:
	res = set()
	for adj in DIRECTIONS.values():
		res.add(addTuples(tile, adj))
	return res


def getNextDay(blacks: set) -> set:
	res = set()
	whites = set()

	for tile in blacks:
		neigbours = getNeighbours(tile)
		whites.update(neigbours)
		n_black_neighbours = len([n for n in neigbours if n in blacks])
		if 0 < n_black_neighbours < 3:
			res.add(tile)

	whites.difference_update(blacks)
	for tile in whites:
		neigbours = getNeighbours(tile)
		n_black_neighbours = len([n for n in neigbours if n in blacks])
		if n_black_neighbours == 2:
			res.add(tile)

	return res


with open("input.txt") as input_file:
	lines = [line.strip() for line in input_file]

black_tiles = set()
for line in lines:
	target = getTilePosition(line)
	if target in black_tiles:
		black_tiles.remove(target)
	else:
		black_tiles.add(target)

print(f"Part 1: {len(black_tiles)}")

for _ in range(100):
	black_tiles = getNextDay(black_tiles)

print(f"Part 2: {len(black_tiles)}")

###

end = time.time()
print(f"Runtime: {end - begin}")
