from enum import Enum

from card import Card


class Result(Enum):
    INPROGRESS = 0
    VICTORY = 1
    DEFEAT = 2


class User:
    id: int
    result: Result
    sleeve: list


    def __init__(self, id: int, result: Result, sleeve: list):
        self.id = id
        self.result = result
        self.sleeve = sleeve

    def set_result(self, result: Result):
        self.result = result

    def add_card(self, card: Card):
            self.sleeve.append(card)




