import time

begin = time.time()

###

RAW_INPUT = "20,9,11,0,1,2"
starting_numbers = [int(n) for n in RAW_INPUT.split(",")]


def calculateNthNumber(n: int, numbers: list) -> int:
	d = dict()
	for idx, num in enumerate(numbers):
		d[num] = [idx]

	for turn in range(len(numbers), n):

		number = numbers[-1]
		spoken_in_turns = d[number]

		if len(spoken_in_turns) < 2:
			res = 0
		else:
			res = spoken_in_turns[-1] - spoken_in_turns[-2]

		numbers.append(res)
		d.setdefault(res,[]).append(turn)

	return numbers[-1]


print(f"Part 1: {calculateNthNumber(2020,starting_numbers)}")
print(f"Part 2: {calculateNthNumber(30000000,starting_numbers)}")

###

end = time.time()
print(f"Runtime: {end - begin}") 
