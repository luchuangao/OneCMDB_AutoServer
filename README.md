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


