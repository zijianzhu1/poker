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

    player1 = [all_cards['A Hearts'], all_cards['K Hearts'], all_cards['10 Spades'], all_cards['6 Hearts'], all_cards['2 Diamonds'], all_cards['J Diamonds'], all_cards['Q Hearts']] #straight - A
    player2 = [all_cards['A Hearts'], all_cards['K Hearts'], all_cards['10 Spades'], all_cards['6 Hearts'], all_cards['2 Diamonds'], all_cards['10 Hearts'], all_cards['8 Hearts']]  #Hearts flush
    player3 = [all_cards['A Hearts'], all_cards['K Hearts'], all_cards['10 Spades'], all_cards['6 Hearts'], all_cards['2 Diamonds'], all_cards['K Clubs'], all_cards['K Diamonds']] #three of a kind - K
    player4 = [all_cards['A Hearts'], all_cards['K Hearts'], all_cards['10 Spades'], all_cards['6 Hearts'], all_cards['2 Diamonds'], all_cards['Q Clubs'], all_cards['3 Clubs']] #Q high
    player5 = [all_cards['A Hearts'], all_cards['K Hearts'], all_cards['10 Spades'], all_cards['6 Hearts'], all_cards['2 Diamonds'], all_cards['A Diamonds'], all_cards['9 Spades']] #A pairs
    player6 = [all_cards['A Hearts'], all_cards['K Hearts'], all_cards['10 Spades'], all_cards['6 Hearts'], all_cards['2 Diamonds'], all_cards['10 Clubs'], all_cards['10 Diamonds']] #three of a kind - 10
    player7 = [all_cards['A Hearts'], all_cards['K Hearts'], all_cards['10 Spades'], all_cards['6 Hearts'], all_cards['2 Diamonds'], all_cards['7 Clubs'], all_cards['5 Diamonds']] #7 high

    all_players = {'player 1': player1, 'player 2': player2, 'player 3': player3, 'player 4': player4, 'player 5': player5, 'player 6': player6}

   # print(compare_all_players(all_players)) ##{player 1: ['J','K', 'A', '2', '3']}

    player_board = Player_board("zijian",player_with_river_cards)
    P_UI=Player_UI(player_board,player_with_river_cards,all_cards)
    P_UI.run()

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
