import json
from django.shortcuts import render, HttpResponse
from repository import models
from datetime import datetime
from datetime import date


class JsonCustomEncoder(json.JSONEncoder):

    def default(self, value):
        if isinstance(value, datetime):
            return value.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(value, date):
            return value.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, value)


def curd(request):
    return render(request, 'curd.html')


def curd_json(request):
    table_config = [
        {'q':'id', 'title':'ID'},
        {'q':'hostname', 'title':'主机名'},
        {'q':'create_at', 'title':'创建时间'},
        {'q':'asset__cabinet_num', 'title':'机柜号'},
        {'q':'asset__business_unit__name', 'title':'业务线名称'}
    ]

    values_list = []
    for row in table_config:
        values_list.append(row['q'])

    server_list = models.Server.objects.values(*values_list)
    ret = {
        'server_list':list(server_list),
        'table_config':table_config
    }

    return HttpResponse(json.dumps(ret, cls=JsonCustomEncoder))


















