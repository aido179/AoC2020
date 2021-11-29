from ad2_data import lines
# eg line: ['10-16', 'w', 'hkhwvvwztwwwwgdb']
counter = 0
for line in lines:
    letter = line[1]
    string = line[2]
    min_cnt = int(line[0].split("-")[0])
    max_cnt = int(line[0].split("-")[1])
    letter_cnt = string.count(letter)
    if letter_cnt >= min_cnt and letter_cnt <= max_cnt:
        counter += 1

print("part 1")
print(counter)


counter = 0
for line in lines:
    letter = line[1]
    string = line[2]
    pos1 = int(line[0].split("-")[0]) - 1
    pos2 = int(line[0].split("-")[1]) - 1
    if (string[pos1] == letter or string[pos2] == letter) and string[pos1] != string[pos2]:
        counter += 1

print("part 2")
print(counter)
