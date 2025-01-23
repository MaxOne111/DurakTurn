from card import Card
from eresult import Result


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




