from ad5_data import boarding_passes
import math
# Part 1
def binary_space_partition(input_string, front="F", back="B", space_size=128):
    if 2**len(input_string) != space_size:
        raise ValueError(f"Input_string and space_size do not match: {len(input_string)}, {math.sqrt(space_size)}")
    curr_min = 0
    curr_max = space_size
    for dir in input_string:
        offset = ((curr_max - curr_min) / 2)
        if dir == front:
            curr_max = curr_max - offset
        if dir == back:
            curr_min = curr_min + offset
    return int(curr_min)

# print(f" --- {binary_space_partition('BFFFBBF')}") #70
# print(f" --- {binary_space_partition('FFFBBBF')}") #14
# print(f" --- {binary_space_partition('BBFFBBF')}") #102

def getSeatID(row, column):
    return (row*8)+column

def boardingpassToSeatId(bp):
    row_part = bp[:7]
    col_part = bp[7:]
    row = binary_space_partition(row_part)
    col = binary_space_partition(col_part, front="L", back="R", space_size=8)
    return getSeatID(row, col)

max_seat_id = 0
for bp in boarding_passes:
    max_seat_id = max(max_seat_id, boardingpassToSeatId(bp))

print(f"part 1: {max_seat_id}")

# part 2

seat_ids = [boardingpassToSeatId(bp) for bp in boarding_passes]
seat_ids.sort()
for i, id in enumerate(seat_ids):
    if seat_ids[i+1] != (id+1):
        print(f"part 2: {id+1}")
        break
