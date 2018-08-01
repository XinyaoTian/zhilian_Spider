# -*- encoding:utf-8 -*-
#!/root/anaconda2/bin

# 适配crontab脚本命令
# 注意！ 这个文件要部署在与所有jobInfo.json相同的路径下
from pyhdfs import *
from func_pack import get_current_day
import logging
logging.basicConfig(level=logging.INFO)

client = HdfsClient(hosts="47.93.45.238,9000",user_name="hadoop",timeout=5)

ubuntuSrc = "./data/jobInfo_" + get_current_day() + ".json"
hadoopSrc = "/user/hadoop/" + "jobInfo_" + get_current_day() + ".json"

if client is not None:
    logging.info("Connect to hadoop cluster successful. ")
    client.copy_from_local(ubuntuSrc , hadoopSrc)
else:
    logging.error("Unable to connect to hadoop cluster. ")

if client.exists(hadoopSrc):
    logging.info(hadoopSrc + ":Files put successful.")