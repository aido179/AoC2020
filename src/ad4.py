from ad4_data import passports
import re

# Part 1
required_fields = ['byr',
'iyr',
'eyr',
'hgt',
'hcl',
'ecl',
'pid']
valid_count = 0
for pspt in passports:
    fields = list(map(lambda f: f[:3], re.split(' |\n',pspt)))
    if all(elem in fields for elem in required_fields):
        valid_count += 1
print('part 1')
print(valid_count)


# Part 2 - add validation
"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""
def hgt_validator(hgt):
    if hgt[-2:] == 'cm':
        v = hgt[:-2]
        return (int(v) >= 150 and int(v) <=193)
    if hgt[-2:] == 'in':
        v = hgt[:-2]
        return (int(v) >= 59 and int(v) <=76)
    return False

def hcl_validator(hgt):
    m = re.compile('^#[\da-f]{6}$')
    return m.match(hgt)

def ecl_validator(ecl):
    m = re.compile('^amb|blu|brn|gry|grn|hzl|oth$')
    return m.match(ecl)

def pid_validator(pid):
    m = re.compile('^\d{9}$')
    return m.match(pid)

field_validators = {
    'byr': lambda byr: (int(byr) >= 1920 and int(byr) <=2002),
    'iyr': lambda iyr: (int(iyr) >= 2010 and int(iyr) <=2020),
    'eyr': lambda eyr: (int(eyr) >= 2020 and int(eyr) <=2030),
    'hgt': hgt_validator,
    'hcl': hcl_validator,
    'ecl': ecl_validator,
    'pid': pid_validator,
    'cid': lambda _: True
}

valid_count = 0
for pspt in passports:
    fields = re.split(' |\n',pspt)
    field_names = list(map(lambda f: f[:3], fields))
    if all(elem in field_names for elem in required_fields) and all(field_validators[field_names[ind]](field[4:]) for ind, field in enumerate(fields)):
        valid_count += 1

print('part 2')
print(valid_count)
