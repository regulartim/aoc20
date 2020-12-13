import time

begin = time.time()

###

DIRECTIONS = {
	"E": (1,0),
	"S": (0,-1),
	"W": (-1,0),
	"N": (0,1)
}


def movePoint(point: tuple, movement: tuple, factor: int) -> tuple:
	point_x, point_y = point
	move_x, move_y = movement
	point = point_x + move_x*factor, point_y + move_y*factor
	return point


def rotateShip(di: int, instr: tuple) -> int:
	action, v = instr
	idx_change = v//90
	di = di + (idx_change if action == "R" else -idx_change)
	return di % 4


def rotateWaypoint(point: tuple, instr: tuple) -> tuple:
	x, y = point
	action, v = instr
	steps = v//90

	for _ in range(steps):
		if action == "L":
			x, y = -y, x
		if action == "R":
			x, y = y, -x

	return x, y


def changeWaypoint(point: tuple, instr) -> tuple:
	action, v = instr
	if action in "LR":
		return rotateWaypoint(point, instr)

	movement = DIRECTIONS[action]
	return movePoint(point, movement, v)


def navigate1(point: tuple, di: int, instr: tuple) -> tuple:
	action, v = instr

	if action in "NSWEF":
		movement = DIRECTIONS[action] if action != "F" else list(DIRECTIONS.values())[di]
		point = movePoint(point, movement, v)

	else:
		di = rotateShip(di, instr)

	return point, di


def navigate2(point: tuple, wp: tuple, instr: tuple) -> tuple:
	action, v = instr
	if action == "F":
		point = movePoint(point, wp, v)
	else:
		wp = changeWaypoint(wp, instr)

	return point, wp


def manhattanDistance(point: tuple) -> int:
	return sum([abs(v) for v in point])


with open("input.txt") as input_file:
	instructions = [(line[0], int(line[1:])) for line in input_file]

p1_position, p2_position = (0,0), (0,0)
direction = 0
waypoint = (10,1)

for i in instructions:
	p1_position, direction = navigate1(p1_position, direction, i)
	p2_position, waypoint = navigate2(p2_position, waypoint, i)


print(f"Part 1: {manhattanDistance(p1_position)}")
print(f"Part 2: {manhattanDistance(p2_position)}")

###

end = time.time()
print(f"Runtime: {end - begin}")
