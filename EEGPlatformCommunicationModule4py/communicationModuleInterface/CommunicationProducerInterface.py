"""
@File:CommunicationProducerInterface.py
@Author:lcx
@Date:2020/10/714:37
@Desc:
"""
from abc import ABCMeta, abstractmethod
class CommunicationProducerInterface(metaclass=ABCMeta):

    @abstractmethod
    def send(self, topic: str, value: bytes, timeout: float = 1, key=None) -> None:
        """

        :param topic: this param is the topic name that you want to send message to, type: str
        :param value: this param is the message context, type: bytes
        :param timeout: this param is the timeout for sending a msg, but that doesn't mean the msg sending is failed
        :param key: this param isn't used currently
        :return: None
        """
        pass

    @abstractmethod
    def close(self, timeout: float = 1) -> None:
        """

        release resources
        :param: timeout: this param is the flush timeout before closed
        :return: None
        """
        pass