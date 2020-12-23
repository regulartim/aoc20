
import time

begin = time.time()

###

RAW_INPUT = "389125467"
RAW_INPUT = "789465123"


class node:

	def __init__(self, value):
		self.value = value
		self.next_node = None


class circularlist:

	def __init__(self, l: list):
		self.lookup = dict()
		self.current = None
		self.last = None

		for value in l:
			if self.current is None:
				n = node(value)
				n.next_node = n
				self.current = n
				self.last = n
				self.lookup[value] = n
			else:
				self.insert(value, self.last.value)

	def rotate(self, steps: int):
		for _ in range(steps):
			self.current = self.current.next_node
			self.last = self.last.next_node

	def popleft(self):
		res = self.current.value
		self.last.next_node = self.current.next_node
		if self.current == self.current.next_node:
			self.current = None
			self.last = None
		else:
			self.current = self.current.next_node
		self.lookup.pop(res)
		return res

	def insert(self, value, behind):
		n = node(value)
		pred = self.lookup[behind]
		n.next_node = pred.next_node
		pred.next_node = n
		if pred == self.last:
			self.last = n
		self.lookup[value] = n

	def isEmpty(self):
		return self.current is None




def play(cups: circularlist, moves: int) -> list:

	highest_value = 9

	for _ in range(moves):

		current = cups.current.value
		cups.rotate(1)

		pick_up = [cups.popleft() for _ in range(3)]

		destination = current -1 if current > 1 else highest_value
		while destination in pick_up:
			destination = destination -1 if destination > 1 else highest_value

		#destination_idx = cups.index(destination)

		for p in reversed(pick_up):
			cups.insert(p, behind=destination)


	return cups


def getResultString(q: list) -> str:
	while q.current.value != 1:
		q.rotate(1)

	res = ""
	while not q.isEmpty():
		res += str(q.popleft())

	return res[1:]


def getP2Result(q: list) -> int:
	while q[0] != 1:
		q.rotate(1)

	return q[1] * q[2]


cup_list_p1 = circularlist([int(n) for n in RAW_INPUT])
#cup_list_p2 = deque([int(n) for n in RAW_INPUT])

#for i in range(len(cup_list_p2), 1000000):
#	cup_list_p2.append(i+1)

cup_list_p1 = play(cup_list_p1, moves=100)
#cup_list_p2 = play(cup_list_p2, moves=100)

print(f"Part 1: {getResultString(cup_list_p1)}")
#print(f"Part 2: {getP2Result(cup_list_p2)}")

###

end = time.time()
print(f"Runtime: {end - begin}")
