import time
import itertools

begin = time.time()

###

def isValidP1(pw: dict) -> bool:
	occ = pw["pw"].count(pw["letter"])
	return pw["min"] <= occ <= pw["max"]

def isValidP2(pw: dict) -> bool:
	lst = [0] + list(pw["pw"])
	return (lst[pw["min"]] == pw["letter"]) != (lst[pw["max"]] == pw["letter"])


pw_data = []
with open("input.txt") as input_file:
	for line in input_file:
		line = line.split()
		pw_data.append({
			"pw": line[-1],
			"letter": line[-2][:-1],
			"min": int(line[0].split("-")[0]),
			"max": int(line[0].split("-")[1])
			})

part1, part2 = 0, 0
for pw in pw_data:
	if isValidP1(pw):
		part1 += 1
	if isValidP2(pw):
		part2 += 1

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

###

end = time.time()
print(f"Runtime: {end - begin}") 
