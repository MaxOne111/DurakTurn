import random

from user import User
from eresult import Result
from turn import Turn
from card import Card, ECardRank, ECardSuits

def get_neighbour(list_id: list, defender_id_in_list: int):

    if len(list_id) == 2:
        return list_id[increase_index(len(list_id), defender_id_in_list - 1)]

    return list_id[increase_index(len(list_id), defender_id_in_list + 1)]

def take_card(user: User, taken_card: Card):
    user.add_card(taken_card)

def increase_index(list_len: int, index: int):

    result = index % list_len

    return result

def get_card_view(card: Card):
    view = f"{card.suit.value}{card.rank.name}"
    return view

def generate_deck():
    deck = []
    for suit in ECardSuits:
        for rank in ECardRank:
            deck.append(Card(suit, rank))
    return deck

def card_distribution(users: list[User], deck: list[Card]):
    for user in users:
        for i in range(6):
            random_card = random.choice(deck)
            user.add_card(random_card)
            deck.remove(random_card)



def initialize_users(users: list[User], players_count: int):
    max_count = 6

    if players_count <= 1 or players_count > max_count :
        raise ValueError("Invalid players count")

    first_id = random.randint(1, 100 - max_count)

    for i in range(first_id, first_id + players_count):
        users.append(User(i, Result.INPROGRESS, []))

def init_users(users: list[User], min_id: int, max_id: int):

    if min_id < 0 or max_id < 0 or max_id <= min_id or max_id - max_id == 1 or max_id - min_id > 6:
        raise Exception("Invalid players count")

    for i in range(min_id,max_id):
        users.append(User(i, Result.INPROGRESS, []))


def new_round(prev_turn: Turn, list_id: list, was_take: bool, active_player_id: int):

    add_index = 1

    if was_take:
        add_index = 2

    if not prev_turn.attacker in list_id and not prev_turn.defender in list_id:
        next_attacker = find_id_by_player_id(list_id, active_player_id)
        attacker_id = increase_index(len(list_id), next_attacker)
    elif not prev_turn.attacker in list_id:
        attacker_id = increase_index(len(list_id), list_id.index(prev_turn.defender) + add_index - 1)
    else:
        attacker_id = increase_index(len(list_id), list_id.index(prev_turn.attacker) + add_index)

    defender_id = increase_index(len(list_id), attacker_id + 1)

    attacker = list_id[attacker_id]
    defender = list_id[defender_id]

    return Turn(attacker, defender, list_id)


def can_defend(attack_card: Card, defend_card: Card):
    if attack_card.suit == defend_card.suit:

        result = defend_card.rank.value > attack_card.rank.value

        if result == False:
            print("Weak card")
            return False

        return result
    else:
        print("Not suit")
        return False

def find_player_by_id(users: list, id: int):
    founded_player = list(filter(lambda user: user.id == id, users))
    if len(founded_player) == 0:
        return None

    return founded_player[0]

def find_id_by_player_id(list_id: list, player_id: int):
    founded_player = list_id.index(player_id)

    return founded_player

def check_end_game(list_id: list):
    if len(list_id) == 1:
        print(f"Game Over, {list_id[0]} lose!")
        return True

    return False