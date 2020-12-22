import time
from collections import deque
from itertools import islice
import copy

begin = time.time()

###

def oneIsEmpty(lists: list) -> bool:
	return any(len(l) == 0 for l in lists)


def calculateScore(l: list) -> int:
	factor = 1
	res = 0
	for n in reversed(l):
		res += n * factor
		factor += 1
	return res


def getRoundId(decks):
	res = str()
	for d in decks:
		res += str(d)
	return res


def normalCombat(decks):
	while not oneIsEmpty(decks):
		cards = [d.popleft() for d in decks]
		winner = 0 if cards[0] > cards[1] else 1
		decks[winner].append(cards.pop(winner))
		decks[winner].append(cards.pop(0))
	return winner, calculateScore(decks[winner])


def recursiveCombat(decks):
	previous = set()
	while not oneIsEmpty(decks):
		roundId = getRoundId(decks)
		if roundId in previous:
			return 0, calculateScore(decks[0])
		previous.add(roundId)

		cards = [d.popleft() for d in decks]

		if cards[0] <= len(decks[0]) and cards[1] <= len(decks[1]):
			recursionDecks = [deque(islice(d, 0, card)) for d, card in zip(decks,cards)]
			winner, _ = recursiveCombat(recursionDecks)

		else:
			winner = 0 if cards[0] > cards[1] else 1

		decks[winner].append(cards.pop(winner))
		decks[winner].append(cards.pop(0))

	return winner, calculateScore(decks[winner])


with open("input.txt") as input_file:
	blocks = input_file.read().split("\n\n")

player_decks = []
for block in blocks:
	deck = deque()
	for line in block.split("\n"):
		if line and "Player" not in line:
			deck.append(int(line))
	player_decks.append(deck)

copy = copy.deepcopy(player_decks)

print(f"Part 1: {normalCombat(player_decks)[1]}")
print(f"Part 2: {recursiveCombat(copy)[1]}")

###

end = time.time()
print(f"Runtime: {end - begin}")
