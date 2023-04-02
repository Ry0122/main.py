from loguru import logger
from cpu.Game.Class_Card import Card
from cpu.event.event_manger import EventManager, Event
from cpu.message.message import Message
from cpu.communication.CommunicationConsumer import KafkaConsumer


class ActionControl():
    def __init__(self):
        self.k = 0
        self.all_pai = Card().LoadCards()
        self.player_cards = [[], []]
        for self.k in range(0, 26):
            self.player_cards[self.k % 2].append(self.all_pai[self.k])
        # trigger控制器
        '''self.trig_ctrl = TriggerController(TriggerConfig.EEG_TYPE,
                                           TriggerConfig.TRIGGER_HANDLE,
                                           TriggerConfig.TRIGGER_PORT)'''
        # 事件管理器
        self.event_mng = EventManager()
        self.Message = Message()
        # Kafka消费者
        self.consumer = KafkaConsumer('Algorithm2Stimulation', self.event_mng)

    def add_event_listener(self):
        #接收六种消息格式 吃，摸牌，胡行为，信息打的牌的行为，选牌行为信息
        self.event_mng.add_event_listener('ACGT', self.__recv_result_get)
        self.event_mng.add_event_listener('ACSP', self.__recv_result_select)
        self.event_mng.add_event_listener('ACOT', self.__recv_result_out)
        self.event_mng.add_event_listener('ACPG', self.__recv_result_peng)
        self.event_mng.add_event_listener('ACHU', self.__recv_result_hu)

    def start(self):
        self.add_event_listener()
        self.event_mng.start()
        logger.info('开始运行事件管理器')
        self.consumer.start()

    def rec_result_get_card(self, event):
        msg = event.message


    def rec_result_select_card(self,event):
        msg = event.message

    def rec_result_out_card(self,event):
        msg = event.message