from wsgiref.simple_server import make_server
import json
def app(request,response):
    response("200 ok", [('Content-Type', 'application/json')])
    re ={}
    for key ,value in request.items():
        re[str(key)]=str(value)

    print(type(request))
    print(type(response))
 
    
    
    return [json.dumps(re).encode("utf-8")]

make_server('',8080,app).serve_forever()