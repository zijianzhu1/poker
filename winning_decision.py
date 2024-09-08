# 输入1-7张牌组成的list，返回list中最大的牌型（return value: String）
# 大小顺序从高到低依次为：皇家同花顺（Royal Flush）、同花顺（Straight Flush）、
# 四条（Four of a Kind）、葫芦（Four of a Kind with a Full House）、同花（Flush）、
# 顺子（Straight）、三条（Three of a Kind）、两对（Two Pair）、一对（One Pair）

# String
from setup import one_card


def find_type(present_cards):  # {player 1: object}
    # card_list eg, format[(number of cards, value of card)]: [(3, 1), (2, 2), (0, 14), (0, 13), (0, 12), (0, 11),
    # (0, 10), (0, 9), (0, 8), (0, 7), (0, 6), (0, 5), (0, 4), (0, 3)]
    # each member has different combinations: three As, two 2s
    card_list = sorted_by_number(present_cards)
    most_card = card_list[0]  # [(K,3), (10, 3), (2,2)]
    most_card2 = card_list[1]

    if (is_straight_flush(present_cards)):
        return "Straight Flush"

    if (most_card[1]) == 4:
        return "Four of a Kind"

    if (is_fullHouse(present_cards)):
        return "FullHouse"

    if (is_flush(present_cards)):
        return "Flush"

    if (is_straight(present_cards)):
        return "Straight"

    if (most_card[1]) == 3:
        return "Three of a Kind"

    if (most_card[1]) == 2 and (most_card2[1]) == 2:
        return "Two Pair"

    if (most_card[1]) == 2:
        return "One Pair"

    return "High Card"


# bool
def is_straight_flush(present_cards):
    # check flush first
    flush_dict = {'Spades': [], 'Clubs': [], 'Hearts': [], 'Diamonds': []}

    for card in present_cards:
        current_suit = card.card_suit
        if current_suit == 'Spades':
            flush_dict['Spades'].append(card)
        elif current_suit == 'Clubs':
            flush_dict['Clubs'].append(card)
        elif current_suit == 'Hearts':
            flush_dict['Hearts'].append(card)
        elif current_suit == 'Diamonds':
            flush_dict['Diamonds'].append(card)

    sorted_dict = sorted(flush_dict.items(), key=lambda x: -len(x[1]))  # dict sorted by the len of the list
    # returns a list of tuples
    # [('Clubs', [card3, card4, card5]),
    # ('Diamonds', [card7, card8, card9]),
    # ('Spades', [card1, card2]),
    # ('Hearts', [card6])]

    flush_cards = sorted_dict[0][1]
    if len(flush_cards) >= 5:
        # then check whether or not the flush is a straight [1,3,6,7,8,9,10]
        if is_straight(flush_cards):
            return True
    return False


# bool
def is_flush(present_cards):
    suitdict = {'Spades': 0, 'Clubs': 0, 'Hearts': 0, 'Diamonds': 0}
    for card in present_cards:
        current_suit = card.card_suit
        suitdict[current_suit] = suitdict[current_suit] + 1
    max_value = max(zip(suitdict.values(), suitdict.keys()))[0]
    #    print (max(zip(suitdict.values(), suitdict.keys())))
    #    print (max_value)
    if max_value >= 5:
        return True
    return False


# bool
def is_straight(present_cards):
    current_count = 0

    present_cards = sorted_by_value(present_cards)  # [(14, 2), (13, 1), (12, 1), (11, 1), (10, 1), (9, 1)]
    present_cards = [list(i) for i in present_cards]
    present_cards[13][1] = present_cards[0][1]
    present_cards = [tuple(i) for i in present_cards]

    # 用count找5个连续的value，如果找到了就返回True
    for i in range(len(present_cards) - 5):
        current_count = 0
        # print('ROUND: ', i+1)
        for j in range(5):
            if present_cards[i + j][1] > 0:
                current_count += 1
                # print(current_count)
            if present_cards[i + j][1] == 0:
                current_count = 0
                # print(current_count)
            if current_count == 5:
                # print('STRAIGHT!')
                return True
    return False

    # if current_count == 0 and card[1] != 0:
    #     current_count += 1
    #     current_value = card[0]
    #     continue

    # if current_value == card[0] - 1:
    #     current_count += 1
    # else:
    #     current_count == 0
    # current_value = card[0]
    # if current_count > max_count:
    #     max_count = current_count

    # print("current value is " + str(current_value))
    # print("current count is " + str(current_count))
    # print(present_cards)
    # if max_count < 5:
    #     return False
    # print('straight!')
    # return True


# bool
def is_fullHouse(present_cards):
    numdict = {'AS': 0, '2': 0, '3': 0, '4': 0, '5': 0,
               '6': 0, '7': 0, '8': 0, '9': 0, '10': 0,
               'J': 0, 'Q': 0, 'K': 0, 'A': 0}
    for card in present_cards:
        current_number = card.card_number
        numdict[current_number] = numdict[current_number] + 1
    # number_sorted return format: [(2, '2'),(1, 'AS'),(1, '4'),(1, '3'),(0, 'Q'),(0, 'K'),...]
    number_sorted = list(reversed(sorted(zip(numdict.values(), numdict.keys()))))
    if number_sorted[0][0] >= 3:
        if number_sorted[1][0] >= 2:
            return True
    return False


# 将present_cards中的card 按照出现的数量从高到低进行排序，返回值为list(tuple)
def sorted_by_number(present_cards) -> list:
    numdict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
               6: 0, 7: 0, 8: 0, 9: 0, 10: 0,
               11: 0, 12: 0, 13: 0, 14: 0}
    for card in present_cards:  # for card in card object
        current_value = card.card_value
        numdict[current_value] = numdict[current_value] + 1
    # number_sorted return format: [(2, 2),(1, 1),(1, 4),(1, 3),(0, 12),(0, 13),...]
    # number_sorted = list(reversed(sorted(zip(numdict.values(), numdict.keys()))))

    # Convert the dictionary to a list of tuples
    # value_list = list(numdict.items())

    # Sort the list of tuples: first by value (ascending), then by key (ascending)
    number_sorted = sorted(list(numdict.items()), key=lambda x: (-x[1], -x[0]))

    return number_sorted


# 将present_cards中的card 按照出现的value大小从高到低进行排序，返回值为list(tuple)
# (e.g) [(14, 0), (13, 0), (12, 0), (11, 0), (10, 0), (9, 0), (8, 0), (7, 0),
# (6, 0), (5, 0), (4, 0), (3, 0), (2, 2), (1, 3)]
def sorted_by_value(present_cards) -> list:
    numdict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
               6: 0, 7: 0, 8: 0, 9: 0, 10: 0,
               11: 0, 12: 0, 13: 0, 14: 0}
    for card in present_cards:
        current_value = card.card_value
        numdict[current_value] = numdict[current_value] + 1
    value_sorted = list(reversed(sorted(zip(numdict.keys(), numdict.values()))))

    return value_sorted


# 对比牌型大小，如果相同牌型的话对比双方手牌大小
def compare_hands(present_cards_mine, present_cards_opponent) -> int:  # value - win:1 tie:0 lose:-1
    my_hand_type = find_type(present_cards_mine)
    opponent_hand_type = find_type(present_cards_opponent)
    hand_type = compare_hand_type(my_hand_type, opponent_hand_type)

 #   print('my hand: ', my_hand_type)
   # print('opp hand: ', opponent_hand_type)

    if hand_type == 1:  # my hand type wins
        return 1
    elif hand_type == -1:  # opponent hand type wins
        return -1
    elif hand_type == 0:  # my_hand_type == opponent_hand_type
        if my_hand_type == "Straight Flush" or my_hand_type == "Straight":
            return compare_straight(present_cards_mine, present_cards_opponent)

        if my_hand_type == "Four of a Kind":
            return compare_four(present_cards_mine, present_cards_opponent)

        if my_hand_type == "FullHouse":
            return compare_fullHouse(present_cards_mine, present_cards_opponent)

        if my_hand_type == "Flush":
            return compare_flush(present_cards_mine, present_cards_opponent)

        if my_hand_type == "Three of a Kind":
            return compare_three(present_cards_mine, present_cards_opponent)

        if my_hand_type == "Two Pairs":
            return compare_pairs(present_cards_mine, present_cards_opponent)

        if my_hand_type == "One Pair":
            return compare_pairs(present_cards_mine, present_cards_opponent)

        if my_hand_type == "High Card":
            return compare_high(present_cards_mine, present_cards_opponent)


# 对比牌型大小
def compare_hand_type(my_hand, opponent_hand) -> int:
    type_dict = {'Straight Flush': 8, 'Four of a Kind': 7, 'FullHouse': 6,
                 'Flush': 5, 'Straight': 4, 'Three of a Kind': 3, 'Two Pair': 2,
                 'One Pair': 1, 'High Card': 0}
    if type_dict[my_hand] > type_dict[opponent_hand]:
        return 1
    elif type_dict[my_hand] < type_dict[opponent_hand]:
        return -1
    elif type_dict[my_hand] == type_dict[opponent_hand]:
        return 0


def compare_straight(present_cards_mine, present_cards_opponent) -> int:
    # need to compare straight flush
    my_hand_sorted = sorted_by_value(present_cards_mine)
    op_hand_sorted = sorted_by_value(present_cards_opponent)

    my_biggest = one_card()
    for i in range(len(my_hand_sorted)):
        # 当前的第i张手牌张数不为0，且后两张牌的张数也不为0
        if my_hand_sorted[i][1] != 0 and my_hand_sorted[i + 1][1] != 0 and my_hand_sorted[i + 2][1] != 0:
            my_biggest = my_hand_sorted[i]
            break

    op_biggest = one_card()
    for i in range(len(op_hand_sorted)):
        # 当前的第i张手牌张数不为0，且后两张牌的张数也不为0
        if op_hand_sorted[i][1] != 0 and op_hand_sorted[i + 1][1] != 0 and op_hand_sorted[i + 2][1] != 0:
            op_biggest = op_hand_sorted[i]
            break

    if my_biggest[0] > op_biggest[0]:
        return 1
    elif my_biggest[0] < op_biggest[0]:
        return -1
    elif my_biggest[0] == op_biggest[0]:
        return 0


def compare_four(present_cards_mine, present_cards_opponent) -> int:
    # (e.g) [(14, 0), (13, 0), (12, 0), (11, 0), (10, 0), (9, 0), (8, 0), (7, 0),
    # (6, 0), (5, 0), (4, 0), (3, 0), (2, 2), (1, 3)]
    my_hand_sorted = sorted_by_number(present_cards_mine)
    op_hand_sorted = sorted_by_number(present_cards_opponent)

    # print(my_hand_sorted)
    # print(op_hand_sorted)

    # 先对比四条的大小
    my_biggest = one_card()
    found_my_biggest_card = False
    # 再对比第二大的单牌的大小
    my_second_big = one_card()
    for i in range(len(my_hand_sorted)):  # 0, 1, 2
        # 找到最大的牌后找第二大的单牌
        if found_my_biggest_card and my_hand_sorted[i][1] >= 1:
            my_second_big = my_hand_sorted[i]
            break

        # find the straight
        if my_hand_sorted[i][1] == 4:
            my_biggest = my_hand_sorted[i]
            found_my_biggest_card = True

    op_biggest = one_card()
    found_op_biggest_card = False
    op_second_big = one_card()
    for i in range(len(op_hand_sorted)):
        if found_op_biggest_card and op_hand_sorted[i][1] >= 1:
            op_second_big = op_hand_sorted[i]
            break

        # find the straight
        if op_hand_sorted[i][1] == 4:
            op_biggest = op_hand_sorted[i]
            found_op_biggest_card = True

    if my_biggest[0] > op_biggest[0]:
        return 1
    elif my_biggest[0] < op_biggest[0]:
        return -1
    elif my_biggest[0] == op_biggest[0]:
        # compare the second big
        if my_second_big[0] > op_second_big[0]:
            return 1
        elif my_second_big[0] < op_second_big[0]:
            return -1
        elif my_second_big[0] == op_second_big[0]:
            return 0


def compare_fullHouse(present_cards_mine, present_cards_opponent) -> int:
    my_hand_sorted = sorted_by_value(present_cards_mine)
    op_hand_sorted = sorted_by_value(present_cards_opponent)

    my_biggest = one_card()
    found_my_biggest_card = False
    my_second_big = one_card()

    # compare the three of a kinds
    for i in range(len(my_hand_sorted)):
        # 找到最大的牌后找第二大的单牌
        if found_my_biggest_card and my_hand_sorted[i][1] >= 2:
            my_second_big = my_hand_sorted[i]
            break

        # 当前的第i张手牌张数数量大于等于4
        if my_hand_sorted[i][1] == 3:
            my_biggest = my_hand_sorted[i]
            found_my_biggest_card = True

    op_biggest = one_card()
    found_op_biggest_card = False
    op_second_big = one_card()

    # compare the three of a kinds
    for i in range(len(my_hand_sorted)):
        # 找到最大的牌后找第二大的单牌
        if found_op_biggest_card and op_hand_sorted[i][1] >= 2:
            op_second_big = op_hand_sorted[i]
            break

        # 当前的第i张手牌张数数量大于等于4
        if op_hand_sorted[i][1] == 3:
            op_biggest = op_hand_sorted[i]
            found_op_biggest_card = True

    if my_biggest[0] > op_biggest[0]:
        return 1
    elif my_biggest[0] < op_biggest[0]:
        return -1
    elif my_biggest[0] == op_biggest[0]:
        # if both the same, compare the pairs
        if my_second_big[0] > op_second_big[0]:
            return 1
        elif my_second_big[0] < op_second_big[0]:
            return -1
        elif my_second_big[0] == op_second_big[0]:
            return 0


def compare_flush(present_cards_mine, present_cards_opponent) -> int:  # inputs ares list of objects

    def find_flush(present_cards):
        flush_dict = {'Spades': [], 'Clubs': [], 'Hearts': [], 'Diamonds': []}

        for card in present_cards_mine:
            current_suit = card.card_suit
            if current_suit == 'Spades':
                flush_dict['Spades'].append(card)
            elif current_suit == 'Clubs':
                flush_dict['Clubs'].append(card)
            elif current_suit == 'Hearts':
                flush_dict['Hearts'].append(card)
            elif current_suit == 'Diamonds':
                flush_dict['Diamonds'].append(card)

        sorted_dict = sorted(flush_dict.items(), key=lambda x: -len(x[1]))  # returns a list of tuples
        # flush_cards = sorted(sorted_dict[0][1], reverse = True) #sorted by desc order [K, 10, 8, etc]
        flush_cards = sorted(sorted_dict[0][1], key=lambda card: card.card_value,
                             reverse=True)  # sorted by desc order [K, 10, 8, etc]
        return flush_cards

    my_flush = find_flush(present_cards_mine)
    op_flush = find_flush(present_cards_opponent)

    # compare who has the higher card in flush
    my_biggest = my_flush[0].card_value
    op_biggest = op_flush[0].card_value
    if my_biggest > op_biggest:
        return 1
    elif my_biggest < op_biggest:
        return -1


def compare_three(present_cards_mine, present_cards_opponent) -> int:
    my_hand_sorted = sorted_by_number(present_cards_mine)
    op_hand_sorted = sorted_by_number(present_cards_opponent)

    my_biggest = one_card()
    found_my_biggest_card = False
    my_second_big = one_card()

    # compare the three of a kinds
    for i in range(len(my_hand_sorted)):
        # 找到最大的牌后找第二大的单牌
        if found_my_biggest_card and my_hand_sorted[i][1] >= 1:
            my_second_big = my_hand_sorted[i]
            break

        # 当前的第i张手牌张数数量大于等于4
        if my_hand_sorted[i][1] == 3:
            my_biggest = my_hand_sorted[i]
            found_my_biggest_card = True

    op_biggest = one_card()
    found_op_biggest_card = False
    op_second_big = one_card()

    # compare the three of a kinds
    for i in range(len(my_hand_sorted)):
        # 找到最大的牌后找第二大的单牌
        if found_op_biggest_card and op_hand_sorted[i][1] >= 1:
            op_second_big = op_hand_sorted[i]
            break

        # 当前的第i张手牌张数数量大于等于4
        if op_hand_sorted[i][1] == 3:
            op_biggest = op_hand_sorted[i]
            found_op_biggest_card = True

    if my_biggest[0] > op_biggest[0]:
        return 1
    elif my_biggest[0] < op_biggest[0]:
        return -1
    elif my_biggest[0] == op_biggest[0]:
        # if both the same, compare the second big
        if my_second_big[0] > op_second_big[0]:
            return 1
        elif my_second_big[0] < op_second_big[0]:
            return -1
        elif my_second_big[0] == op_second_big[0]:
            return 0


def compare_pairs(present_cards_mine, present_cards_opponent) -> int:
    my_hand_sorted = sorted_by_number(present_cards_mine)
    op_hand_sorted = sorted_by_number(present_cards_opponent)

    # [(K, 2), (6, 2)]
    my_biggest = my_hand_sorted[0]
    my_second_big = my_hand_sorted[1]
    op_biggest = op_hand_sorted[0]
    op_second_big = my_hand_sorted[1]

    if my_biggest[0] > op_biggest[0]:
        return 1
    elif my_biggest[0] < op_biggest[0]:
        return -1
    elif my_biggest[0] == op_biggest[0]:
        if my_second_big[0] > op_second_big[0]:
            return 1
        elif my_second_big[0] < op_second_big[0]:
            return -1
        elif my_second_big[0] == op_second_big[0]:
            return 0


def compare_high(present_cards_mine, present_cards_opponent) -> int:
    my_hand_sorted = sorted_by_number(present_cards_mine)
    op_hand_sorted = sorted_by_number(present_cards_opponent)

    # [(K, 2), (6, 2)]
    my_biggest = my_hand_sorted[0]
    op_biggest = op_hand_sorted[0]

    if my_biggest[0] > op_biggest[0]:
        return 1
    elif my_biggest[0] < op_biggest[0]:
        return -1
    elif my_biggest[0] == op_biggest[0]:
        return 0


def compare_all_players(players_card):  # {player1: [object]}
    number_of_players = len(players_card)
    # keys = list(players_card.keys()) #[player1, player2, player3]

    points = {player: 0 for player in players_card}

    for i in players_card.keys():
        print(i, 'turn')
        for j in players_card.keys():
            if i != j:  # avoid objects comparing with themselves
                game_results = compare_hands(players_card[i], players_card[j])  # {player1: [object]}

                if game_results is not None:
                    points[i] += game_results
  #  print(sorted(points.items(), key=lambda x: -x[1]))
    winner = sorted(points.items(), key=lambda x: -x[1])[0]
    return winner




