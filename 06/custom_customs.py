import time

begin = time.time()

###

def getAnswerUnion(group: list) -> set:
	res = set()
	for elem in group:
		res.update(list(elem))
	return res

def getAnswerIntersection(group: list) -> set:
	res = set(group[0])
	for elem in group:
		res.intersection_update(list(elem))
	return res

def sumOfCounts(l: list) -> int:
	return sum((len(elem) for elem in l))

with open("input.txt") as input_file:
	groups = [block.split() for block in input_file.read().split("\n\n")]

answer_unions = [getAnswerUnion(g) for g in groups]
answer_intersects = [getAnswerIntersection(g) for g in groups]

print(f"Part 1: {sumOfCounts(answer_unions)}")
print(f"Part 2: {sumOfCounts(answer_intersects)}")

###

end = time.time()
print(f"Runtime: {end - begin}") 
