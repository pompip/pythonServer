import student
from myfile import MyFile
import requests
import json

url = 'http://pompip.cn/article/list'
request = requests.post(url)

li = json.loads(request.text)

for o in li:
    print(o['title'])





