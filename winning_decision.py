# 输入1-7张牌组成的list，返回list中最大的牌型（return value: String）
# 大小顺序从高到低依次为：皇家同花顺（Royal Flush）、同花顺（Straight Flush）、
# 四条（Four of a Kind）、葫芦（Four of a Kind with a Full House）、同花（Flush）、
# 顺子（Straight）、三条（Three of a Kind）、两对（Two Pair）、一对（One Pair）

# String
from setup import one_card
def find_type(present_cards):
    #card_list eg, format[(number of cards, value of card)]: [(3, 1), (2, 2), (0, 14), (0, 13), (0, 12), (0, 11),
    # (0, 10), (0, 9), (0, 8), (0, 7), (0, 6), (0, 5), (0, 4), (0, 3)]
    card_list = sorted_by_number(present_cards)
    most_card = card_list[0]

    if(is_straight(present_cards)):
        if(is_flush(present_cards)):
            return "Straight Flush"

    if(most_card[0]) == 4:
        return "Four of a Kind"

    if(is_fullHouse(present_cards)):
        return "FullHouse"

    if(is_flush(present_cards)):
        return "Flush"

    if(is_straight(present_cards)):
        return "Straight"

    if(most_card[0]) == 3:
        return "Three of a Kind"

    if(most_card[0]) == 2 and (most_card[1]) == 2:
        return "Two Pair"

    if(most_card[0]) == 2:
        return "One Pair"

    return "High Card"

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
    max_count = 0
    current_count = 0
    current_value = 0
    # 用count找5个连续的value，如果找到了就返回True
    for card in present_cards:
        if current_count == 0:
            current_count += 1
            current_value = card.card_value
            continue

        if current_value == card.card_value - 1:
            current_count += 1
        else:
            current_count == 0
        current_value = card.card_value
        if current_count > max_count:
            max_count = current_count

        #print("current value is " + str(current_value))
        #print("current count is " + str(current_count))

    if max_count < 5:
        return False
    return True

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
    for card in present_cards:
        current_value = card.card_value
        numdict[current_value] = numdict[current_value] + 1
    # number_sorted return format: [(2, 2),(1, 1),(1, 4),(1, 3),(0, 12),(0, 13),...]
    number_sorted = list(reversed(sorted(zip(numdict.values(), numdict.keys()))))

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
def compare_hands(present_cards_mine, present_cards_opponent) -> bool:
    my_hand_type = find_type(present_cards_mine)
    opponent_hand_type = find_type(present_cards_opponent)
    print(my_hand_type)
    print(opponent_hand_type)

    if my_hand_type == opponent_hand_type:
        #todo
        if my_hand_type == "Straight Flush" or my_hand_type == "Straight":
            return compare_straight(present_cards_mine, present_cards_opponent)

        if my_hand_type == "Four of a Kind":
            return compare_four(present_cards_mine,present_cards_opponent)

        if my_hand_type == "FullHouse":
            return True

        if my_hand_type == "Flush":
            return True

        if my_hand_type == "Three of a Kind":
            return True

        if my_hand_type == "Two Pair":
            return True

        if my_hand_type == "One Pair":
            return True

        if my_hand_type == "High Card":
            return True

    return False

# 对比牌型大小
def compare_hand_type(my_hand, opponent_hand) -> bool:
    type_dict = {'Straight Flush': 8, 'Four of a Kind': 7, 'FullHouse': 6,
                 'Flush': 5, 'Straight':4, 'Three of a Kind': 3, 'Two Pair': 2,
                 'One Pair': 1, 'High Card': 0}
    return type_dict[my_hand] > type_dict[opponent_hand]

def compare_straight(present_cards_mine, present_cards_opponent) -> bool:
    my_hand_sorted = sorted_by_value(present_cards_mine)
    op_hand_sorted = sorted_by_value(present_cards_opponent)

    my_biggest = one_card()
    for i in range(len(my_hand_sorted)):
        #当前的第i张手牌张数不为0，且后两张牌的张数也不为0
        if my_hand_sorted[i][1] != 0 and my_hand_sorted[i+1][1] != 0 and my_hand_sorted[i+2][1] != 0:
            my_biggest = my_hand_sorted[i]
            break

    op_biggest = one_card()
    for i in range(len(op_hand_sorted)):
        #当前的第i张手牌张数不为0，且后两张牌的张数也不为0
        if op_hand_sorted[i][1] != 0 and op_hand_sorted[i+1][1] != 0 and op_hand_sorted[i+2][1] != 0:
            op_biggest = op_hand_sorted[i]
            break

    return my_biggest[0] > op_biggest[0]


def compare_four(present_cards_mine, present_cards_opponent) -> bool:
    my_hand_sorted = sorted_by_value(present_cards_mine)
    op_hand_sorted = sorted_by_value(present_cards_opponent)

    print(my_hand_sorted)
    print(op_hand_sorted)

    #先对比四条的大小
    my_biggest = one_card()
    found_my_biggest_card = False
    #再对比第二大的单牌的大小
    my_second_big = one_card()
    for i in range(len(my_hand_sorted)):
        #找到最大的牌后找第二大的单牌
        if found_my_biggest_card and my_hand_sorted[i][1] >=0:
            my_second_big = my_hand_sorted[i]
            break

        #当前的第i张手牌张数数量大于等于4
        if my_hand_sorted[i][1] >= 4:
            my_biggest = my_hand_sorted[i]
            found_my_biggest_card = True


    op_biggest = one_card()
    found_op_biggest_card = False
    op_second_big = one_card()
    for i in range(len(op_hand_sorted)):
        if found_op_biggest_card and op_hand_sorted[i][1] >=0:
            op_second_big = op_hand_sorted[i]
            break
        #当前的第i张手牌张数数量大于等于4
        if op_hand_sorted[i][1] >= 4:
            op_biggest = op_hand_sorted[i]
            found_op_biggest_card = True


    #如果四条的牌相同
    if my_biggest[0] == op_biggest[0]:
        #对比第二大的单牌
        print("my second big is " + str(my_second_big[0]))
        print("op second big is " + str(op_second_big[0]))
        return my_second_big[0] > op_second_big[0]

    return my_biggest[0] > op_biggest[0]
def compare_all_players(players_card):
    number_of_players=len(players_card)
    keys = list(players_card.keys())
    for i in range(number_of_players):
        for j in range(number_of_players):
            print(keys[i])
            print(keys[j])




