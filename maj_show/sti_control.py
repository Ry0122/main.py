import threading
from loguru import logger
from paradim.maj_ssvp import SSVEP
from communication.CommunicationConsumer import KafkaConsumer
from cpu.communication.CommunicationProducer import KafkaProducer
from event.event_manger import EventManager


class StimulationControl:

    def __init__(self):
        # trigger控制器
        #self.trig_ctrl = TriggerController(TriggerConfig.EEG_TYPE,
        #                                   TriggerConfig.TRIGGER_HANDLE,
        #                                   TriggerConfig.TRIGGER_PORT)
        # 范式
        self.paradigm = SSVEP()
        # 事件管理器
        self.event_mng = EventManager()
        # Kafka消费者
        self.produce = KafkaProducer(topic='command')

        self.consumer = KafkaConsumer(topic='pai_num', event_mng=self.event_mng)
        self.consumer2 = KafkaConsumer(topic='pai_control', event_mng=self.event_mng2)

    def add_event_listener(self):
        self.event_mng.add_event_listener('FDBK', self.__recv_result)


    def start(self):
        self.add_event_listener()
        self.event_mng.start()
        self.event_mng2.start()
        logger.info('开始运行事件管理器')
        self.consumer.start()
        self.consumer2.start()

        if self.paradigm is not None:
            self.paradigm.run()


    def __recv_result(self, event):
        msg = event.message
        self.paradigm.feedback_result = int(msg)

