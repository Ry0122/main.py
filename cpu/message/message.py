from cpu.event.event_manger import Event

import time

from loguru import logger

class Message:
    def __init__(self):
        self.round_flag = None
        self.state_flag = False
        self.get_card = 1
        self.select_card = 2
        self.out_card = 3
        self.state = self.get_card  # 状态
        self.last_message = None
        self.player_cards = None

    def message_kind(self,message,event):
        if self.state == self.get_card:
            #摸牌
            if message == "1":
                event.event_type = 'GET'
                event.message = '你要摸的牌'
            #碰牌
            if message == "2":
                event.event_type = 'PENG'
                event.message = '你要碰的牌'
            #吃牌
            if message == "3":
                event.event_type = 'CHI'
                event.message = '你要吃的牌'
            #胡牌
            if message == "4":
                event.event_type = 'HU'
                event.message = '游戏结束'


        if self.state == self.select_card:
            # 选择你的牌
            if message == "1":
                event.event_type = 'GSELECT'
                event.message = '你将要出的牌'

            # 胡牌
            if message == "2":
                event.event_type = 'HU'
                event.message = '游戏结束'

        if self.state == self.out_card:
            #选择你的牌
            if message == "1":
                event.event_type = 'GSELECT'
                event.message = '你将要出的牌'

            #胡牌
            if message == "2":
                event.event_type = 'HU'
                event.message = '游戏结束'


