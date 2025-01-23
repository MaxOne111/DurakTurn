import game_turns as turns
import utils

from turn import Turn


def main():

    users = list()

    utils.initialize_users(users, 6)

    list_id = list()

    for user in users:
        list_id.append(user.id)

    deck = utils.generate_deck()

    #----------Init----------

    start_attacker_id = 0
    start_defender_id = start_attacker_id + 1

    cards_in_round = list()

    start_attacker = list_id[start_attacker_id]
    start_defender = list_id[start_defender_id]

    turn = Turn(start_attacker, start_defender, list_id)

    utils.card_distribution(users, deck)

    can_beat = False
    was_take = False
    cards_in_round_was_changed = False

    defender_turn = None
    attacker_turn = None

    while True: #----------Round----------

        print("==========New round==========")

        current_defender_id_in_list = utils.increase_index(len(list_id), turn.queue.index(turn.defender))

        neighbour_id = utils.get_neighbour(list_id, current_defender_id_in_list)

        active_player_id =  turn.attacker

        while True: #----------Turn----------

            attacker_turn = turns.start_attacker_turn(turn, users, active_player_id, can_beat)

            if attacker_turn["cards_count"] == 0:

                if active_player_id in list_id:
                    list_id.remove(active_player_id)

                    if active_player_id == turn.attacker:
                        active_player_id = neighbour_id

                    elif active_player_id == neighbour_id:
                        active_player_id = turn.attacker

            if utils.check_end_game(list_id):
                return

            if attacker_turn["was_beat"] == False: #attacker/neighbour did not press "beat"

                if not attacker_turn["player_card"].rank.name in cards_in_round: #if attacking card is new
                    cards_in_round.append(attacker_turn["player_card"].rank.name)
                    cards_in_round_was_changed = True

                if not was_take: #if defender did not press "take" in first turn
                    defender_turn = turns.start_defender_turn(turn, users, attacker_turn["player_card"])

                if defender_turn["was_take"] == False: #if defender did not press "take" in this turn
                    can_beat = True

                    if defender_turn["cards_count"] == 0:
                        list_id.remove(turn.defender)
                        break

                    if not defender_turn["player_card"].rank.name in cards_in_round: #if defending card is new
                        cards_in_round.append(defender_turn["player_card"].rank.name)
                        cards_in_round_was_changed = True

                    continue
                else: #if defender pressed "take" in this turn
                    was_take = True
                    can_beat = True
                    if turn.attacker == neighbour_id:
                        break
                    elif active_player_id == turn.attacker: #if current active players is attacker
                        continue


            else: #attacker/neighbour pressed "beat"

                if neighbour_id != turn.attacker: #if there is more than 2 players left

                    if active_player_id == turn.attacker:
                        if not cards_in_round_was_changed:
                            break

                        cards_in_round_was_changed = False
                        active_player_id = neighbour_id
                        continue

                    elif active_player_id == neighbour_id:
                        if cards_in_round_was_changed:
                            active_player_id = turn.attacker
                            cards_in_round_was_changed = False
                            continue

                break

        if utils.check_end_game(list_id):
            return

        turn = utils.new_round(turn, list_id, was_take, active_player_id)
        can_beat = False
        was_take = False
        cards_in_round.clear()

main()