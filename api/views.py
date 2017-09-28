import json
from django.shortcuts import render,HttpResponse


def asset(request):
    if request.method == 'POST':
        server_info = json.loads(request.body.decode("utf-8"))
        for k,v in server_info.items():
            print(k,v)
    return HttpResponse("...")