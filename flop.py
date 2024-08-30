def flop_card(remaining_card,players_card):
    keys = list(players_card.keys())
    #flop_card_name=keys[0:3]
    flop_cards=remaining_card[0:3]
    print(flop_cards[0].name)
    print(flop_cards[1].name)
    print(flop_cards[2].name)
    print(keys)
    for i in keys:
        players_card[i].append(flop_cards[0])
        players_card[i].append(flop_cards[1])
        players_card[i].append(flop_cards[2])
    print(players_card)
    print(remaining_card)
    print(len(remaining_card))
    remaining_card_after_flop=remaining_card[3:len(remaining_card)]
    return players_card,remaining_card_after_flop
def turn_card(remaining_card,players_card):
    keys = list(players_card.keys())
    turn_cards = remaining_card[0]
    for i in keys:
        players_card[i].append(turn_cards)
    print(players_card)
    print(remaining_card)
    print(len(remaining_card))
    remaining_card_after_turn = remaining_card[1:len(remaining_card)]
    return players_card, remaining_card_after_turn
def river_card(remaining_card,players_card):
    keys = list(players_card.keys())
    river_cards = remaining_card[0]
    for i in keys:
        players_card[i].append(river_cards)
    remaining_card_after_river=remaining_card[1:len(remaining_card)]
    return players_card,remaining_card_after_river