import time

begin = time.time()

###

ALLOCATION = {
	"F": "0",
	"B": "1",
	"L": "0",
	"R": "1"
}


def parseSeatId(brdng_pass: str) -> int:
	binary = (ALLOCATION[char] for char in list(brdng_pass))
	return int("".join(binary), 2)


def findFreeSeat(ids: list) -> int:
	prev = 0
	for sid in ids:
		if sid - prev == 2:
			return sid -1
		prev = sid


with open("input.txt") as input_file:
	passes = [line.strip() for line in input_file]

seat_ids = [parseSeatId(p) for p in passes]
seat_ids = sorted(seat_ids)

print(f"Part 1: {seat_ids[-1]}")
print(f"Part 2: {findFreeSeat(seat_ids)}")

###

end = time.time()
print(f"Runtime: {end - begin}")
