
#记录出完牌的数组


class PlayerOutCard():
    def __init__(self,player_card,card):
        self.player_cards = player_card
        self.cards = card
    def PlayOutCard(self):
        #玩家出过的牌
        self.player_cards = []
        self.player_cards.append(self.cards)