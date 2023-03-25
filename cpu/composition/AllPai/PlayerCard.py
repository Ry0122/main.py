

import operator




class PlayerCard():
    def __init__(self,player_card,card):
        self.player_cards = player_card
        self.cards = card
    #加载玩家的牌，出过的牌
    def PlayerCard(self):
        # 玩家的牌
        self.player_cards = [[],[]]
        # 玩家选定的牌
        # player_slectcard = Select_card
        # 按顺序存储到记录2个牌手的牌的数组
        for k in range(0, 26):
            self.player_cards[k%2].append(self.cards[k])
        return self.player_cards





