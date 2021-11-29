from ad8_data import data

sourcecode = data.split("\n")


class Interpreter:
    def __init__(self):
        self.accumulator = 0
        self.inst = 0
        self.instructions = {
            "nop": self.nop,
            "acc": self.acc,
            "jmp": self.jmp
        }
        self.call_log = [] # list of the instructions that have been called.

    def reset(self):
        self.accumulator = 0
        self.inst = 0
        self.call_log = [] # list of the instructions that have been called.

    def nop(self, arg):
        self.inst += 1

    def acc(self, arg):
        self.accumulator += int(arg)
        self.inst += 1

    def jmp(self, arg):
        self.inst += int(arg)

    def execute(self, sourcecode):
        while True:
            if self.inst == len(sourcecode)+1:
                print("Execution Complete.")
                return True
            (i, a) = sourcecode[self.inst].split(" ")
            if self.inst in self.call_log:
                print(f"Loop detected at instruction {max(self.call_log)+1}")
                print(f"Accumulator: {self.accumulator}")
                return False
            self.call_log.append(self.inst)
            self.instructions[i](a)

def modifySource(sourcecode, call_log):
    """Find the last call of nop or jmp in call_log, and swap it in sourcecode"""
    searching = True
    i = len(call_log) - 1
    while searching and (i>0):
        (ins, a) = sourcecode[call_log[i]].split(" ")
        if ins == "nop":
            print(f"{sourcecode[call_log[i]]} -> jmp {a}")
            sourcecode[call_log[i]] = f"jmp {a}"
            return sourcecode
        if ins == "jmp":
            print(f"{sourcecode[call_log[i]]} -> nop {a}")
            sourcecode[call_log[i]] = f"nop {a}"
            return sourcecode
        else:
            i -= 1

interp = Interpreter()
while True:
    interp.reset()
    if not interp.execute(sourcecode):
        sourcecode = modifySource(sourcecode, interp.call_log)
        # modify src?
    else:
        # should be good
        pass
