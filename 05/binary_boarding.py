import time

begin = time.time()

###

def narrowDown(position: tuple, instr: str) -> tuple:
	lower, upper = position
	move = int((upper - lower + 1) / 2)

	if instr in {"F", "L"}:
		upper -= move
	if instr in {"B", "R"}:
		lower += move

	return (lower, upper)


def findSeat(brdng_pass: str) -> dict:
	row = (0,127)
	seat = (0,7)

	for char in brdng_pass[:7]:
		row = narrowDown(row, char)

	for char in brdng_pass[7:]:
		seat = narrowDown(seat, char)

	return {"row": row[0], "seat": seat[0]}


def seatId(seat_pos: dict) -> int:
	return seat_pos["row"] * 8 + seat_pos["seat"]


def findFreeSeat(ids: list) -> int:
	prev = 0
	for sid in ids:
		if sid - prev == 2:
			return sid -1
		prev = sid


with open("input.txt") as input_file:
	passes = [line.strip() for line in input_file]

seats = [findSeat(p) for p in passes]
seat_ids = [seatId(s) for s in seats]

seat_ids = sorted(seat_ids)

print(f"Part 1: {seat_ids[-1]}")
print(f"Part 2: {findFreeSeat(seat_ids)}")

###

end = time.time()
print(f"Runtime: {end - begin}")
