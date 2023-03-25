from cpu.action.control import event_control


class ActionControl():
    def __init__(self):
        # trigger控制器
        self.trig_ctrl = TriggerController(TriggerConfig.EEG_TYPE,
                                           TriggerConfig.TRIGGER_HANDLE,
                                           TriggerConfig.TRIGGER_PORT)
        # 事件管理器
        self.paradigm = event_control(self.trig_ctrl)
        # Kafka消费者
        self.consumer = KafkaConsumer('Algorithm2Stimulation', self.event_mng)

    def add_event_listener(self):
        self.event_mng.add_event_listener('FDBK', self.__recv_result)

    def start(self):
        self.add_event_listener()
        self.event_mng.start()
        logger.info('开始运行事件管理器')
        self.consumer.start()
        if self.paradigm is not None:
            self.paradigm.run()

    def __recv_result(self, event):
        msg = event.message
        self.paradigm.feedback_result = int(msg)
