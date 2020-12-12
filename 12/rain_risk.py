import time

begin = time.time()

###

DIRECTIONS = [(1,0),(0,-1),(-1,0),(0,1)]
CELESTIAL = {
	"E": (1,0),
	"S": (0,-1),
	"W": (-1,0),
	"N": (0,1)
}


def move(current: dict, instr: tuple) -> dict:
	action, v = instr

	if action in "NSWEF":
		x, y = DIRECTIONS[current["dir"]] if action == "F" else CELESTIAL[action]
		curr_x, curr_y = current["pos"]
		current["pos"] = (curr_x+x*v, curr_y+y*v)

	else:
		idx_change = v//90
		new_dir = current["dir"] + (idx_change if action == "R" else -idx_change)
		current["dir"] = new_dir%4

	return current


def rotate(wp: tuple, instr: tuple) -> tuple:
	x,y = wp
	action, v = instr
	steps = v//90
	for _ in range(steps):
		if action == "L":
			x, y = -y, x
		if action == "R":
			x, y = y, -x
	return (x,y)

def manhattan(point: tuple) -> int:
	return sum([abs(v) for v in point])

with open("input.txt") as input_file:
	instructions = [(line[0], int(line[1:])) for line in input_file]

#print(instructions)

status = {
	"pos": (0,0),
	"dir": 0
}

for i in instructions:
	status = move(status, i)

print(f"Part 1: {manhattan(status['pos'])}")

waypoint = (10,1)
position = (0,0)

for i in instructions:
	if i[0] == "F":
		movement = (waypoint[0]*i[1], waypoint[1]*i[1])
		position = (position[0]+movement[0], position[1]+movement[1])
	elif i[0] in "LR":
		waypoint = rotate(waypoint, i)
	else:
		tmp = {"pos": waypoint, "dir": 0}
		waypoint = move(tmp, i)["pos"]

print(f"Part 2: {manhattan(position)}")

###

end = time.time()
print(f"Runtime: {end - begin}")
