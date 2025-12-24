from cell import Cell

class Board:
    def __init__(self, size: int):
        self.size = size
        self.cells = [Cell(i+1) for i in range(size*size)]

    def initialize_snakes(self, snakes: list):
        for snake in snakes:
            start = snake.start
            self.cells[start].snake = snake

    def initialize_ladders(self, ladders: list):
        for ladder in ladders:
            start = ladder.start
            self.cells[start].ladder = ladder