import time
from collections import deque
from itertools import islice
import copy

begin = time.time()

###

def oneIsEmpty(lists: list) -> bool:
	return any(len(l) == 0 for l in lists)


def calculateScore(l: list) -> int:
	return sum([idx * n for idx, n in enumerate(reversed(l) ,1)])


def getRoundId(decks: list) -> str:
	res = str()
	for d in decks:
		res += str(d)
	return res


def normalCombat(decks: list) -> tuple:
	while not oneIsEmpty(decks):
		cards = [d.popleft() for d in decks]
		winner = 0 if cards[0] > cards[1] else 1
		decks[winner].append(cards.pop(winner))
		decks[winner].append(cards.pop(0))
	return winner, decks[winner]


def recursiveCombat(decks: list) -> tuple:
	previous = set()
	while not oneIsEmpty(decks):

		roundId = getRoundId(decks)
		if roundId in previous:
			return 0, decks[0]

		previous.add(roundId)

		cards = [d.popleft() for d in decks]

		if cards[0] <= len(decks[0]) and cards[1] <= len(decks[1]):
			recursionDecks = [deque(islice(d, 0, card)) for d, card in zip(decks,cards)]
			winner, _ = recursiveCombat(recursionDecks)

		else:
			winner = 0 if cards[0] > cards[1] else 1

		decks[winner].append(cards.pop(winner))
		decks[winner].append(cards.pop(0))

	return winner, decks[winner]


with open("input.txt") as input_file:
	blocks = input_file.read().split("\n\n")

player_decks = []
for block in blocks:
	deck = deque()
	for line in block.split("\n"):
		if line and "Player" not in line:
			deck.append(int(line))
	player_decks.append(deck)

decks_copy = copy.deepcopy(player_decks)

print(f"Part 1: {calculateScore(normalCombat(player_decks)[1])}")
print(f"Part 2: {calculateScore(recursiveCombat(decks_copy)[1])}")

###

end = time.time()
print(f"Runtime: {end - begin}")
