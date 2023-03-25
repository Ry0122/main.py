class computerOut():
    def ComputerOut(self):  # 电脑智能出牌
        global k, MyTurn
        playersCard[1].append(self.m_aCards[k]);  # 第14张牌

        result1 = Rule_Decide.canHu(playersCard[1]);  # 计算电脑手中各种牌型的数量,判断胡牌
        if (result1):  # 胡牌了
            return;  # 对家（电脑）不需要再出牌

        i = self.ComputerCard(playersCard[1]);  # 智能出牌
        # i=0;#总是出第一张牌，没有智能出牌
        card = playersCard[1][i]
        del (playersCard[1][i])
        # 加到电脑出过牌的数组
        playersOutCard[1].append(card)
        # outCardOrder(playersOutCard[1]);#整理出过的牌，Z轴深度问题

        # 电脑按花色理手中的牌
        Card.soker(playersCard[1]);

        k = k + 1  # 发过牌的总数
        MyTurn = True  # 轮到玩家