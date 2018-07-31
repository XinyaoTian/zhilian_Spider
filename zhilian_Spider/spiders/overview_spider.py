# -*- encoding:utf-8 -*-
import scrapy

# 导入正则模块用于匹配 url 和 xpath
import re

import time
import sys

import logging
logging.basicConfig(level = logging.DEBUG)

from zhilian_Spider.items import JobInfoItem

from func_pack import get_current_day
from func_pack import get_current_time

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.conf import settings
from urlparse import urljoin

# 由于python中的string是以ascii编码的,所以在这里要手动转换为utf-8,这样utf-8才可以使用unicode函数解码~
reload(sys)
sys.setdefaultencoding('utf-8')

class OverviewSpider(CrawlSpider):

    name = "OverviewSpider"

    custom_settings = {
        'ITEM_PIPELINES':{
            'zhilian_Spider.pipelines.jobInfo_JsonWithEncodingPipeline':300
        }
    }

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept - Encoding":"gzip, deflate , br",
        "Accept - Language":"zh-CN,zh;q=0.9,en;q=0.8",
        "Cache - Control":"max-age=0",
        "Connection":"keep-alive",
        "Host": "sou.zhaopin.com",
        # "Referer":" http: // bj.lianjia.com /?utm_source = baidu & utm_medium = pinzhuan & utm_term = biaoti & utm_content = biaotimiaoshu & utm_campaign = sousuo & ljref = pc_sem_baidu_ppzq_x",
        "Upgrade-Insecure-Requests":"1",
        "User - Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
    }

    meta = {
        'dont_redirect':True,
        'handle_httpstatus_list': [301, 302],
    }

    allowed_domains = ["zhaopin.com"]

    # start_urls = [
    #     'https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC%3B%E4%B8%8A%E6%B5%B7%3B%E5%B9%BF%E5%B7%9E%3B%E6%B7%B1%E5%9C%B3%3B%E5%A4%A9%E6%B4%A5&kw=%E5%A4%A7%E6%95%B0%E6%8D%AE&sm=0&isadv=0&isfilter=1&p=1'
    # ]

    start_urls = [
        'https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC%2B%E4%B8%8A%E6%B5%B7%2B%E5%B9%BF%E5%B7%9E%2B%E6%B7%B1%E5%9C%B3%2B%E5%A4%A9%E6%B4%A5&kw=hadoop&isadv=0&isfilter=1&p=1&bj=300200'
    ]

    cookie = settings['COOKIE']

    # 设置发起请求的各项参数。为避免重复爬取起始页，如注释掉这个函数，转而用parse方法发起首次请求。
    # def start_requests(self):
    #     for href in self.start_urls:
    #         yield scrapy.Request(url=href , callback=self.parse ,method= 'GET',headers = self.headers ,
    #                              meta=self.meta, cookies=self.cookie, encoding='utf-8')

    # 此函数用于发起请求计算总页数并翻页
    def parse(self,response):
        meta = {
            'dont_redirect': True,
            'handle_httpstatus_list': [301, 302],
            'current_page_num': None
        }

        # 这里需要计算出该求职信息共有多少页，便于爬虫的翻页
        jobs_per_page = len(response.xpath('//table[@class="newlist"]'))
        jobs_total = int(response.xpath('/html/body/div[3]/div[3]/div[2]/span[1]/em/text()').extract_first())
        print "***************" + str(jobs_total) + "***************"

        # 计算总页数
        if jobs_total%jobs_per_page is not 0:
            full_page = jobs_total // jobs_per_page + 1
        else:
            full_page = jobs_total // jobs_per_page

        print "***************"+ str(full_page) + "***************"

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
            # logging.info("Current page(" + str(part_url) + ") : " + str(cur_page) + "/" + str(full_page))
            meta['current_page_num'] = part_url
            # print part_url
            yield scrapy.Request(url_to_request,callback=self.parse_job_info,method= 'GET',headers = self.headers ,
                                 meta=meta, cookies=self.cookie, encoding='utf-8')
            cur_page += 1

    def parse_job_info(self,response):
        # logging.info("New page")
        for item in response.xpath('//table[@class="newlist"]'):

            meta_job = {
                'dont_redirect': True,
                'handle_httpstatus_list': [301, 302],
                'feedback_rate': None  # 这个变量是用来传递上一个页面中的信息的
            }

            # infoItem = OverviewItem()
            # infoItem['job_name'] = item.xpath('.//td[1]/div[1]/a[1]/text()').extract_first()
            job_url = item.xpath('.//td[1]/div[1]/a[1]/@href').extract_first()
            # infoItem['job_url'] = job_url
            job_url = str(job_url)
            # 这里一定要使用urljoin函数，不然是爬不到相应的url的
            job_url = urljoin(response.url,job_url)

            # logging.info("url_type: " + str(type(job_url)) + "  url: " + str(job_url))
            # infoItem['feedback_rate'] = item.xpath('.//td[2]/span[1]/text()').extract_first()

            meta_job['feedback_rate'] = item.xpath('.//td[2]/span[1]/text()').extract_first()
            # infoItem['company_name'] = item.xpath('.//td[3]/a[1]/text()').extract_first()
            # infoItem['salary'] = item.xpath('.//td[4]/text()').extract_first()
            # infoItem['work_position'] = item.xpath('.//td[5]/text()').extract_first()
            # infoItem['work_position'] = item.xpath('.//td[6]/span[1]/text()').extract_first()
            # infoItem['current_page'] = response.meta['current_page_num']

            # yield infoItem

            yield scrapy.Request(url=job_url,callback=self.parse_specific_info,
                                 meta=meta_job, encoding='utf-8')

    def parse_specific_info(self,response):
        infoItem = JobInfoItem()
        # 职业名称信息
        infoItem['job_name'] = response.xpath('/html/body/div[5]/div[1]/div[1]/h1/text()').extract_first()
        # infoItem['feedback_rate'] = response.meta['feedback_rate']
        for item in response.xpath('//div[@class="terminalpage clearfix"]'):

            #url信息
            infoItem['job_url'] = response.url

            # 职位信息
            infoItem['salary'] = item.xpath('.//div[1]/ul[1]/li[1]/strong/text()').extract_first()
            infoItem['work_position'] = item.xpath('.//div[1]/ul[1]/li[2]/strong/a/text()').extract_first()
            infoItem['publish_date'] = item.xpath('.//div[1]/ul[1]/li[3]/strong/span/text()').extract_first()
            infoItem['job_nature'] = item.xpath('.//div[1]/ul[1]/li[4]/strong/text()').extract_first()
            infoItem['work_experience'] = item.xpath('.//div[1]/ul[1]/li[5]/strong/text()').extract_first()
            infoItem['education_degree'] = item.xpath('.//div[1]/ul[1]/li[6]/strong/text()').extract_first()
            infoItem['demand_number'] = item.xpath('.//div[1]/ul[1]/li[7]/strong/text()').extract_first()
            infoItem['job_category'] = item.xpath('.//div[1]/ul[1]/li[8]/strong/a/text()').extract_first()

            #公司信息
            infoItem['company_name'] = item.xpath('.//div[@class="company-box"]/p[@class="company-name-t"]/a/text()').extract_first()

            for detail in item.xpath('.//div[@class="company-box"]/ul[1]/li'):
                subtitle = detail.xpath('.//span/text()').extract_first()
                # subtitle.encode('utf-8')
                if subtitle ==  unicode('公司规模：'):
                    infoItem['company_scale'] = detail.xpath('.//strong/text()').extract_first()
                elif subtitle == '公司性质：':
                    infoItem['company_nature'] = detail.xpath('.//strong/text()').extract_first()
                elif subtitle == '公司行业：':
                    infoItem['company_industrial'] = detail.xpath('.//strong/a/text()').extract_first()
                elif subtitle == '公司主页：':
                    infoItem['company_webpage'] = detail.xpath('.//strong/a/@href').extract_first()
                elif subtitle == '公司地址：':
                    infoItem['company_address'] = detail.xpath('.//strong/text()').extract_first()
            # infoItem['company_scale'] = item.xpath('.//div[@class="company-box"]/ul[1]/li[1]/strong/text()').extract_first()
            # infoItem['company_nature'] = item.xpath('.//div[@class="company-box"]/ul[1]/li[2]/strong/text()').extract_first()
            # infoItem['company_industrial'] = item.xpath('.//div[@class="company-box"]/ul[1]/li[3]/strong/a/text()').extract_first()
            # infoItem['company_webpage'] = item.xpath('.//div[@class="company-box"]/ul[1]/li[4]/strong/a/@href').extract_first()
            # infoItem['company_address'] = item.xpath('.//div[@class="company-box"]/ul[1]/li[5]/strong/text()').extract_first()

            # 利用meta传递从之前页面爬取到的简历反馈率
            infoItem['feedback_rate'] = response.meta['feedback_rate']
            infoItem['scrape_time'] = get_current_day() + "_" + get_current_time()


            yield infoItem

        pass

    pass