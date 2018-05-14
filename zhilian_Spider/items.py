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
    current_page = scrapy.Field() # 爬取的当前页数
    pass

class JobInfoItem(scrapy.Item):
    job_url = scrapy.Field()  # 网页链接
    job_name = scrapy.Field() # 职位名称

    salary = scrapy.Field()  # 薪资
    publish_date = scrapy.Field()  # 发布日期
    work_experience = scrapy.Field() # 工作经验
    demand_number = scrapy.Field() # 招聘人数
    work_position = scrapy.Field()  # 工作地点
    job_nature = scrapy.Field() # 工作性质(全职？兼职？)
    education_degree = scrapy.Field() # 学历要求
    job_category = scrapy.Field() # 职业类别

    company_name = scrapy.Field() # 公司名称
    company_nature = scrapy.Field() # 公司性质
    company_industrial = scrapy.Field() # 公司行业
    company_webpage = scrapy.Field() # 公司主页
    company_address = scrapy.Field() # 公司地址

    feedback_rate = scrapy.Field() # 简历反馈率
    pass
