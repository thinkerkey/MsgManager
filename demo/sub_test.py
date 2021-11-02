import sys
sys.path.append("..")

# -----------sub demo code -------------
from manager import NodeRegister

node = NodeRegister()

def msg1_call(msg):
    # print(msg.author)
    # print(msg.version)
    print(msg.a[0])

def msg2_call(msg):
    # print(msg.author)
    # print(msg.version)
    print(msg)

node.sub("test1", msg1_call)
node.sub("test2", msg2_call)

node.subspin()
print("====")