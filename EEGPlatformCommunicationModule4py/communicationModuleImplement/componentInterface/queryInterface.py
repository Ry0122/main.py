from abc import ABCMeta, abstractmethod


class QueryInterface(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def listTopics(self, topic: str = None, retryLimit: int = 1, timeout: float = 0.5) -> list:
        """

        :param topic: this param is the topic name that you want to inquire, type: str
        :param retryLimit: todo:
        :param timeout: this param is the inquire timeout, type: int
        :return: Map of topics indexed by the topic name. Value is TopicMetadata object in confluent-kafka.
        """
        pass