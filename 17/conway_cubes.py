import time
import itertools

begin = time.time()

###

NEIGHBOUTHOOD = dict()

NEIGHBOUTHOOD[4] = set(itertools.product([-1,0,1], repeat=4))
NEIGHBOUTHOOD[4].remove((0,0,0,0))

NEIGHBOUTHOOD[3] = set((a,b,c,0) for a,b,c,d in NEIGHBOUTHOOD[4])
NEIGHBOUTHOOD[3].remove((0,0,0,0))


def getNeighbours(point: tuple, dim: int) -> set:
	res = set()
	px, py, pz, pw = point
	for nx, ny, nz, nw in NEIGHBOUTHOOD[dim]:
		res.add((px+nx, py+ny, pz+nz, pw+nw))
	return res


def countActiveNeighbours(point: tuple, actives: set, dim: int) -> int:
	return len([n for n in getNeighbours(point, dim) if n in actives])


def cycle(actives: set, dim: int) -> set:

	res = set()
	inactives = set()

	for cube in actives:
		inactives.update(getNeighbours(cube, dim))
		if 2 <= countActiveNeighbours(cube, actives, dim) <= 3:
			res.add(cube)

	inactives.difference_update(actives)

	for cube in inactives:
		if countActiveNeighbours(cube, actives, dim) == 3:
			res.add(cube)
	return res


def runSimulation(actives: set, dimensions: int, cycles=6):
	for _ in range(cycles):
		actives = cycle(actives, dimensions)
	return len(actives)


initial_actives = set()
with open("input.txt") as input_file:
	for y, line in enumerate(input_file):
		for x, char in enumerate(line):
			if char == "#":
				initial_actives.add((x,y,0,0))

print(f"Part 1: {runSimulation(initial_actives,3)}")
print(f"Part 2: {runSimulation(initial_actives,4)}")

###

end = time.time()
print(f"Runtime: {end - begin}")
