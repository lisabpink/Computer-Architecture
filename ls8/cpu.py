"""CPU functionality."""

import sys


class CPU:
    """Main CPU class."""

#! Day 1: Step 1: Add the constructor to `cpu.py`
    def __init__(self):
        """Construct a new CPU."""
        self.pc = 0
        self.reg = [0] * 8
        self.ram = [0] * 256

#! Day 1: Step 2: Add RAM functions

    # `ram_read()` should accept the address to read and return the value stored there.
    def ram_read(self, mar):
        return self.ram[mar]

    # `ram_write()` should accept a value to write, and the address to write it to.
    def ram_write(self, mar, mdr):
        self.ram[mar] = mdr

    def load(self, prog):
        """Load a program into memory."""

        address = 0

        #! Day 2:  Step 7: Un-hardcode the machine code
        with open(prog) as program:
            for ins in program:
                ins_split = ins.split('#')
                ins_value = ins_split[0].strip()

                print(f"INS VAL >>>{ins_value}")

                if ins_value == '':
                    continue
                ins_num = int(ins_value, 2)
                print(f"TO RAM {ins_num , address}")
                self.ram_write(address, ins_num)
                address += 1

        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010,  # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111,  # PRN R0
        #     0b00000000,
        #     0b00000001,  # HLT
        # ]

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

#! Day 1: Step 3: Implement the core of `CPU`'s `run()` method
    def run(self):
        """Run the CPU."""
        HLT = 0b00000001
        LDI = 0b10000010
        PRN = 0b01000111
        #! Step 8: Implement a Multiply and Print the Result
        MUL = 0b10100010

        running = True

        while running:
            instruction = self.ram_read(self.pc)
            opr_a = self.ram_read(self.pc + 1)
            opr_b = self.ram_read(self.pc + 2)

            #! Day 1: Step 4: Implement the `HLT` instruction handler
            if instruction == HLT:
                running = False
                self.pc += 1

            #! Day 1: Step 5: Add the `LDI` instruction
            elif instruction == LDI:
                self.reg[opr_a] = opr_b
                self.pc += 3

            #! Day 1: Step 6: Add the `PRN` instruction
            elif instruction == PRN:
                print(self.reg[opr_a])
                self.pc += 2

              #! Day 2:  Step 8: Implement a Multiply and Print the Result
            elif instruction == MUL:
                product = self.reg[opr_a] * self.reg[opr_b]
                self.reg[opr_a] = product
                self.pc += 3

            else:
                print(f"bad input: {bin(instruction)}")

                running = False
