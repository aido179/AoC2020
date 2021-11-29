from ad1_data import nums
import timeit
"""
...the Elves in accounting just need you to fix your expense report (your puzzle
input); apparently, something isn't quite adding up.
Specifically, they need you to find the two entries that sum to 2020 and then
multiply those two numbers together.

For example, suppose your expense report contained the following:
1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying
them together produces 1721 * 299 = 514579, so the correct answer is 514579.
"""

def search(nums):
    for i, val in enumerate(nums):
        search_list = nums[i:]
        curr_val = search_list[0]
        search_val = 2020-curr_val
        try:
            return search_list[search_list.index(search_val)] * curr_val
        except ValueError:
            pass
    print("oops not found")
    return False

print('Part 1')
print(timeit.timeit('search(nums)', globals=globals(), number = 100))
print(search(nums))

"""
Using the above example again, the three entries that sum to 2020 are 979, 366,
and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to
2020?
"""


def search2_offset(nums, curr_first_num):
    for i, val in enumerate(nums):
        search_list = nums[i:]
        curr_val = search_list[0]
        search_val = (2020-curr_first_num)-curr_val
        try:
            return search_list[search_list.index(search_val)] * curr_val
        except ValueError:
            pass
    return False

def search2(nums):
    for i, val in enumerate(nums):
        search_list = nums[i:]
        curr_val = search_list[0]
        search_result = search2_offset(search_list, curr_val)
        if search_result:
            return search_result * curr_val

print('Part 2')
print(timeit.timeit('search2(nums)', globals=globals(), number = 100))
print(search2(nums))
