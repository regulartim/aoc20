import time
from sympy.ntheory.modular import crt

begin = time.time()

###

with open("input.txt") as input_file:
	lines = list(input_file)

current_time = int(lines[0])
busses_in_service = [int(elem) for elem in lines[1].split(",") if elem != "x"]

departs_in = {elem: elem - (current_time % elem) for elem in busses_in_service}
next_bus = min(departs_in.items(), key=lambda tup: tup[1])

depature_offset = [int(elem)-idx for idx, elem in enumerate(lines[1].split(",")) if elem != "x"]

print(f"Part 1: {next_bus[0] * next_bus[1]}")
print(f"Part 2: {crt(busses_in_service, depature_offset)[0]}")

###

end = time.time()
print(f"Runtime: {end - begin}")
