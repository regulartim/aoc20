import time 
import itertools

begin = time.time() 

###

def getSummands(l: list, result: int, n_summands: int) -> tuple:
	for tup in itertools.combinations(l, n_summands):
	 	if sum(tup) == result:
	 		return tup

with open("input.txt") as input_file:
	numbers = [int(line) for line in input_file]

a, b = getSummands(numbers, result=2020, n_summands=2)
print(f"Part 1: {a*b}")

a, b, c = getSummands(numbers, result=2020, n_summands=3)
print(f"Part 2: {a*b*c}")

###

end = time.time()
print(f"Runtime: {end - begin}")
