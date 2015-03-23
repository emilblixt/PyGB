#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      EM007
#
# Created:     11-02-2015
# Copyright:   (c) EM007 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------


class CPU:
    def __init__(self, clockrate):
        self.hz = clockrate  # Clock speed
        self.cc = self.hz  # Cycle Counter
        self.pc = 0  # Program Counter
        self.sp = 0  # Stack Pointer

        self.registers = {
            'A': 0x00,
            'B': 0x00,
            'C': 0x00,
            'D': 0x00,
            'E': 0x00,
            'F': 0x00,
            'H': 0x00,
            'L': 0x00
        }

        self.flags = {
            'Z': 0x00,
            'N': 0x00,
            'H': 0x00,
            'C': 0x00
        }

    def reset(self):
        self.pc = 0x0100
        self.sp = 0xFFFE

    def run(self):
        while True:
            self.pc += 1
            # Code to read opcode here and calculate cycles
            if self.cc <= 0:
                break

    def executeopcode(self, opcode):
        if opcode:
            return self.hz + opcode
        else:
            return None

cpu = CPU(60)




"""
Plan:
    Read OpCode
    Decrease CC depending on amount of cycles OpCode needs
    Execute OpCode
    if cc <= 0 cc = cpu_hz

"""