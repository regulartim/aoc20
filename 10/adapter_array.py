import time

begin = time.time()

###

def arrangements(seq_len: int) -> int:
	if seq_len < 0:
		return 0
	if seq_len == 0:
		return 1
	return arrangements(seq_len-1) + arrangements(seq_len-2) + arrangements(seq_len-3)


def product(factors: list) -> int:
	res = 1
	for f in factors:
		res *= f
	return res


with open("input.txt") as input_file:
	adapters = sorted([int(line) for line in input_file])

j_out = [0] + adapters + [adapters[-1] +3]
diffs = [0] + [j - j_out[idx] for idx, j in enumerate(j_out[1:])]

one_seqences = "".join(str(n) for n in diffs[1:]).split("3")
arrangements_per_seq = [arrangements(len(seq)) for seq in one_seqences]

print(f"Part 1: {diffs.count(1) * diffs.count(3)}")
print(f"Part 2: {product(arrangements_per_seq)}")

###

end = time.time()
print(f"Runtime: {end - begin}")
