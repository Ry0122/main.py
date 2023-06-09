"""
@File:CommunicationProducer.py
@Author:lcx
@Date:2020/10/714:34
@Desc:
"""
import logging
import os
import sys
import time

from confluent_kafka.cimpl import KafkaException

from ..communicationModuleImplement.componentInterface.queryInterface import QueryInterface

from ..communicationModuleInterface.CommunicationProducerInterface import CommunicationProducerInterface
from confluent_kafka import Producer
from ..communicationModuleInterface.communicationModuleException.Exceptions import *
import json

class CommunicationProducer(CommunicationProducerInterface, QueryInterface):

    conf = dict()
    topic = ""
    producer = ""
    def __init__(self, confPath: str):
        """

        :param confPath: this param is the path of the producer config file that you want to use. type: str
        """
        self.buildTime = str(time.time())
        self.logger = logging.getLogger("communicationProducer-{}".format(self.buildTime))
        self.debugLogEnableFlag = False
        self.retryLimit = None
        self.realtimeFlush = None
        if not os.path.exists(confPath):
            self.logger.fatal("no config file at {}".format(confPath))
            raise NoConfigFileException
        with open(confPath, 'r') as load_f:
            self.conf = json.load(load_f)
        if "debugLogEnable" in self.conf.keys():
            self.logger.info("get configuration: debugLogEnable = {}".format(self.conf["debugLogEnable"]))
            self.debugLogEnableFlag = (self.conf["debugLogEnable"].lower() == "true")
            self.conf.pop("debugLogEnable")
        if "retryLimit" in self.conf.keys():
            self.retryLimit = int(self.conf["retryLimit"])
            self.conf.pop("retryLimit")
            self.logger.info("get configuration: retryLimit = {}".format(self.retryLimit))
        if "realtimeFlush" in self.conf.keys():
            self.logger.info("get configuration: realtimeFlush = {}".format(self.conf["realtimeFlush"]))
            self.realtimeFlush = (self.conf["realtimeFlush"].lower() == "true")
            self.conf.pop("realtimeFlush")
        self.producer = Producer(self.conf)
        self.logger.info("producer instance built: buildTime={}, config={}, config at: {}".format(self.buildTime,
                                                                                                  confPath, str(self.conf)))

    def listTopics(self, topic: str = None, retryLimit: int = 1, timeout=0.5) -> list:
        result = None
        if self.retryLimit != None:
            retryLimit = self.retryLimit
        else:
            retryLimit = retryLimit
        retryTime = 0
        while retryTime < retryLimit:
            try:
                resultClusterMetadata = self.producer.list_topics(topic, timeout)
            except KafkaException as ke:
                retryTime += 1
                self.logger.error("get topic list failed, retry for {} time".format(str(retryTime)))
                time.sleep(1)
            else:
                result = list(resultClusterMetadata.topics.keys())
                self.logger.info("get topic list: {}".format(str(result)))
                break
        if result == None:
            self.logger.fatal("topic list query failed, retried {} times, waited for {} secs, found broker not "
                              "available, please check the connection.".format(str(retryLimit), str(retryLimit * 1.5)))
            raise TopicQueryFailed("topic list query failed, retried {} times, waited for {} secs, found broker not "
                                   "available, please check the connection.".format(str(retryLimit),
                                                                                    str(retryLimit * 1.5)))
        return result

    def send(self, topic: str, value: bytes, timeout: float = 1, key=None) -> None:

        if not type(value) == type(b"a"):
            raise WrongMessageValueType(type(value))
        else:
            self.producer.produce(topic, value, key)
            if self.realtimeFlush:
                self.producer.flush(timeout=timeout)
            if self.debugLogEnableFlag:
                self.logger.debug("producer instance (buildTime at {}) send a message at {}".format(self.buildTime,
                                                                                                    time.time()))

    def close(self, timeout: float = 1) -> None:
        self.producer.flush(timeout=timeout)
        self.logger.info("producer instance closed: buildTime={}".format(self.buildTime))
