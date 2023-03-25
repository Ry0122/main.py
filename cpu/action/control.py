from cpu.composition.AllPai.card import Card
from cpu.composition.AllPai.PlayerCard import PlayerCard
from cpu.Game.Rule.Rule import Rule_Decide
from cpu.Game.Rule.computer import computer


class event_control():
    def __init__(self,event):
        self.PlayerSelectCard = None
        self.allcard = []
        self.playercard = [[],[]]
        self.playeroutcard = [[],[]]
        self.event_get = event
        self.k = 26
        self.result_Hu = False
        self.result_Gang = False
        self.result_Peng = False
        self.result_Chi = False
        self.result_mopai = False
        self.step = self.init_step()

    def run(self):
        self.init_step()

    def init_step(self):
        #生成所有牌
        allcard = Card.LoadCards()
        #生成玩家的牌
        self.playercard = PlayerCard.PlayerCard(allcard)
        self.result_mopai = True
        #self.step = self.mopai()


    def mopai(self):
        self.playercard[0].appened(self.allcard)
        self.result_Hu = Rule_Decide.canHu(self.playercard[0])
        self.result_Gang = Rule_Decide.canGang(self.allcard[self.k],self.playercard[0])
        self.step = self.xuanpai()

    def xuanpai(self):
        #出牌有效
        self.PlayerSelectCard = Card


    def dengdai(self):
        self.result_Gang = Rule_Decide.canGang(self.allcard[self.k], self.playercard[0])
        self.result_Peng = Rule_Decide.canPeng(self.allcard[self.k], self.playercard[0])
        self.result_Chi = Rule_Decide.canChi(self.allcard[self.k], self.playercard[0])
        self.result_mopai = True
        self.step = self.xuanpai()

    def dapai(self):
        if (self.PlayerSelectCard == None):  # 还没选择出的牌
            return
        if not (self.PlayerSelectCard == None):
            self.k = self.k +1
            self.playeroutcard[0].append(self.PlayerSelectCard)
            del (self.playersCard[0][self.PlayerSelectCard.cardID])
            computer.computerout(self.PlaySelectCard,self.playercard[1])
            self.k = self.k + 1





