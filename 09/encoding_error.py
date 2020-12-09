import time
import itertools

begin = time.time()

###

def findInvalidNumber(l: list, n: int) -> int:
	for idx, elem in enumerate(l[n:]):
		for tup in itertools.combinations(l[idx:n+idx], 2):
			if sum(tup) == elem:
				break
		else:
			return elem

	return 0


def findContiguousSet(l: list, n: int) -> int:
	for idx, s in enumerate(l):
		res = [s]
		for successor in l[idx+1:]:
			res.append(successor)
			s += successor
			if s > n:
				break
			if s == n:
				return min(res) + max(res)
	return 0


with open("input.txt") as input_file:
	numbers = [int(line) for line in input_file]

n_to_consider = 25
invalid = findInvalidNumber(numbers, n_to_consider)

print(f"Part 1: {invalid}")
print(f"Part 2: {findContiguousSet(numbers, invalid)}")

###

end = time.time()
print(f"Runtime: {end - begin}")
