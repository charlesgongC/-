# 使用__new__
class SingleTon(object):
    _instance = None
    def __new__(cls,*args,**kwargs):
        if not cls._instance:
            cls._instance = super(SingleTon,cls).__new__(cls,*args,**kwargs)
        return cls._instance

# 元类
class MymetaClass(type):
    def __call__(self,*args,**kwargs):
        if not getattr(self,'_instance'):
            self._instance = super().__call__(*args,**kwargs)
        return self._instance

# class Mysql(metaclass = MymetaClass):
#     _instance =None
#     def __init__(self,host,port):
#         self.host = host
#         self.port = port

# 使用装饰器
from functools import wraps

def single_ton(cls):
    _instance = {}

    @wraps(cls)
    def single(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return single

@single_ton
class Mysql():
    def __init__(self,host,port):
        self.host = host
        self.port = port


# m1 = Mysql('127.0.0.1',3306)
# m2 = Mysql('127.0.0.2',3306)
# print(m2.host)
# print(id(m1),id(m2))

# 使用类方法
# class Mysql:
#     _instance = None
#     def __init__(self,host,port):
#         self.host = host
#         self.port = port
#     @classmethod
#     def singleton(cls):
#         if not cls.singleton:
#             _instance = cls('127.0.0.1',3306)
#         return cls._instance

# 使用模块
# class SingleTon(object):
#     def __init__(self, val):
#         self.val = val

# single = SingleTon(2)