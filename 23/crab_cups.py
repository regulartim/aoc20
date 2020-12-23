
import time

begin = time.time()

###

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
		self.pickup = None

		for value in l:
			if self.current is None:
				n = node(value)
				n.next_node = n
				self.current = n
				self.last = n
				self.lookup[value] = n
			else:
				self.insert(value, self.last.value)

	def insert(self, value, predecessor):
		n = node(value)
		pred = self.lookup[predecessor]
		n.next_node = pred.next_node
		pred.next_node = n
		if pred == self.last:
			self.last = n
		self.lookup[value] = n

	def append(self, value):
		self.insert(value, self.last.value)

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

	def rotate(self, steps: int):
		for _ in range(steps):
			self.current = self.current.next_node
			self.last = self.last.next_node

	def pushToPickup(self, predecessor, n=3):
		pred = self.lookup[predecessor]
		self.pickup = pred.next_node
		for _ in range(n):
			pred.next_node = pred.next_node.next_node

	def insertPickup(self, predecessor, n=3):
		pred = self.lookup[predecessor]
		last_pickup = self.pickup
		for _ in range(n-1):
			last_pickup = last_pickup.next_node
		last_pickup.next_node = pred.next_node
		pred.next_node = self.pickup
		if pred == self.last:
			self.last = last_pickup
		self.pickup = None

	def getPickup(self, n=3) -> set:
		res = set()
		if self.pickup is None:
			return res
		elem = self.pickup
		for _ in range(n):
			res.add(elem.value)
			elem = elem.next_node
		return res

	def getList(self) -> list:
		res = list()
		n = self.current
		res.append(n.value)
		while n != self.last:
			n = n.next_node
			res.append(n.value)
		return res

	def maxValue(self) -> int:
		return max(self.lookup.keys())

	def isEmpty(self) -> bool:
		return self.current is None



def play(cups: circularlist, moves: int) -> list:

	highest_value = cups.maxValue()

	for _ in range(moves):

		current = cups.current.value
		cups.pushToPickup(predecessor=current)
		cups.rotate(1)

		pick_up = cups.getPickup()

		destination = current -1 if current > 1 else highest_value
		while destination in pick_up:
			destination = destination -1 if destination > 1 else highest_value

		cups.insertPickup(predecessor=destination)

	return cups


def getResultString(q: circularlist) -> str:
	while q.current.value != 1:
		q.rotate(1)

	res = ""
	while not q.isEmpty():
		res += str(q.popleft())

	return res[1:]


def getP2Result(q: circularlist) -> int:
	while q.current.value != 1:
		q.rotate(1)

	return q.current.next_node.value * q.current.next_node.next_node.value


cup_list_p1 = circularlist([int(n) for n in RAW_INPUT])
cup_list_p1 = play(cup_list_p1, moves=100)

cup_list_p2 = circularlist([int(n) for n in RAW_INPUT])

for i in range(9, 1000000):
	cup_list_p2.append(i+1)

cup_list_p2 = play(cup_list_p2, moves=10000000)

print(f"Part 1: {getResultString(cup_list_p1)}")
print(f"Part 2: {getP2Result(cup_list_p2)}")

###

end = time.time()
print(f"Runtime: {end - begin}")
