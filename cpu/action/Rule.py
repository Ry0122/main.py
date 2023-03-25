from cpu.action.hu_cpu import huMain



class Rule_Decide():
    def __init__(self, allPai):
        self.card = allPai

    def canHu(self,cards):  # 玩家手中牌playersCard[0]
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
        print(paiArray)
        hu = huMain()  # 胡牌算法类
        result = hu.Win(paiArray)  # 是否胡牌判断
        return result

    # a为所有牌，card为最后一张牌
    def canPeng(self, a, card):
        n = 0
        for i in range(0, len(a)):
            c = a[i]
            if (c.imageID == card.imageID):
                n += 1
        if n >= 2:
            return True
        return False

    def canGang(self, a, card):
        n = 0
        for i in range(0, len(a)):
            c = a[i]
            if (c.imageID == card.imageID):
                n += 1
        if n >= 3:
            return True
        return False

    def canChi(self, a, card):
        n = 0
        if card.m_nType == 4:  # 字牌不用判断吃
            return
        for i in range(0, len(a) - 1):  # 1**
            c1 = a[i]
            c2 = a[i + 1]
            if (c1.m_nNum == card.m_nNum + 1 and c1.m_nType == card.m_nType
                    and c2.m_nNum == card.m_nNum + 2 and c2.m_nType == card.m_nType):
                return True
        for i in range(0, len(a) - 1):  # *1*
            c1 = a[i]
            c2 = a[i + 1]
            if (c1.m_nNum == card.m_nNum - 1 and c1.m_nType == card.m_nType
                    and c2.m_nNum == card.m_nNum + 1 and c2.m_nType == card.m_nType):
                return True
        for i in range(0, len(a) - 1):  # **1
            c1 = a[i]
            c2 = a[i + 1]
            if (c1.m_nNum == card.m_nNum - 2 and c1.m_nType == card.m_nType
                    and c2.m_nNum == card.m_nNum - 1 and c2.m_nType == card.m_nType):
                return True
        return False





