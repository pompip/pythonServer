from wsgiref.simple_server import make_server
import json
def app(request,response):
    response("200 ok", [('Content-Type', 'text/json')])
    # print(request)
    line ="<html><body>"
    for key ,value in request.items():
        line+="<div>%s---->%s</div><br>"%(key,value)
    # map(lambda key,value:line+="<div>%s---->%s</div><br>"%(key,value),request)

    line+="</body></html>"
    
    
    return [json.dumps(request).encode("utf-8")]

make_server('',8080,app).serve_forever()