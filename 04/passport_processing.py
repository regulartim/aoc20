import time
import re

begin = time.time()

###

def isComplete(passport: dict) -> bool:
	if len(passport) == 8:
		return True

	if len(passport) == 7 and passport.get("cid") is None:
		return True

	return False

def isValid(passport: dict) -> bool:
	if not 1920 <= int(passport["byr"]) <= 2002:
		return False

	if not 2010 <= int(passport["iyr"]) <= 2020:
		return False

	if not 2020 <= int(passport["eyr"]) <= 2030:
		return False

	if passport["hgt"][-2:] not in {"cm", "in"}:
		return False

	if passport["hgt"][-2:] == "cm" and not 150 <= int(passport["hgt"][:-2]) <= 193:
		return False

	if passport["hgt"][-2:] == "in" and not 59 <= int(passport["hgt"][:-2]) <= 76:
		return False

	if not re.match("^#[0-9a-f]{6}$", passport["hcl"]):
		return False

	if passport["ecl"] not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
		return False

	if not re.match("^[0-9]{9}$", passport["pid"]):
		return False

	return True


passports = []
with open("input.txt") as input_file:
	for record in input_file.read().split("\n\n"):
		p = dict()
		for field in record.split():
			k, v = field.split(":")
			p[k] = v
		passports.append(p)

complete_passports = [p for p in passports if isComplete(p)]
valid_passports = [p for p in complete_passports if isValid(p)]

print(f"Part 1: {len(complete_passports)}")
print(f"Part 2: {len(valid_passports)}")

###

end = time.time()
print(f"Runtime: {end - begin}")
