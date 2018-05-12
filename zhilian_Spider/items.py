# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 不点击进入职业详细信息页面，信息总览的Item
class OverviewItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_name = scrapy.Field() # 职位名称
    job_url = scrapy.Field() # 详细信息链接
    feedback_rate = scrapy.Field() # 简历反馈率
    company_name = scrapy.Field() # 公司名称
    salary = scrapy.Field() # 薪资
    work_position = scrapy.Field() # 工作地点
    publish_date = scrapy.Field() # 发布日期
    pass
