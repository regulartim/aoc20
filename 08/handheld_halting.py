import time
import re

begin = time.time()

###

class console:
	def __init__(self, prog):
		self.prog = prog
		self.length = len(prog)

		self.accumulator = 0
		self.pos = 0
		self.visited = set()

		self.halt = False
		self.term = False


	def acc(self, v: int) -> None:
		self.accumulator += v
		self.jmp(1)


	def jmp(self, v: int) -> None:
		self.pos += v


	def nop(self, v: int) -> None:
		self.jmp(1)


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
			getattr(self, mode)(value)


with open("input.txt") as input_file:
	instructions = [line.split() for line in input_file]
	instructions = [(i[0], int(i[1])) for i in instructions]

c = console(instructions)
c.execute()
part1 = c.accumulator

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
print(f"Part 2: {c.accumulator}")

###

end = time.time()
print(f"Runtime: {end - begin}")
