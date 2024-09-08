import random
def distribute_cards(number_of_players,all_cards):
    number_of_cards=number_of_players*2
    card_index=random.sample(range(4,56),52)#number_of_cards)
    print(card_index)
    players_card={}
    keys = list(all_cards.keys())
    print(len(card_index))
    print(len(keys))
    print(keys)
    remaining_card_starting_index=2*number_of_players
    for i in range(number_of_players):
        player_name="player "+str(i+1)
        print(player_name)
        card_one_index=i*2
        card_two_index=i*2+1
        #print(card_index[card_one_index])
        #print(keys[card_index[card_one_index]-1])
        #print(keys[card_index[card_two_index]-1])
        card_one=all_cards[keys[card_index[card_one_index]]]
        card_two=all_cards[keys[card_index[card_two_index]]]
        players_card[player_name]=[card_one,card_two]
    remaining_card_index1=card_index[remaining_card_starting_index:52]
    remaining_card_index2=[]
    print(remaining_card_index1)
    #print(keys)
    for i in remaining_card_index1:
        remaining_card_index2.append(keys[i-1])
    remaining_card=[]
    for i in remaining_card_index2:
        remaining_card.append(all_cards[i])
    print(remaining_card)
    print(players_card)
    print(card_index)
    return players_card,remaining_card
