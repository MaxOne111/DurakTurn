from user import User
from turn import Turn
from card import Card
import utils

def start_attacker_turn(turn: Turn, users: list[User], player_id: int, can_beat: bool):

    active_player: User = utils.find_player_by_id(users, player_id)

    if len(active_player.sleeve) == 0:
        return {
            "player_card": None,
            "player_id": active_player.id,
            "was_beat": True,
            "cards_count": len(active_player.sleeve),
        }

    print(f"Now move is {active_player.id}")

    print("Your cards:")
    for card in active_player.sleeve:
        print(f"{active_player.sleeve.index(card) + 1}.{utils.get_card_view(card)}", end="---")
    if can_beat:
        print("\nEnter 0 for beat")

    player_card_id = int(input("\nChoose card: "))

    if can_beat:
        if player_card_id == 0:
            return {
                "player_card": None,
                "player_id": active_player.id,
                "was_beat": True,
                "cards_count": len(active_player.sleeve),
            }


    player_card: Card = active_player.sleeve[player_card_id - 1]

    active_player.sleeve.remove(player_card)

    action_text = ""

    if active_player.id != turn.defender:
        action_text = "Attacked by"
    else:
        action_text = "Defenced by"

    print(f"{action_text}: {utils.get_card_view(player_card)}")

    print("----------")

    return {
        "player_card" : player_card,
        "player_id" : active_player.id,
        "was_beat" : False,
        "cards_count": len(active_player.sleeve),
    }

def start_defender_turn(turn: Turn, users: list[User], attacking_card: utils.Card):

    active_player = utils.find_player_by_id(users, turn.defender)

    print(f"Now move is {active_player.id}")

    print("Your cards:")
    for card in active_player.sleeve:
        print(f"{active_player.sleeve.index(card) + 1}.{utils.get_card_view(card)}", end="---")
    print("\nEnter 0 for take")

    print(f"Attacking card: {utils.get_card_view(attacking_card)}")

    player_card_id = int(input("Choose card: "))

    if player_card_id == 0:
        utils.take_card(active_player, attacking_card)
        print(f"User {active_player.id} take card {utils.get_card_view(attacking_card)}\n")
        return {
            "player_card": None,
            "was_take" : True,
            "cards_count": len(active_player.sleeve),
        }

    defence_card = active_player.sleeve[player_card_id - 1]

    if utils.can_defend(attacking_card, defence_card):
        active_player.sleeve.remove(defence_card)
        was_take = False
    else:
        print("----------")
        start_defender_turn(turn, users, attacking_card)
        return {
            "player_card": None,
            "was_take": True,
            "cards_count": len(active_player.sleeve),
        }

    print(f"Defenced by: {utils.get_card_view(defence_card)}")

    print("----------")

    return {
        "player_card" : defence_card,
        "was_take": False,
        "cards_count": len(active_player.sleeve),
    }

