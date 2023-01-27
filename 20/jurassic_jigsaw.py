import re
import time

from collections import Counter

import numpy as np

begin = time.time()

###

DIRECTIONS = ["up", "left", "down", "right"]

def getBorderId(border: list) -> int:
	binary_list = [0 if char == "." else 1 for char in border]
	return int("".join(str(binary) for binary in binary_list), 2)

class Tile:
	def __init__(self, arg):
		match arg:
			case str():
				block = arg.split("\n")
				self.key = block.pop(0).split()[1][:-1]
				self.grid = np.array([list(b.strip()) for b in block if b != ""], dtype=object)
			case _:
				self.key = 0
				self.grid = arg
		self.neighbours = {d: None for d in DIRECTIONS}

	def __hash__(self):
		return hash(self.key)

	def without_borders(self):
		return self.grid[1:-1,1:-1]

	def permutations(self):
		for k in range(4):
			yield np.rot90(self.grid, k=k)
			yield np.fliplr(np.rot90(self.grid, k=k))

	def border_ids(self):
		borders = [self.grid[0], self.grid[:,0], self.grid[-1], self.grid[:,-1]]
		return {d: getBorderId(b) for b, d in zip(borders, DIRECTIONS)}

	def fix_orientation(self, direction, border_id):
		for p in self.permutations():
			directions = {"up": p[0], "left":p[:,0], "down": p[-1], "right": p[:,-1]}
			if getBorderId(directions[direction]) == border_id:
				self.grid = p
				return True
		return False

	def try_attach(self, other, direction):
		if self.neighbours[direction] or other == self:
			return False
		border_id = self.border_ids()[direction]
		dir_idx = DIRECTIONS.index(direction)
		other_direction = DIRECTIONS[(dir_idx+2)%4]
		success = other.fix_orientation(other_direction, border_id)
		if success:
			self.neighbours[direction] = other
			other.neighbours[other_direction] = self
		return success

	def get_root(self):
		if self.neighbours["up"]:
			return self.neighbours["up"].get_root()
		if self.neighbours["left"]:
			return self.neighbours["left"].get_root()
		return self

	def get_row_image(self):
		if not self.neighbours["right"]:
			return self.without_borders()
		return np.concatenate((self.without_borders(), self.neighbours["right"].get_row_image()), axis=1)

	def get_full_image(self):
		if not self.neighbours["down"]:
			return self.get_row_image()
		return np.concatenate((self.get_row_image(), self.neighbours["down"].get_full_image()), axis=0)

	def get_seamonster_pattern(self):
		grid_dimension = self.grid.shape[0]
		spacing = str(grid_dimension - 20)
		pattern = r"(?=(" \
				+ r"..................#." + ".{" + spacing + "}"\
				+ r"#....##....##....###" + ".{" + spacing + "}"\
				+ r".#..#..#..#..#..#..." + r"))"
		return re.compile(pattern)

	def get_roughness(self):
		seamonster = self.get_seamonster_pattern()
		for p in image.permutations():
			as_single_line = "".join(p.flatten())
			search_result = seamonster.findall(as_single_line)
			if search_result:
				return sum(char == "#" for char in image.grid.flatten()) - len(search_result) * 15


with open("input.txt") as input_file:
	blocks = input_file.read().split("\n\n")

tiles = [Tile(block) for block in blocks]

queue = [tiles[0]]
while queue:
 	current = queue.pop()
 	for t in tiles:
 		for d in DIRECTIONS:
 			if current.try_attach(t, d):
 				queue.append(t)
 				break

corners = [t for t in tiles if list(t.neighbours.values()).count(None) == 2]
image = Tile(tiles[0].get_root().get_full_image())

print(f"Part 1: {np.prod([int(tile.key) for tile in corners])}")
print(f"Part 2: {image.get_roughness()}")

###

end = time.time()
print(f"Runtime: {end - begin}")
