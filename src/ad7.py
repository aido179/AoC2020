from ad7_data import data
from typing import Set, Dict, List, Tuple

#Part 1
rows = data.split("\n")

class Bag:

    def __init__(self, name):
        self.name = name
        self.contains:Dict[str, int] = {}
        self.contained_by:Set[str] = set()

    def addContainer(self, bag_name):
        self.contained_by.add(bag_name)

    def addContent(self, qty, bag_name):
        self.contains[bag_name] = int(qty)
#shiny olive bags contain 3 dim indigo bags, 3 wavy maroon bags.
def getContainedBags(line):
    contents = line.split(" ")[4:]
    output:List[Tuple[int, str]] = []
    if len(contents) == 3: # early return for "no other bags"
        return output
    for i in range(0,len(contents), 4):
        qty = int(contents[i])
        name = f"{contents[i+1]} {contents[i+2]}"
        output.append((qty, name))
    return output

bags = {}
# first pass populate bag.contains
for line in data.split("\n"):
    bagname = " ".join(line.split(" ")[0:2])
    bag = Bag(bagname)
    for cont in getContainedBags(line):
        bag.addContent(*cont)
    bags[bagname] = bag
# second pass populate bag.contained_by
for line in data.split("\n"):
    bagname = " ".join(line.split(" ")[0:2])
    for cont in getContainedBags(line):
        bags[cont[1]].addContainer(bagname)

def searchForContainers(bags, name):
    cont:Set[str] = set()
    for container in bags[name].contained_by:
        if container not in cont:
            cont = cont.union(searchForContainers(bags, container))
        cont.add(container)
    return cont

output = searchForContainers(bags, "shiny gold")
print(f"Part 1: {len(output)}")

def countContents(bags, name):
    count = 1 # 1 counts the current bag
    for name, qty in bags[name].contains.items():
        # print(contents, bags[name].contains_qty[contents], "X", countContents(bags, contents))
        # count += (int(bags[name].contains_qty[contents]) * int(countContents(bags, contents)))
        count += qty * countContents(bags, name)
    return count


output = countContents(bags, "shiny gold") - 1
print(f"Part 2: {output}")
