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
        {
            'q':'id',
            'title':'ID',
            'display': False,
            'text':{
                 'tpl':"{n1}",
                 'kwargs':{'n1':'@id'}
            }
         },
        {
            'q':'hostname',
             'title':'主机名',
             'display': True,
             'text':{
                 'tpl':"{n1}-{n2}",
                 'kwargs':{'n1':'@hostname','n2':'@id'}
             }
         },
        # 页面显示：标题：操作：删除，标记：a标签
        {
            'q': None,
            'title': '操作',
            'display': True,
            'text':{
                'tpl':"<a href='/del?nid={nid}'>删除</a>",
                'kwargs':{'nid':'@id'}
            }
        },
    ]
    # 普通值：原值存放即可
    # @值  ： 根据id，根据获取当前行对应数据

    values_list = []
    for row in table_config:
        if not row['q']:
            continue
        values_list.append(row['q'])

    server_list = models.Server.objects.values(*values_list)
    ret = {
        'server_list':list(server_list),
        'table_config':table_config
    }

    return HttpResponse(json.dumps(ret, cls=JsonCustomEncoder))


















