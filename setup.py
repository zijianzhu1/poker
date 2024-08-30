def card_set_up():
    card_number=["AS","2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    card_suit=["Spades","Club","Hearts","Diamonds"]
    card_value=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    all_card={}
    for i in card_number:
        for j in card_suit:
            name=i+" "+j
           # card=one_card(i,j,card_value[card_number.index[i]])
            card = one_card()
            card.name=name
            card.card_number=i
            card.card_suit=j
            card.card_value=card_value[card_number.index(i)]
            all_card[name]=card
    #print_cards(all_card)
    return all_card
class one_card:
    #def __init__(self,card_number,card_suit,card_value):
    def __init__(self):
        self.card_number=0#=card_number
        self.card_suit=0#=card_suit
        self.card_value=0#=card_value
def print_cards(all_cards):
    for i in all_cards:
        print(i)
        print(all_cards[i].card_number)
        print(all_cards[i].card_suit)
        print(all_cards[i].card_value)
        print("")