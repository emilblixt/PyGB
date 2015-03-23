from mem import memory
from processor import cpu


class GameBoy:
    def __init__(self):
        memory.test = 10
        cpu.hz = 10
