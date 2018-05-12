# -*- encoding:utf-8 -*-
import scrapy

# 导入正则模块用于匹配 url 和 xpath
import re

import logging
logging.basicConfig(level = logging.INFO)

from zhilian_Spider.items import OverviewItem
from zhilian_Spider.items import JobInfoItem

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.conf import settings

class OverviewSpider(CrawlSpider):

    name = "OverviewSpider"

    custom_settings = {
        'ITEM_PIPELINES':{
            'zhilian_Spider.pipelines.overview_JsonWithEncodingPipeline':300
        }
    }

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept - Encoding":"gzip, deflate",
        "Accept - Language":"zh-CN,zh;q=0.9,en;q=0.8",
        "Cache - Control":"max-age=0",
        "Connection":"keep-alive",
        "Host": "sou.zhaopin.com",
        "Referer":" http: // bj.lianjia.com /?utm_source = baidu & utm_medium = pinzhuan & utm_term = biaoti & utm_content = biaotimiaoshu & utm_campaign = sousuo & ljref = pc_sem_baidu_ppzq_x",
        "Upgrade-Insecure-Requests":"1",
        "User - Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
    }

    meta = {
        'dont_redirect':True,
        'handle_httpstatus_list': [301, 302],
    }

    allowed_domains = ["zhaopin.com"]

    start_urls = [
        'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=hadoop&sm=0&fl=530&isadv=0&ispts=1&isfilter=1&p=1&bj=200500&sj=055'
    ]

    cookie = settings['COOKIE']

    # 设置发起请求的各项参数。为避免重复爬取起始页，如注释掉这个函数，转而用parse方法发起首次请求。
    # def start_requests(self):
    #     for href in self.start_urls:
    #         yield scrapy.Request(url=href , callback=self.parse ,method= 'GET',headers = self.headers ,
    #                              meta=self.meta, cookies=self.cookie, encoding='utf-8')

    # 此函数用于发起请求计算总页数并翻页
    def parse(self,response):
        # 这里需要计算出该求职信息共有多少页，便于爬虫的翻页
        jobs_per_page = len(response.xpath('//table[@class="newlist"]'))
        jobs_total = int(response.xpath('/html/body/div[3]/div[3]/div[2]/span[1]/em/text()').extract_first())

        # 计算总页数
        if jobs_total%jobs_per_page is not 0:
            full_page = jobs_total // jobs_per_page + 1
        else:
            full_page = jobs_total // jobs_per_page

        # 设置当前页数，并通过循环 利用scrapy.Request函数依次对后续页数发起请求
        # 并用自己编写的parse_house_info函数对新抓取到的页面进行信息搜集
        cur_page = 1
        while cur_page <= full_page:
            #手动组合字符串url
            part_url = "&p=" + str(cur_page)
            # cur_url = response.urljoin(part_url)
            cur_url = response.url
            url_striped = re.split('&p=\d+',cur_url) # 利用正则匹配掉
            if len(url_striped) == 1:
                url_to_request = url_striped[0] + part_url
            elif len(url_striped) > 1:
                url_to_request = url_striped[0] + part_url + url_striped[1]
            else :
                url_to_request = None
                logging.DEBUG("Cannot request next url!  Current url = " + str(cur_url))
            # logging.info("status : " + str(response.status))
            # logging.info("headers : " + str(response.headers))
            logging.info("Current page(" + str(part_url) + ") : " + str(cur_page) + "/" + str(full_page))
            yield scrapy.Request(url_to_request,callback=self.parse_job_info,method= 'GET',headers = self.headers ,
                                 meta=self.meta, cookies=self.cookie, encoding='utf-8')
            cur_page += 1

    def parse_job_info(self,response):
        # logging.info("New page")
        for item in response.xpath('//table[@class="newlist"]'):

            # meta_job = {
            #     'dont_redirect': True,
            #     'handle_httpstatus_list': [301, 302],
            #     'feedback_rate': None  # 这个变量是用来传递上一个页面中的信息的
            # }

            infoItem = OverviewItem()
            infoItem['job_name'] = item.xpath('.//td[1]/div[1]/a[1]/text()').extract_first()
            infoItem['job_url'] = item.xpath('.//td[1]/div[1]/a[1]/@href').extract_first()
            
            logging.info("url_type: " + str(type(infoItem['job_url'])) + "  url: " + str(infoItem['job_url']))
            infoItem['feedback_rate'] = item.xpath('.//td[2]/span[1]/text()').extract_first()

            # meta_job['feedback_rate'] = infoItem['feedback_rate']
            infoItem['company_name'] = item.xpath('.//td[3]/a[1]/text()').extract_first()
            infoItem['salary'] = item.xpath('.//td[4]/text()').extract_first()
            infoItem['work_position'] = item.xpath('.//td[5]/text()').extract_first()
            infoItem['work_position'] = item.xpath('.//td[6]/span[1]/text()').extract_first()

            yield infoItem

            # yield scrapy.Request(str(infoItem['job_url']),callback=self.parse_specific_info,method= 'GET',headers = self.headers ,
            #                      meta=self.meta, cookies=self.cookie, encoding='utf-8')

    def parse_specific_info(self,response):
        infoItem = JobInfoItem()
        infoItem['job_name'] = response.xpath('/html/body/div[5]/div[1]/div[1]/h1/text()').extract_first()
        # infoItem['feedback_rate'] = response.meta['feedback_rate']
        for item in response.xpath('//div[@class="terminalpage clearfix"]'):
            infoItem['job_url'] = response.url
            # To Do: add xpath().extract_first()
            infoItem['salary'] = item.xpath('.//div[1]/ul[1]/li[1]/strong/text()').extract_first()
            infoItem['work_positon'] = item.xpath('.//div[1]/ul[1]/li[2]/strong/a/text()').extract_first()
            infoItem['publish_date'] = item.xpath('.//div[1]/ul[1]/li[3]/strong/span/text()').extract_first()
            infoItem['job_nature'] = item.xpath('.//div[1]/ul[1]/li[4]/span/text()').extract_first()
            infoItem['work_experience'] = item.xpath('.//div[1]/ul[1]/li[5]/strong/text()').extract_first()

            yield infoItem

        pass

    pass