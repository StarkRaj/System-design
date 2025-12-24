from collections import deque
import random
import traceback

from typing import List
from board import Board
from dice import Dice
from player import Player
from snake import Snake
from ladder import Ladder

class GameController:
    def __init__(self, board:Board, dice:Dice, players:deque[Player])->None:
        self.board = board
        self.dice= dice
        self.players = players
        self.winner = None

    def generate_snakes(self, count:int)->List[Snake]:
        snakes_head = set()
        snakes:Snake = []
        try:
            if count >= self.board.size*self.board.size:
                raise Exception("Snakes can't be more than cells")
            for i in range(count):
                while True:
                    start = random.randint(self.board.size, self.board.size*self.board.size-2)
                    end = random.randint(0, start-1)
                    if start not in snakes_head:
                        snakes_head.add(start)
                        snakes.append(Snake(start, end))
                        break
            return snakes
        except Exception as err:
            raise err
    
    def generate_ladders(self, count:int)->List[Ladder]:
        ladders_head = set()
        ladders:Ladder = []
        try:
            if count >= self.board.size*self.board.size:
                raise Exception("Ladders can't be more than cells")
            for i in range(count):
                while True:
                    start = random.randint(0, self.board.size*self.board.size-2)
                    end = random.randint(start+1, self.board.size*self.board.size-1)
                    if start not in ladders_head:
                        if self.board.cells[end].snake and self.board.cells[end].snake.end == start:
                            continue
                        ladders_head.add(start)
                        ladders.append(Ladder(start, end))
                        break
            return ladders
        except Exception as err:
            raise err

    def play(self):
        while not self.winner:
            dice_number = self.dice.roll()
            active_player = self.players.popleft()
            print("Active player:", active_player.id)
            position = active_player.position + dice_number
            if position == self.board.size*self.board.size-1:
                active_player.position = position
                self.winner = active_player
                break
            elif not position >= self.board.size*self.board.size:
                while self.board.cells[position].snake != None and self.board.cells[position].ladder != None:
                    if self.board.cells[position].ladder:
                        position = self.board.cells[position].ladder.end
                    if self.board.cells[position].snake:
                        position = self.board.cells[position].snake.end
                active_player.position = position
            self.players.append(active_player)

if __name__=="__main__":
    try:
        board = Board(10)
        dice = Dice()
        no_of_players = 2
        players = deque()
        for i in range(no_of_players):
            players.append(Player(i+1, str(i)))

        controller = GameController(board, dice, players)
        snakes = controller.generate_snakes(5)
        ladders = controller.generate_ladders(5)
        board.initialize_snakes(snakes)
        board.initialize_ladders(ladders)
        controller.play()
        print("Player won:", controller.winner.id)
    except Exception as err:
        print(traceback.format_exc())
