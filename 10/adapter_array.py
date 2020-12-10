import time
import itertools

begin = time.time()

###

# Found through testing:
# k = length of a sequence of 1-jolt differences
# v = number of valid arrangements
arrangements_per_one_seq = {
	0: 1,
	1: 1,
	2: 2,
	3: 4,
	4: 7,
	5: 13,
	6: 24,
	7: 44,
	8: 81,
	9: 149,
	10: 274,
	11: 504,
	12: 927,
	13: 1705,
	14: 3136,
	15: 5768,
	16: 10609,
	17: 19513,
	18: 35890
}


def getArrangements(seqs: list, d: dict) -> int:
	res = 1
	for s in seqs:
		res *= d[len(s)]
	return res


with open("input.txt") as input_file:
	adapters = sorted([int(line) for line in input_file])

j_out = [0] + adapters + [adapters[-1] +3]
diffs = [0] + [j - j_out[idx] for idx, j in enumerate(j_out[1:])]

one_seqences = "".join(str(n) for n in diffs[1:]).split("3")

print(f"Part 1: {diffs.count(1)*diffs.count(3)}")
print(f"Part 2: {getArrangements(one_seqences, arrangements_per_one_seq)}")

###

end = time.time()
print(f"Runtime: {end - begin}")
