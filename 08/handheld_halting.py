import time
import re

begin = time.time()

###

class console:
	def __init__(self, prog):
		self.prog = prog
		self.length = len(prog)

		self.acc = 0
		self.pos = 0
		self.visited = set()

		self.halt = False
		self.term = False

	def execute(self) -> None:

		while not self.halt:
			if self.pos in self.visited:
				self.halt = True
				return

			if self.pos >= self.length:
				self.halt = True
				self.term = True
				return

			self.visited.add(self.pos)

			mode, value = self.prog[self.pos]

			if mode == "acc":
				self.acc += value
				self.pos += 1
				continue

			if mode == "jmp":
				self.pos += value
				continue

			if mode == "nop":
				self.pos += 1


with open("input.txt") as input_file:
	instructions = [line.split() for line in input_file]
	instructions = [(i[0], int(i[1])) for i in instructions]

c = console(instructions)
c.execute()
part1 = c.acc

interchange = {"jmp", "nop"}
for idx, instr in enumerate(instructions):
	if instr[0] in interchange:
		this, other = instr[0], interchange.difference({instr[0]}).pop()

		instructions[idx] = (other, instr[1])

		c = console(instructions)
		c.execute()

		instructions[idx] = (this, instr[1])

	if c.term:
			break


print(f"Part 1: {part1}")
print(f"Part 2: {c.acc}")

###

end = time.time()
print(f"Runtime: {end - begin}")
