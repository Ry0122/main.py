"""
@File:CommunicationInitial.py
@Author:lcx
@Date:2020/10/714:38
@Desc:
"""
import os
import sys

from .CommunicationConsumer import CommunicationConsumer
from .CommunicationProducer import CommunicationProducer
from ..communicationModuleImplement.componentInterface.queryInterface import QueryInterface

# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)
from confluent_kafka.cimpl import KafkaException, KafkaError

from ..communicationModuleInterface.CommunicationInitialInterface import CommunicationInitialInterface
from confluent_kafka.admin import AdminClient, NewTopic
import json
from ..communicationModuleInterface.communicationModuleException import Exceptions


class CommunicationInitial(CommunicationInitialInterface):

    @staticmethod
    def topicQuery(communicationCharactor: QueryInterface) -> list:
        """

        :param communicationCharactor: a instance of interface "QueryInterface"
        :return: a list of topic name
        """
        try:
            return communicationCharactor.listTopics()
        except KafkaException as kafkae:
            raise Exceptions.TopicQueryFailed(kafkae)

    @staticmethod
    def topicCreate(topic: str, confPath: str, num_partitions=1, replication_factor=1):
        """

        this method will retry for "retryLimit" (a param which is set in config) times until success
        :param topic: this param is the name of the topic that you want to create. type: str
        :param confPath: broker configuration, "bootstrap.servers" must be set
        :param num_partitions: this param is the partition number of the topic that you want to create.
        default: 1, type: int
        :param replication_factor: this param is the replication number of the topic that you want to create.
        default: 1, type: int
        :return: a dict of futures for each topic, keyed by the topic name. type: dict(<topic_name, future>)
        """
        retryLimit = 0
        if not os.path.exists(confPath):
            raise Exceptions.NoConfigFileException("NoConfigFileException in {}".format(confPath))
        with open(confPath, 'r') as load_f:
            conf = json.load(load_f)
        if not "bootstrap.servers" in conf.keys():
            raise Exceptions.WrongConfigContextException("need bootstrap.servers")
        if "retryLimit" in conf.keys():
            retryLimit = int(conf["retryLimit"])
            conf.pop("retryLimit")

        retryTime = -1
        exception = None
        while retryTime < retryLimit:
            adminClient = AdminClient(conf)
            new_topics = [NewTopic(topic, num_partitions, replication_factor)]
            fs = adminClient.create_topics(new_topics)
            for topic, f in fs.items():
                try:
                    f.result(timeout=1)  # The result itself is None
                    return topic
                except KafkaException as ke:
                    # topic already exits.
                    if ke.args[0].code() == KafkaError.TOPIC_ALREADY_EXISTS:
                        return topic
                except Exception as e:
                    retryTime += 1
                    exception = e
        if exception:
            raise Exceptions.TopicCreateFailed(exception)

    @staticmethod
    def topicDelete(topic: str, confPath: str):
        """

        :param topic: this param is the name of the topic that you want to create. type: str
        :param confPath: broker configuration, "bootstrap.servers" must be set
        :return: a dict of futures for each topic, keyed by the topic name. type: dict(<topic_name, future>)
        """
        if not os.path.exists(confPath):
            raise Exceptions.NoConfigFileException
        with open(confPath, 'r') as load_f:
            conf = json.load(load_f)
        if not "bootstrap.servers" in conf.keys():
            raise Exceptions.WrongConfigContextException
        adminClient = AdminClient(conf)
        fs = adminClient.delete_topics([topic], request_timeout=1)
        for topic, f in fs.items():
            try:
                f.result()  # The result itself is None
                return topic
            except Exception as e:
                raise Exceptions.TopicDeleteFailed(e)
