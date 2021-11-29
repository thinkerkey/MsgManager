from .utils import *
from types import FunctionType, MethodType
import json

class NodeRegister(object):
    def __init__(self) -> None:
        super().__init__()
        self.node = redis.StrictRedis(connection_pool=defual_pool)
        self.suber = self.node.pubsub()
        self.subcall = {}


    def pub(self, topic : str, msg):
        if isinstance(msg, dict):
            self.node.publish(topic, str(msg))
        elif isinstance(msg, object):
            # self.node.publish(topic, str(msg.__dict__))
            data = json.dumps(msg, default=lambda o:o.__dict__)
            self.node.publish(topic, data)
        else:
            print("不支持的消息类型")

    def sub(self, topic : str, callback: FunctionType):
        if isinstance(callback, (FunctionType,MethodType)):
            self.suber.subscribe(topic)
            self.subcall[topic] = callback
        else:
            print("需要指定回调函数")

    def subspin(self):
        for item in self.suber.listen():
            if item['type']=='message':
                data = item['data'].decode()
                data=eval(data)
                topic = item['channel'].decode()
                msg = CreateObjectFromMsg(data)
                self.subcall[topic](msg, topic)

    def unsub(self, topic : str):
        try:
            self.suber.unsubscribe(topic)
            self.subcall.pop(topic)
        except:
            print("没有找到当前话题:%s" %topic)





