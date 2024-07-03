# import warnings
# def deprecated(func):
#
#     def newFunc(*args, **kwargs):
#         warnings.warn('Call to deprecated function {}'.format(func.__name__),
#         category = DeprecationWarning)
#         return func(*args, **kwargs)
#     return newFunc
#
# @deprecated
# def prod(x,y):
#     'Returns product of two numbers'
#     return x*y
#
# print(prod(12,12))
# print(prod.__name__)
# print(prod.__doc__)

# import sys
# import builtins
#
# print(sys.builtins.__dict__keys())

# class MyError(Exception):
#     def __init__(self,value):
#         self.value = value
#
#     def __str__(self):
#         return repr(self.value)
#
# try:
#     print('Hello World')
#     raise MyError('OOPs something went wrong')
# except MyError as e:
#     print('Error message: ', e)

# print('{0:$>2d}*{1:$>2d}={2:$>2d}'.format(5,10,5*10))

# def smart_divide(func):
#     def wrapper(*args):
#         a, b = args
#         if b == 0:
#             print('oops! cannot divide')
#             return
#         return func(*args)
#     return wrapper
#
# @smart_divide
# def divide(a, b):
#     return a / b
#
# print(divide.__name__)
# print(divide(4, 16))

# print(divide (8,0))

import re
def f1(data):
    p=re.compile('(?P[A-Z]{2,3})(?P[0-9]{3})')
    return p.search(data)

obj=f1('CS 101')dept,
num=obj.group('dept'),obj.group('num')