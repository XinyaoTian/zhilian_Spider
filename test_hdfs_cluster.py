# -*- encoding:utf-8 -*-
from pyhdfs import *

client = HdfsClient(hosts="47.93.45.238,9000",user_name="hadoop",timeout=5)

print client.listdir("/user/hadoop/")

# client.delete("/user/hadoop/jobInfo_zhilian.csv")
#
# print client.listdir("/user/hadoop/")

if client.exists("/user/hadoop/jobInfo_zhilian.csv"):
    response = client.open("/user/hadoop/jobInfo_zhilian.csv")
    print response.read()
else:
    print "No such file."