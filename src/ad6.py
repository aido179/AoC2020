from ad6_data import data
from typing import Set
from functools import reduce
# Part 1 - first attempt
def countAnswers_part1(input):
    running_total = 0
    question_groups = input.split("\n\n")
    for group in question_groups:
        answers:Set[str] = set()
        lines = group.split('\n')
        for line in lines:
            answers |= set(line)
        running_total += len(answers)
    return running_total

print(f"part 1: {countAnswers_part1(data)}")


# Part 2 - updated and made lovely.
def countAnswers(input, func):
    input_as_sets = [list(map(set, group.split('\n'))) for group in input.split("\n\n")]
    return sum(len(reduce(func, group)) for group in input_as_sets)

print(f"part 1: {countAnswers(data, set.union)}")
print(f"part 2: {countAnswers(data, set.intersection)}")

# part 1: 6443
# part 2: 3232
