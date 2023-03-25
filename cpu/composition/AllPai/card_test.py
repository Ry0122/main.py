from card import Card
m_aCards = []
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
            card = Card(m_nType, num)  # 创建“饼条万”牌
            # card.MoveTo(100+num*60,100+m_nType*80)
            m_aCards.append(card)  # 将牌添加到数组

cardtype = 4  # 字牌
for num in range(1, 8):  # 1--7
    FrontURL = "res/nan/4"
    FrontURL = FrontURL + str(num)  # URL地址
    FrontURL = FrontURL + ".png"
    for n in range(1, 5):  # 每种牌4张
        card = Card(cardtype, num)  # 创建字牌
        # card.MoveTo(100+num*60,100+4*80)
        # card["state"]=DISABLED
        m_aCards.append(card)  # 将牌添加到数组

print(m_aCards)