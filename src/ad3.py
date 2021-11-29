from ad3_data import grid

# Part 1
#Trees encountered following slope: right 3; down 1

def count_trees_for_slope(grid, inc_right, inc_down):
    curr_x = 0
    tree_count = 0
    for curr_y in range(0, len(grid), inc_down):
        if curr_y != 0:
            curr_x = (curr_x + inc_right) % len(grid[curr_y])
        if grid[curr_y][curr_x] == "#":
            tree_count += 1
    return tree_count

print("part 1")
print(count_trees_for_slope(grid, 3, 1))

# Part 2

"""
Right 1, down 1.
Right 3, down 1.
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
"""
a = count_trees_for_slope(grid, 1, 1)
b = count_trees_for_slope(grid, 3, 1)
c = count_trees_for_slope(grid, 5, 1)
d = count_trees_for_slope(grid, 7, 1)
e = count_trees_for_slope(grid, 1, 2)
print("part 2")
print(a*b*c*d*e)

test_grid_1 = """....1
....2
.#..3
....4
..#.5""".split("\n")
tg1 = count_trees_for_slope(test_grid_1, 1, 2)
print(tg1)
