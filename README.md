# OneCMDB_AutoServer
基于Django实现CMDB客户端

#### APP功能
* api 接收发送客户端数据
* backend 后台管理
* repository 操作数据库，数据处理

#### 创建数据库表

数据库设计的三层框架：  
* 数据库访问层:   
-User：增，删除，修改  

* 业务处理层:  
	-用户：  
	-授权：   
	 
* UI层:  
	-UI展示层  


1. Server 		    服务器信息表
2. Disk		        硬盘信息表
3. Asset		    资产信息表
4. NetworkDevice	网络设备表
5. IDC		        机房信息表
6. TAG		        资产标签表
7. NIC		        网卡信息表
8. Memory		    内存信息表
9. UserProfile	    用户信息表
10. UserGroup	    用户组表
11. BusinessUnit	业务线表
12. AdminInfo	    用户登陆相关信息
13. AssetRecord	    资产变更记录表
14. ErrorLog	    错误日志表


#### 资产入库

API项目中，views.py中对磁盘进行资产入库：
* 删除
* 增加
* 更新

#### API验证

为什么要做API验证？  
传输过程中，保证数据不被篡改。  

1. 发令牌：静态方式  
PS：隐患，容易被他人截获  

2. 改良，动态令牌【问题更严重】  
PS：隐患，容易被他人截获

3. 再动态令牌基础上，对时间和key做限制
记录，把访问过得key记录到字典中【使用redis即可】  
时间，将2s以外的key进行删除  

4. 数据加密（AES）  

总结：  
和Tornado中加密Cookie类似  
客户端创建动态KEY：md5(key+time)|time  
限制（添加）：  
第一关：时间  
第二关：算法规则
第三关：已访问记录2秒【redis来实现】  
第四关：对数据进行加密  

#### 后台管理

知识点：  
1. 序列化：
    * Django内置： from django.core import serializers  
    * JSON + 扩展


