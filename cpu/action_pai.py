from tkinter.messagebox import *

from Card import Card

def xuan_card():
    global MyTurn,PlayerSelectCard,m_LastCard
    card = Card()
    if (m_LastCard == None):  # 未选过的牌
        m_LastCard = card
        PlayerSelectCard = card
    else:  # 已经选过的牌
        m_LastCard = card
        PlayerSelectCard = card

def out_card():
    global MyTurn, PlayerSelectCard, m_LastCard
    if (MyTurn == False):  # 没轮到自己出牌
        return
    if (PlayerSelectCard == None):  # 还没选择出的牌
        showinfo(title="提示", message="还没选择出的牌")
        return
    if not(PlayerSelectCard==None):
        playersOutCard[0].append(PlayerSelectCard);
        #玩家牌减少
        del(playersCard[0][PlayerSelectCard.cardID])
        #playersCard[0].remove(PlayerSelectCard);
        m_LastCard=None
        PlayerSelectCard=None
        MyTurn = False
        ComputerOut( ) #电脑智能出牌
        fun2()

def chi_card():
    global MyTurn
    card=playersOutCard[1][len(playersOutCard[1])-1];
    playersCard[0].append(card);#第14张牌
    #监听第14张牌
    sortPoker2(playersCard[0]);#按顺序存储到记录玩家牌手的牌的数组
    result1=ComputerCardNum(playersCard[0]);#计算手中各种牌型的数量,判断胡牌
    if(result1):#胡牌了
        showinfo(title="恭喜",message="玩家Win!")
        return #玩家不需要再出牌
    MyTurn=True

def get_card():
    global k
    global playersCard,MyTurn
    #玩家按花色理手中的牌
    m_aCards[k].MoveTo(90 + 55 * 13, 500)
    playersCard[0].append(m_aCards[k])    #第14张牌
    #监听第14张牌
    sortPoker2(playersCard[0]) #按顺序存储到记录牌手的牌的数组
    result1=ComputerCardNum(playersCard[0]) #计算手中各种牌型的数量,判断胡牌
    if(result1):#胡牌了
        showinfo(title="恭喜",message="玩家Win!")
        return #玩家不需要再出牌
    k=k+1  #下一张要摸的牌在m_aCards索引号
    MyTurn=True