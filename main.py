import student
from myfile import MyFile
import requests


def testLan(a,b,method):
    return method(a,b)

print(testLan(1,10,lambda x,y:x+y))
