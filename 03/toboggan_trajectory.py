import time

begin = time.time()

###

def getNextCoord(current: tuple, movement: tuple, w: int) -> tuple:
	a, b = current
	r, d = movement
	return ((a+r)%w, b+d)

def product(l: list):
	p = 1
	for val in l:
		p = p * val
	return p

trees = set()
with open("input.txt") as input_file:
	for y, line in enumerate(input_file):
		length, width = y+1, len(line)-1
		for x, char in enumerate(line):
			if char == "#":
				trees.add((x,y))

slopes = {
			(1,1): 0,
			(3,1): 0,
			(5,1): 0,
			(7,1): 0,
			(1,2): 0
		}

for k, v in slopes.items():
	pos = (0,0)
	counter = 0
	while pos[1] <= length:
		pos = getNextCoord(pos, k, width)
		if pos in trees:
			counter += 1
	slopes[k] = counter

print(f"Part 1: {slopes[(3,1)]}")
print(f"Part 2: {product(slopes.values())}")

###

end = time.time()
print(f"Runtime: {end - begin}")
