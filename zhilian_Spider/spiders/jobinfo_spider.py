# -*- encoding:utf-8 -*-
import scrapy

# 导入正则模块用于匹配 url 和 xpath
import re

import requests

import logging
logging.basicConfig(level = logging.INFO)

from zhilian_Spider.items import OverviewItem
from zhilian_Spider.items import JobInfoItem

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.conf import settings
from urlparse import urljoin

class JobinfoSpider(CrawlSpider):

    name = "JobinfoSpider"

    custom_settings = {
        'ITEM_PIPELINES':{
            'zhilian_Spider.pipelines.jobInfo_JsonWithEncodingPipeline':301
        }
    }

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept - Encoding":"gzip, deflate",
        "Accept - Language":"zh-CN,zh;q=0.9,en;q=0.8",
        "Cache - Control":"max-age=0",
        "Connection":"keep-alive",
        "Host": "sou.zhaopin.com",
        # "Referer":" http: // bj.lianjia.com /?utm_source = baidu & utm_medium = pinzhuan & utm_term = biaoti & utm_content = biaotimiaoshu & utm_campaign = sousuo & ljref = pc_sem_baidu_ppzq_x",
        "Upgrade-Insecure-Requests":"1",
        # "User - Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
    }

    meta = {
        'dont_redirect':True,
        'handle_httpstatus_list': [301, 302 , 500 , 502],
    }

    allowed_domains = ["zhaopin.com"]

    start_urls = [
        'http://jobs.zhaopin.com/426548538250246.htm'
    ]

    cookie = settings['COOKIE']

    # 设置发起请求的各项参数。为避免重复爬取起始页，如注释掉这个函数，转而用parse方法发起首次请求。
    # def start_requests(self):
    #     for href in self.start_urls:
    #         yield scrapy.Request(url=href , callback=self.parse ,method= 'GET',headers = self.headers ,
    #                              meta=self.meta, cookies=self.cookie, encoding='utf-8')

    def parse(self,response):
        print response
        infoItem = JobInfoItem()
        infoItem['job_name'] = response.xpath('/html/body/div[5]/div[1]/div[1]/h1/text()').extract_first()
        # infoItem['feedback_rate'] = response.meta['feedback_rate']
        for item in response.xpath('//div[@class="terminalpage clearfix"]'):
            infoItem['job_url'] = response.url
            # To Do: add xpath().extract_first()
            infoItem['salary'] = item.xpath('.//div[1]/ul[1]/li[1]/strong/text()').extract_first()
            infoItem['work_position'] = item.xpath('.//div[1]/ul[1]/li[2]/strong/a/text()').extract_first()
            infoItem['publish_date'] = item.xpath('.//div[1]/ul[1]/li[3]/strong/span/text()').extract_first()
            infoItem['job_nature'] = item.xpath('.//div[1]/ul[1]/li[4]/span/text()').extract_first()
            infoItem['work_experience'] = item.xpath('.//div[1]/ul[1]/li[5]/strong/text()').extract_first()

            yield infoItem
