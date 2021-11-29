from ad8_data import data
from ad8_data_2 import data as data2

sourcecode = data.split("\n")


class Interpreter:
    def __init__(self):
        self.accumulator = 0
        self.pos = 0
        self.instructions = {
            "nop": self.nop,
            "acc": self.acc,
            "jmp": self.jmp
        }
        self.call_log = [] # list of the instructions that have been called.

    def reset(self):
        self.accumulator = 0
        self.pos = 0
        self.call_log = [] # list of the instructions that have been called.

    def nop(self, arg):
        self.pos += 1

    def acc(self, arg):
        self.accumulator += int(arg)
        self.pos += 1

    def jmp(self, arg):
        self.pos += int(arg)

    def execute(self, sourcecode):
        while True:
            if self.pos == len(sourcecode):
                print("Execution Complete.")
                return True
            (i, a) = sourcecode[self.pos].split(" ")
            if self.pos in self.call_log:
                #print(f"Loop detected at instruction {max(self.call_log)+1}")
                #print(f"Accumulator: {self.accumulator}")
                return False
            self.call_log.append(self.pos)
            self.instructions[i](a)

def findNextCallLogIndexToModify(index, call_log, sourcecode):
    while index > 0:
        index -= 1
        (i, a) = sourcecode[call_log[index]].split(" ")
        if i == 'nop':
            return (index, f"jmp {a}")
        if i == 'jmp':
            return (index, f"nop {a}")
    return (0, "ERR 0")


interp = Interpreter()
interp.execute(sourcecode)
print("Part 1:", interp.accumulator)

original_call_log = interp.call_log.copy()
# modified_call_log = interp.call_log
modified_call_index = len(original_call_log)
modified_sourcecode = sourcecode.copy()
while True:
    interp.reset()
    if not interp.execute(sourcecode):
        (modified_call_index, new_call) = findNextCallLogIndexToModify(modified_call_index, original_call_log, sourcecode)
        modified_sourcecode = sourcecode
        modified_sourcecode[original_call_log[modified_call_index]] = new_call
    else:
        print("Part 2: modify line",original_call_log[modified_call_index]+1, "change it to:", new_call)
        # should be good
        break

sourcecode2 = data2.split("\n")
interp.execute(sourcecode)
print("Part 2:", interp.accumulator)
