import redis

defual_pool = redis.ConnectionPool(host='localhost', port=6379, db=0)

# class CreateObjectFromMsg(dict):
#     def __getattr__(self, name):
#         return self[name]

#     def __setattr__(self, name, value):
#         self[name] = value


class CreateObjectFromMsg(object):
    def __init__(self, d):
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
               setattr(self, a, [CreateObjectFromMsg(x) if isinstance(x, dict) else x for x in b])
            else:
               setattr(self, a, CreateObjectFromMsg(b) if isinstance(b, dict) else b)
