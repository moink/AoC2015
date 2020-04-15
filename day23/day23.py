import abc
import collections

def read_input_lines():
    """Open today's input data and return it as a list of lines

    Returns:
        [str]
            Lines in 'input.txt'
    """
    with open('input.txt') as in_file:
        data = in_file.read().strip().splitlines()
    return data

class Computer(abc.ABC):
    """A virtual machine base class for running custom assembly languages

    Seems that Topaz likes to put problems that require virtual machines
    with registers that run his own small assembly languages. There was one
    in 2015 (day 23) and one in 2016 (day 12) and a much more complex one
    used on many days in 2019. This probably doesn't implement enough for
    the 2019 IntCode computer but it works for 2016 and probably 2015 (will
    check later).

    To use this, inherit from this class. Include the following two lines at
    the start of the class:
        operation = advent_tools.Computer.operation
        return_register = 'a'
    (setting return_register to the register that the question requests) and
    then decorate all assembly commands with @operation('cmd') where cmd is
    the first word of the instruction to call that command. The operations
    can use self.registers.
    """

    operation_map = {}

    @property
    @abc.abstractmethod
    def return_register(self):
        pass

    def __init__(self):
        self.registers = collections.defaultdict(int)
        self.instruction_pointer = 0

    @classmethod
    def operation(cls, instruction_start):
        def decorator(func):
            cls.operation_map[instruction_start] = func
            return func
        return decorator

    def run_instruction(self, line):
        words = line.split()
        func = self.operation_map[words[0]]
        func(self, *words[1:])

    def run_program(self, program):
        while True:
            try:
                line = program[self.instruction_pointer]
            except IndexError:
                return self.registers[self.return_register]
            self.run_instruction(line)
            self.instruction_pointer = self.instruction_pointer + 1

    def run_input_file(self):
        program = read_input_lines()
        return(self.run_program(program))

class AdventComputer(Computer):

    operation = Computer.operation
    return_register = 'b'

    def run_instruction(self, line):
        line = line.replace(',', ' ')
        super().run_instruction(line)

    @operation('hlf')
    def halve(self, key):
        self.registers[key] = self.registers[key] // 2

    @operation('tpl')
    def triple(self, key):
        self.registers[key] = 3 * self.registers[key]

    @operation('inc')
    def increment(self, key):
        self.registers[key] = self.registers[key] + 1

    @operation('jmp')
    def jump(self, offset):
        self.instruction_pointer = self.instruction_pointer + int(offset) - 1

    @operation('jie')
    def jump_if_even(self, key, offset):
        if (self.registers[key] % 2) == 0:
            self.jump(offset)

    @operation('jio')
    def jump_if_one(self, key, offset):
        if self.registers[key] == 1:
            self.jump(offset)

def test_program():
    program = ['inc b', 'jio b, +2', 'tpl b', 'inc b']
    computer = AdventComputer()
    print(computer.run_program(program))

def part_1():
    computer = AdventComputer()
    print(computer.run_input_file())

def part_2():
    computer = AdventComputer()
    computer.registers['a'] = 1
    print(computer.run_program(program))

if __name__ == '__main__':
    part_1()
    # test_program()
    # part_2()