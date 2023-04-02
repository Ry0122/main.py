import threading
from loguru import logger
from paradim.maj_ssvp import SSVEP
from communication.CommunicationConsumer import KafkaConsumer
from cpu.communication.CommunicationProducer import KafkaProducer
from event.event_manger import EventManager


class StimulationControl:

    def __init__(self):
        # trigger控制器
        # self.trig_ctrl = TriggerController(TriggerConfig.EEG_TYPE,
        #                                   TriggerConfig.TRIGGER_HANDLE,
        #                                   TriggerConfig.TRIGGER_PORT)
        # 范式
        self.paradigm = SSVEP()
        # 事件管理器
        self.event_mng = EventManager()
        self.event_mng2 = EventManager()
        # Kafka生产者;产生命令
        self.produce = KafkaProducer(topic='command')
        self.produce = KafkaProducer(topic='select_card')
        # Kafka消费者
        self.consumer = KafkaConsumer(topic='pai_num', event_mng=self.event_mng)
        self.consumer2 = KafkaConsumer(topic='action', event_mng=self.event_mng2)

    def add_event_listener(self):
        self.event_mng.add_event_listener('BEHA', self.__recv_result_card)
        # 接收行为的信息
        self.event_mng2.add_event_listener('PENG', self.__recv_result_action)

    def start(self):
        self.add_event_listener()
        self.event_mng.start()
        self.event_mng2.start()
        logger.info('开始运行事件管理器')
        self.consumer.start()
        self.consumer2.start()

        if self.paradigm is not None:
            self.paradigm.run()

    def __recv_result_card(self, event):
        msg = event.message
        self.paradigm.run()
        self.paradigm.maj_create(msg)

    def __recv_result_action(self, event):
        msg = event.message
        self.paradigm.run()
        self.paradigm.maj_create()
        self.paradigm.action_create()
