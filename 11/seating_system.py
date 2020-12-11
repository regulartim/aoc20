import time

begin = time.time()

###

seat_map = {
	"floor": set(),
	"empty": set(),
	"occupied": set(),
	"history": [0]
}

neighbourhood = {(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)}


def getAdjacents(point: tuple, floor: set, part2: bool) -> list:
	if not part2:
		return [(point[0]+a, point[1]+b) for a, b in neighbourhood]

	res = []
	for a, b in neighbourhood:
		neighbour = (point[0]+a, point[1]+b)
		while neighbour in floor:
			neighbour = (neighbour[0]+a, neighbour[1]+b)
		res.append(neighbour)
	return res


def buildAdjMap(d: dict, part2: bool) -> dict:
	seats = d["empty"]
	return {seat: getAdjacents(seat, d["floor"], part2) for seat in seats}


def getNextState(d: dict, adjacencies: dict, part2: bool) -> dict:
	empty, occupied = set(), set()

	for seat in d["empty"]:
		for a in adjacencies[seat]:
			if a in d["occupied"]:
				empty.add(seat)
				break
		else:
			occupied.add(seat)

	for seat in d["occupied"]:
		occupied_adjacents = [a for a in adjacencies[seat] if a in d["occupied"]]
		if len(occupied_adjacents) < (5 if part2 else 4):
			occupied.add(seat)
		else:
			empty.add(seat)

	return {
		"floor": d["floor"],
		"empty": empty,
		"occupied": occupied,
		"history": d["history"] + [len(occupied)]
	}


def hasStabilised(history: list) -> bool:
	if len(history) < 2:
		return False

	if len(set(history[-2:])) > 1:
		return False

	return True


with open("input.txt") as input_file:
	for y, line in enumerate(input_file):
		for x, char in enumerate(line):
			pos = (x,y)
			if char == ".":
				seat_map["floor"].add(pos)
			if char == "L":
				seat_map["empty"].add(pos)

for part in (1, 2):
	state = seat_map
	adjacency_map = buildAdjMap(seat_map, part2=(part==2))

	while not hasStabilised(state["history"]):
		state = getNextState(state, adjacency_map, part2=(part==2))
	print(f"Part {part}: {state['history'][-1]}")

###

end = time.time()
print(f"Runtime: {end - begin}")
