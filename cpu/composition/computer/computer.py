import random
from cpu.action.Rule import Rule_Decide
from cpu.composition.AllPai.card import Card


class computer():
    def __init__(self,pai_get):
        self.m_aCards = pai_get
        self.playersCard = []


    def ComputerCard(cards):
        # 计算手中各种牌型的数量
        paiArray = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        for i in range(0, 14):
            card = cards[i]
            if (card.imageID > 10 and card.imageID < 20):  # 桶
                paiArray[0][0] += 1
                paiArray[0][card.imageID - 10] += 1
            if (card.imageID > 20 and card.imageID < 30):  # 条
                paiArray[1][0] += 1
                paiArray[1][card.imageID - 20] += 1
            if (card.imageID > 30 and card.imageID < 40):  # 万
                paiArray[2][0] += 1
                paiArray[2][card.imageID - 30] += 1
            if (card.imageID > 40 and card.imageID < 50):  # 字
                paiArray[3][0] += 1
                paiArray[3][card.imageID - 40] += 1
        # 电脑智能选牌
        # 1.判断字牌的单张 ，有则找到
        for j in range(1, 10):
            if (paiArray[3][j] == 1):
                # 获取在手中牌的位置下标
                k = Card.ComputerSelectCard(cards, 3 + 1, j)
                return k

        # 2.判断顺子，刻子（三张相同的）
        for i in range(0, 3):
            for j in range(1, 10):
                if (paiArray[i][j] >= 3):  # 刻子
                    paiArray[i][j] -= 3
                if (j <= 7 and paiArray[i][j] >= 1 and paiArray[i][j + 1] >= 1
                        and paiArray[i][j + 2] >= 1):  # 顺子
                    paiArray[i][j] -= 1
                    paiArray[i][j + 1] -= 1
                    paiArray[i][j + 2] -= 1

        # 3.判断单张非字牌（饼，条，万） ，有则找到
        for i in range(0, 3):
            for j in range(1, 10):
                if (paiArray[i][j] == 1):
                    # 获取在手中牌的位置下标
                    k = Card.ComputerSelectCard(cards, i + 1, j)
                    return k

        # 4.判断两张牌（饼，条，万，包括字牌） ，有则找到,拆双牌
        for i in range(3, -1):
            for j in range(1, 10):
                if (paiArray[i][j] == 2):
                    # 获取在手中牌的位置下标
                    k = Card.ComputerSelectCard(cards, i + 1, j)
                    return k

        # 5.如果以上情况均没出现则随机选出1张牌
        k = random.randint(0, 13)  # 随机选出1张牌
        return k


    def ComputerOut(self,k):  # 电脑智能出牌
        self.playersCard.append(self.m_aCards[k]);  # 第14张牌

        result1 = Rule_Decide.canHu(self.playersCard);  # 计算电脑手中各种牌型的数量,判断胡牌
        if (result1):  # 胡牌了
            return;  # 对家（电脑）不需要再出牌

        i = self.ComputerCard(self.playersCard);  # 智能出牌
        # i=0;#总是出第一张牌，没有智能出牌
        card = self.playersCard[i]
        del (self.playersCard[i])

        # outCardOrder(playersOutCard[1]);#整理出过的牌，Z轴深度问题

        # 电脑按花色理手中的牌
        Card.soker(self.playersCard);





