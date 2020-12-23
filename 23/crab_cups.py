
import time
from collections import deque

begin = time.time()

###

RAW_INPUT = "789465123"


def play(cups: list, moves: int) -> list:

	highest_value = max(cups)

	for _ in range(moves):

		current = cups[0]
		cups.rotate(-1)

		pick_up = [cups.popleft() for _ in range(3)]

		destination = current -1 if current > 1 else highest_value
		while destination in pick_up:
			destination = destination -1 if destination > 1 else highest_value

		destination_idx = cups.index(destination)

		for p in reversed(pick_up):
			cups.insert(destination_idx+1, p)


	return cups


def getResultString(q: list) -> str:
	while q[0] != 1:
		q.rotate(1)

	res = ""
	while q:
		res += str(q.popleft())

	return res[1:]


def getP2Result(q: list) -> int:
	while q[0] != 1:
		q.rotate(1)

	return q[1] * q[2]


cup_list_p1 = deque([int(n) for n in RAW_INPUT])
#cup_list_p2 = deque([int(n) for n in RAW_INPUT])

#for i in range(len(cup_list_p2), 1000000):
#	cup_list_p2.append(i+1)

cup_list_p1 = play(cup_list_p1, moves=100)
#cup_list_p2 = play(cup_list_p2, moves=100)

print(f"Part 1: {getResultString(cup_list_p1)}")
#print(f"Part 2: {getP2Result(cup_list_p2)}")

###

end = time.time()
print(f"Runtime: {end - begin}")
