class Player_board:
    """
    inicilize the class
    """
    def __init__(self,username,player_card):
        self.username=username
        self.player_card=player_card

    def update_card(self,player_card):
        self.player_card=player_card
    def update_name(self,username):
        self.username=username