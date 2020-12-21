import time

begin = time.time()

###

def getAllergensFromInput(l: list) -> tuple:
	allerg, ingr_count = dict(), dict()

	for line in l:
		line = line.split("(")
		ingredients = set(line[0].split())

		for a in line[1].split()[1:]:
			a =  a[:-1]
			allerg[a] = allerg[a].intersection(ingredients) if a in allerg else ingredients

		for i in ingredients:
			ingr_count[i] = ingr_count.get(i, 0) +1

	return allerg, ingr_count


def reduceDict(d: dict) -> dict:
	unique = set()
	while len(unique) < len(d):
		for v in d.values():
			if len(v) > 1:
				v.difference_update(unique)
			else:
				unique.update(v)
	return d


with open("input.txt") as input_file:
	lines = list(input_file)

allergens, ingredient_count = getAllergensFromInput(lines)

allergens = reduceDict(allergens)
all_ingredients = set(ingredient_count.keys())
canonical_dangerous_ingrediens = [v.pop() for _, v in sorted(allergens.items())]
non_allergen_ingredients = all_ingredients.difference(set(canonical_dangerous_ingrediens))

print(f"Part 1: {sum(ingredient_count[i] for i in non_allergen_ingredients)}")
print(f"Part 2: {','.join(canonical_dangerous_ingrediens)}")

###

end = time.time()
print(f"Runtime: {end - begin}")
