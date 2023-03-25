import random


class Card():
    def __init__(self):
        self.m_nNum = None
        self.m_nType = None
        self.all_pai = []

    # 构造函数，参数type指定牌的类型，参数num指定牌的点数
    def Card(self, cardtype, num):
        self.m_nType = cardtype  # 牌的类型 饼=1 条=2 万=3 字牌=4
        self.m_nNum = num  # 牌的点数（1到9）
        # 根据牌的类型及编号来设置牌文件的路径及文件名

        if self.m_nType == 1:  # 桶（饼）
            FrontURL = "res/nan/1"
        elif self.m_nType == 2:  # 条
            FrontURL = "res/nan/2"
        elif self.m_nType == 3:  # 万
            FrontURL = "res/nan/3"
        elif self.m_nType == 4:  # 字牌
            FrontURL = "res/nan/4"
        self.imageID = self.m_nType * 10 + self.m_nNum  # 牌自己图像编号ID
        FrontURL = FrontURL + str(self.m_nNum)  # URL地址
        FrontURL = FrontURL + ".png"
        # 牌自己图像编号ID
        return self.imageID

    def LoadCards(self) -> object:
        for m_nType in range(1, 4):  # 1--3代表饼条万
            for num in range(1, 10):  # 1--9
                # 根据牌的类型及编号来设置牌文件的路径及文件名
                if m_nType == 1:  # 桶（饼）
                    FrontURL = "res/nan/1"
                elif m_nType == 2:  # 条
                    FrontURL = "res/nan/2"
                elif m_nType == 3:  # 万
                    FrontURL = "res/nan/3"

                FrontURL = FrontURL + str(num)  # URL地址
                FrontURL = FrontURL + ".png"
                for n in range(1, 5):  # 每种牌4张
                    card = self.Card(m_nType, num)  # 创建“饼条万”牌
                    # card.MoveTo(100+num*60,100+m_nType*80)
                    self.all_pai.append(card)  # 将牌添加到数组

        cardtype = 4  # 字牌
        for num in range(1, 8):  # 1--7
            FrontURL = "res/nan/4"
            FrontURL = FrontURL + str(num)  # URL地址
            FrontURL = FrontURL + ".png"
            for n in range(1, 5):  # 每种牌4张
                card = self.Card(cardtype, num)  # 创建字牌
                # card.MoveTo(100+num*60,100+4*80)
                # card["state"]=DISABLED
                self.all_pai.append(card)  # 将牌添加到数组

        random.shuffle(self.all_pai)
        return self.all_pai
