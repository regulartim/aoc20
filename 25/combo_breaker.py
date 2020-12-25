import time

begin = time.time()

###

PUB_KEYS = (8458505, 16050997)


def transformSubjectNumber(v: int, sn: int) -> int:
	v = v * sn
	return v % 20201227


def findLoopSize(key: int) -> int:	
		iterations, v = 0, 1
		while v != key:
			v = transformSubjectNumber(v, 7)
			iterations += 1
		return iterations


def getEncKey(key, loops):
	v = 1
	for _ in range(loops):
		v = transformSubjectNumber(v, key)
	return v


loop_sizes = tuple(findLoopSize(k) for k in PUB_KEYS)
encryption_key = getEncKey(PUB_KEYS[0], loop_sizes[1])

print(f"Part 1: {encryption_key}")
print(f"Part 2: ???")

###

end = time.time()
print(f"Runtime: {end - begin}")
