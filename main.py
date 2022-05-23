# import time
# # import datetime
# # import flask
# # a=flask.Flask
# # v=datetime.time
# # tt=time.asctime()
# #
# # print(tt)
# #
# # list=[13,12,23,34,45,64,34,77]
# #
# # for i in list:
# #     if i>20:
# #         print(i)
# #         time.sleep(1)
# # tt=time.asctime()
# # print(tt)
import  binascii
import math
# mm=['a','b','c','d','e','f','g']
# pp = dict(zip(mm,range(6)))
# # print(pp)
# a = ("John", "Charles", "Mike","kaushik")
# b = ("Jenny", "Christy", "Monica")
#
# #
# print(tuple(zip(a, b)))
# print(list(zip(a, b)))
# print(dict(zip(a, b)))

import json
import requests

def speak(str):

    from win32com.client import Dispatch
    a = Dispatch("SAPI.spvoice")
    a.speak(str)


speak("hello i am kaushik")
