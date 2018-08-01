# -*- coding: utf-8 -*-
# 注意json文件以一个空的字典{}结尾！
import json
import codecs
import pymongo
from scrapy.conf import settings
import logging
from pyhdfs import *

from func_pack import get_current_day

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class jobInfo_FeedExportLocalCsv(object):
    pass


# 在hdfs集群上以CSV格式存储数据
# 由于频繁的发起hdfs连接请求，因此经常出现丢包情况，故放弃使用这个函数
class jobInfo_WriteHdfsCsvPipeline(object):
    def __init__(self):
        # 利用IP+Port,连接集群上的Namenode
        self.client = HdfsClient(hosts="47.93.45.238,9000", user_name="hadoop", timeout=5)
        self.count = 0
        # 若存储数据的文件已经存在
        if self.client.exists("/user/hadoop/jobInfo_zhilian.csv"):
            logging.info("Open the file src='/user/hadoop/jobInfo_zhilian.csv'")
            pass
        else: #若存储数据的文件不存在
            # 在hadoop集群上建立这个存储文件
            self.client.create("/user/hadoop/jobInfo_zhilian.csv","")
            logging.info("Create the file path='/user/hadoop/jobInfo_zhilian.csv'")
            # 初始化csv的目录结构
            self.client.append("/user/hadoop/jobInfo_zhilian.csv",
                          "," +
                          "job_url," +
                          "job_name," +
                          "salary," +
                          "publish_date" +
                          "work_experience," +
                          "job_nature," +
                          "education_degree," +
                          "job_category," +
                          "company_name," +
                          "company_scale," +
                          "company_nature," +
                          "company_industrial," +
                          "company_webpage," +
                          "company_address," +
                          "feedback_rate," +
                           "scrape_time" + "\n"
                          )

    def process_item(self, item ,spider):
        self.count += 1
        self.client.append("/user/hadoop/jobInfo_zhilian.csv",
                           str(self.count) + "," +
                           str(item["job_url"]) + "," +
                           str(item["job_name"]) + "," +
                           str(item['salary']) + "," +
                           str(item['publish_date']) + "," +
                           str(item['work_experience']) + "," +
                           str(item['job_nature']) + "," +
                           str(item['education_degree']) + "," +
                           str(item['job_category']) + "," +
                           str(item['company_name']) + "," +
                           str(item['company_scale']) + "," +
                           str(item['company_nature']) + "," +
                           str(item['company_industrial']) + "," +
                           str(item['company_webpage']) + "," +
                           str(item['company_address']) + "," +
                           str(item['feedback_rate']) + "," +
                           str(item['scrape_time']) + "\n"
                           )
        return item


    # 要特别注意这两个函数名，因为框架需要调用 因此名字必须是open_spider 一点都不能错
    def open_spider(self, spider):
        pass
        # print "Spider start!"

    #同样 close_spider 的函数名也必须是这个，否则框架是无法识别的
    def close_spider(self, spider):
        pass
        #print "Close the spider pipeline"



#此管道处理函数 用于处理 distinct_spider.py 中 的爬虫数据
class jobToday_JsonWithEncodingPipeline(object):
    def __init__(self):
        self.file = codecs.open('./jobInfo_today.json', 'w', encoding='utf-8')
        self.file.write('[')
        #print "Open the spider pipeline"

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.file.write(line)
        return item

    #要特别注意这两个函数名，因为框架需要调用 因此名字必须是open_spider 一点都不能错
    def open_spider(self,spider):
        pass
        #print "Spider start!"

    #同样 close_spider 的函数名也必须是这个，否则框架是无法识别的
    def close_spider(self, spider):
        #print "Close the spider pipeline"
        #注意Json文件以一个空的数据结构结尾
        self.file.write('{}]')
        self.file.close()

#此管道处理函数 用于处理 overview_spider.py 中 的爬虫数据
class jobInfo_JsonWithEncodingPipeline(object):
    def __init__(self):
        fname = "./data/jobInfo_" + get_current_day() + ".json"
        self.file = codecs.open(fname, 'w', encoding='utf-8')
        self.file.write('[')
        #print "Open the spider pipeline"

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.file.write(line)
        return item

    #要特别注意这两个函数名，因为框架需要调用 因此名字必须是open_spider 一点都不能错
    def open_spider(self,spider):
        pass
        #print "Spider start!"

    #同样 close_spider 的函数名也必须是这个，否则框架是无法识别的
    def close_spider(self, spider):
        #print "Close the spider pipeline"
        #注意Json文件以一个空的数据结构结尾
        self.file.write('{}]')
        self.file.close()

class MongoDB_StoragePipeline(object):
    def __init__(self):
        # 链接数据库
        self.client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        # 数据库登录需要帐号密码的话
        # self.client.admin.authenticate(settings['MINGO_USER'], settings['MONGO_PSW'])
        self.db = self.client[settings['MONGO_DB']]  # 获得数据库的句柄
        self.coll = self.db[settings['MONGO_COLL']]  # 获得collection的句柄

    def open_spider(self,spider):
        logging.info("MongoDB_Pipeline has been opened.")

    def close_spider(self,spider):
        logging.info("MongoDB_Pipeline has been closed.")

    def process_item(self, item, spider):
        postItem = dict(item)  # 把item转化成字典形式
        self.coll.insert(postItem)  # 向数据库插入一条记录
        return item  # 会在控制台输出原item数据，可以选择不写

class SpiderPipeline(object):
    def process_item(self, item, spider):
        return item
