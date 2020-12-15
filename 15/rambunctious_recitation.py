import time

begin = time.time()

###

RAW_INPUT = "20,9,11,0,1,2"
starting_numbers = [int(n) for n in RAW_INPUT.split(",")]


def calculateNthNumber(n: int, numbers: list) -> int:
	d = dict()
	for idx, num in enumerate(numbers):
		d[num] = idx

	number = numbers[-1]
	for turn in range(len(numbers), n):

		has_been_spoken = number in d
		last_spoken = d.get(number, 0)

		d[number] = turn-1
		number = (turn-1) - last_spoken	if has_been_spoken else 0

	return number


print(f"Part 1: {calculateNthNumber(2020,starting_numbers)}")
print(f"Part 2: {calculateNthNumber(30000000,starting_numbers)}")

###

end = time.time()
print(f"Runtime: {end - begin}") 
