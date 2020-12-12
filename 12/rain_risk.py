import time

begin = time.time()

###

DIRECTIONS = {
	"E": (1,0),
	"S": (0,-1),
	"W": (-1,0),
	"N": (0,1)
}


def move(point: tuple, di: int, instr: tuple) -> tuple:
	action, v = instr

	if action in "NSWEF":
		x, y = DIRECTIONS[action] if action != "F" else list(DIRECTIONS.values())[di]
		curr_x, curr_y = point
		point = (curr_x+x*v, curr_y+y*v)

	else:
		idx_change = v//90
		new_dir = di + (idx_change if action == "R" else -idx_change)
		di = new_dir % 4

	return point, di


def rotate(point: tuple, instr: tuple) -> tuple:

	x, y = point
	action, v = instr
	steps = v//90

	for _ in range(steps):
		if action == "L":
			x, y = -y, x
		if action == "R":
			x, y = y, -x

	return x, y


def moveWaypoint(point: tuple, instr) -> tuple:
	action, _ = instr
	if action in "LR":
		return rotate(point, instr)
	return move(point, 0, instr)[0]


def movePartTwo(point: tuple, wp: tuple, instr: tuple) -> tuple:
	action, v = instr
	if action == "F":
		point = (point[0] + wp[0]*v), (point[1] + wp[1]*v)
	else:
		wp = moveWaypoint(wp, instr)

	return point, wp


def manhattanDistance(point: tuple) -> int:
	return sum([abs(v) for v in point])


with open("input.txt") as input_file:
	instructions = [(line[0], int(line[1:])) for line in input_file]

p1_position, p2_position = (0,0), (0,0)
direction = 0
waypoint = (10,1)

for i in instructions:
	p1_position, direction = move(p1_position, direction, i)
	p2_position, waypoint = movePartTwo(p2_position, waypoint, i)


print(f"Part 1: {manhattanDistance(p1_position)}")
print(f"Part 2: {manhattanDistance(p2_position)}")

###

end = time.time()
print(f"Runtime: {end - begin}")
