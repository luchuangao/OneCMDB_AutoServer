import json
from django.shortcuts import render,HttpResponse
from repository import models

def asset(request):
    if request.method == 'POST':
        # 新资产信息
        server_info = json.loads(request.body.decode("utf-8"))
        hostname = server_info['basic']['data']['hostname']
        server_obj = models.Server.objects.filter(hostname=hostname).first()
        if not server_obj:
            return HttpResponse('当前主机名在资产中未录入')
        asset_obj = server_obj.asset

        # 资产表中以前资产信息
        # server_obj 可以找到服务基本信息（单条）
        # disk_list = server_obj.disk.all()

        # 处理：
        """
        1. 根据新资产和原资产进行比较：新["5","1"]      老["4","5","6"]
        2. 增加: [1,]   更新：[5,]    删除：[4,6]
        3. 增加：
                server_info中根据[1,],找到资产详细：入库
           删除：
                数据库中找当前服务器的硬盘：[4,6]

           更新：[5,]
                disk_list = [obj,obj,obj]

        s1 = set(["5","1"])
        s2 = set(["4","5","6"])
        # 增加: [1,]   更新：[5,]    删除：[4,6]
        print(s1-s2) #增加
        print(s1&s2) #更新
        print(s2-s1) #删除


                {
                    'data': {
                        '5': {'slot': '5', 'capacity': '476.939', 'pd_type': 'SATA', 'model': 'S1AXNSAFB00549A     Samsung SSD 840 PRO Series              DXM06B0Q'},
                        '3': {'slot': '3', 'capacity': '476.939', 'pd_type': 'SATA', 'model': 'S1AXNSAF912433K     Samsung SSD 840 PRO Series              DXM06B0Q'},
                        '4': {'slot': '4', 'capacity': '476.939', 'pd_type': 'SATA', 'model': 'S1AXNSAF303909M     Samsung SSD 840 PRO Series              DXM05B0Q'},
                        '0': {'slot': '0', 'capacity': '279.396', 'pd_type': 'SAS', 'model': 'SEAGATE ST300MM0006     LS08S0K2B5NV'},
                        '2': {'slot': '2', 'capacity': '476.939', 'pd_type': 'SATA', 'model': 'S1SZNSAFA01085L     Samsung SSD 850 PRO 512GB               EXM01B6Q'},
                        '1': {'slot': '1', 'capacity': '279.396', 'pd_type': 'SAS', 'model': 'SEAGATE ST300MM0006     LS08S0K2B5AH'}
                    },

                    'status': True
                }

                log_list = []

                dict_info = {'slot': '5', 'capacity': '476.939', 'pd_type': 'SATA', 'model': 'S1AXNSAFB00549A     Samsung SSD 840 PRO Series              DXM06B0Q'},
                obj
                    if obj.capacity != dict_info['capacity']:
                        log_list.append('硬盘容量由%s变更为%s' %s(obj.capacity,dict_info['capacity'])
                        obj.capacity = dict_info['capacity']
                    ...
                obj.save()

                models.xxx.object.create(detail=''.join(log_list))

        """

    return HttpResponse("...")