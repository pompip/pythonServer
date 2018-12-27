import json
from urllib import request

url = 'http://localhost:8080'
# request = requests.post(url)

# li = json.loads(request.text)

# for key,value in li.items():
#     if '\\' in str(value) :
#         continue
#     print("%s---->%s"%(key,value))



with request.urlopen(url,b"") as rep:
    print(rep.read())
    print(type(rep))

    print(rep.geturl())
    print(rep.info())
    print(rep.peek())



# j = json.loads(b)
# print(type(j))

# print(j["REQUEST_METHOD"])