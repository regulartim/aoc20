import time

begin = time.time()

###

RAW_INPUT = "20,9,11,0,1,2"
starting_numbers = [int(n) for n in RAW_INPUT.split(",")]


def calculateNthNumber(n: int, numbers: list) -> int:
	d = dict()
	for idx, num in enumerate(numbers):
		d[num] = [idx]

	number = numbers[-1]
	for turn in range(len(numbers), n):

		spoken_in_turns = d[number]

		if len(spoken_in_turns) < 2:
			number = 0
		else:
			number = spoken_in_turns[-1] - spoken_in_turns[-2]

		d.setdefault(number,[]).append(turn)

	return number


print(f"Part 1: {calculateNthNumber(2020,starting_numbers)}")
print(f"Part 2: {calculateNthNumber(30000000,starting_numbers)}")

###

end = time.time()
print(f"Runtime: {end - begin}") 
