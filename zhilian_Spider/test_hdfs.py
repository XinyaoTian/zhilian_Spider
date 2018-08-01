# -*- encoding:utf-8 -*-
from pyhdfs import *
from func_pack import get_current_day
import requests

print "jobInfo_" + get_current_day()

client = HdfsClient(hosts="47.93.45.238,9000",user_name="hadoop",timeout=5)
print client.get_home_directory()
print client.get_active_namenode()
# fo = HdfsClient(hosts="47.93.45.238,50070",user_name="hadoop")
# print fo.copy_from_local("D:/Jupyter notebook/ipynb_materials/src/speech_text.txt","/user/hadoop")
# print client.copy_from_local("D:/Jupyter notebook/ipynb_materials/src/speech_text.txt","/user/hadoop")
#
# print client.get_xattrs("/user/hadoop")
#
# # 查询
print client.listdir("/user/hadoop")

# client.append("/user/hadoop/speech_text.txt","\n hello! there's a new message!\n")

# 从本地上传文件至集群
# ToDo 部署后注意要配置Ubuntu中 /etc/hosts 中的IP地址到主机名的映射
# client.copy_from_local("D:/Jupyter notebook/ipynb_materials/src/speech_text.txt","/user/hadoop/speech_text.txt")

response = client.open("/user/hadoop/speech_text.txt")
# print response.getheader
print response.read()



# print client.listdir("/user/hadoop")

# print "Hello World"