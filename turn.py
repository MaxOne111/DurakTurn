from typing import List


class Turn:
    attacker: int
    defender: int
    queue: List[int]

    def __init__(self, attacker: int, defender: int, queue: List[int]):
        self.attacker = attacker
        self.defender = defender
        self.queue = queue



