import sys
sys.path.append("..")

# -----------pub demo code -------------
from manager import NodeRegister
from msg.pointcloud import PointCloud
from msg.bbox2d import BoundingBox2D
import time
msg = {
    "author" : "yuangao",
    "version" : 1.0
}

msg2 = {
    "author" : "chengxiaoqiang",
    "version" : 1.2
}



node = NodeRegister()
obj = BoundingBox2D()

while True:
    node.pub("test1", obj)
    print("pub msg:", obj)
    time.sleep(1)
    print("pub msg2:", msg2)
    node.pub("test2", msg2)
    time.sleep(1)