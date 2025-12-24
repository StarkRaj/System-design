class Cell:
    def __init__(self, position: int):
        self.position = position
        self.snake = None
        self.ladder = None