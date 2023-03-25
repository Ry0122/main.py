import random
from cpu.action.Rule import Rule_Decide
from operator import index

from Card import Card
import operator
from tkinter import *

def LoadCards():  # 加载136张麻将牌到舞台
    global k
    m_aCards = []
    playersCard = [[], []]  # 记录2个牌手拿到的牌
    playersOutCard = [[], []]  # 记录2个牌手出过的牌
    k = 0  # 记录已发出牌的个数
    m_LastCard = None  # 用户是否选过牌
    PlayerSelectCard = None  # 用户选中的牌
    MyTurn = True  # 轮到玩家出牌(游戏开始玩家先出牌）
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
    random.shuffle(m_aCards)
    for k in range(0, 26):  # while(k<26):
        playersCard[(k%2)].append(m_aCards[k])

    # 玩家按花色理手中的牌
    sortPoker2(playersCard[0])
    # 电脑按花色理手中的牌
    sortPoker2(playersCard[1])
    k = 26  # 发牌数量


def  sortPoker2(cards):        #按花色理牌手手中的牌
    n=len(cards)               #元素（牌）的个数
    for  index  in range(0,n): #重新设置各张牌在场景中的位置
        print(cards[index].imageID,end=" ")
    #排序
    #sorted(cards, key=lambda card: card.imageID)   # sort by age
    cards.sort(key=operator.attrgetter('imageID'))

    print("\n排序后:")
    for  index  in range(0,n): #重新设置各张牌在场景中的位置
        print(cards[index].imageID,end=" ")
        cards[index].cardID=index
# ------------


