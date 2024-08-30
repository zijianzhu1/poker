# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from setup import card_set_up
from pre_flop import distribute_cards
from flop import flop_card
from flop import turn_card
from flop import river_card
from winning_decision import compare_all_players
from interface_setup import Player_board
from userinterface import Player_UI
def main():
    all_cards=card_set_up()
    players_card,remaining_card=distribute_cards(7,all_cards)
    player_with_flop_cards,remaining_card_after_flop=flop_card(remaining_card,players_card)
    player_with_turn_cards, remaining_card_after_turn = turn_card(remaining_card_after_flop, player_with_flop_cards)
    player_with_river_cards, remaining_card_after_river = river_card(remaining_card_after_turn,player_with_turn_cards)
    compare_all_players(player_with_river_cards)

    player_board = Player_board("zijian",player_with_river_cards)
    P_UI=Player_UI(player_board,player_with_river_cards)
    P_UI.run()

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
