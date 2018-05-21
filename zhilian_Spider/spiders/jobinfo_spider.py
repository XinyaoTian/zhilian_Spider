# # -*- encoding:utf-8 -*-
# import scrapy
#
# # 导入正则模块用于匹配 url 和 xpath
# import re
#
# import requests
#
# import logging
# logging.basicConfig(level = logging.INFO)
#
# from zhilian_Spider.items import JobInfoItem
#
# from scrapy.contrib.spiders import CrawlSpider, Rule
# from scrapy.conf import settings
# from urlparse import urljoin
#
# from func_pack import get_current_day
# from func_pack import get_current_time
# from func_pack import get_jobhrefs
#
# class JobinfoSpider(CrawlSpider):
#
#     name = "JobinfoSpider"
#
#     custom_settings = {
#         'ITEM_PIPELINES':{
#             'zhilian_Spider.pipelines.jobInfo_JsonWithEncodingPipeline':301
#         }
#     }
#
#     headers = {
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#         "Accept - Encoding":"gzip, deflate",
#         "Accept - Language":"zh-CN,zh;q=0.9,en;q=0.8",
#         "Cache - Control":"max-age=0",
#         "Connection":"keep-alive",
#         "Host": "sou.zhaopin.com",
#         # "Referer":" http: // bj.lianjia.com /?utm_source = baidu & utm_medium = pinzhuan & utm_term = biaoti & utm_content = biaotimiaoshu & utm_campaign = sousuo & ljref = pc_sem_baidu_ppzq_x",
#         "Upgrade-Insecure-Requests":"1",
#         # "User - Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
#     }
#
#     meta = {
#         'dont_redirect':True,
#         'handle_httpstatus_list': [301, 302 , 500 , 502],
#     }
#
#     allowed_domains = ["zhaopin.com"]
#
#     # start_urls = [
#     #     'http://jobs.zhaopin.com/426548538250246.htm'
#     # ]
#
#     start_urls = get_jobhrefs()
#
#     cookie = settings['COOKIE']
#
#     # 设置发起请求的各项参数。为避免重复爬取起始页，如注释掉这个函数，转而用parse方法发起首次请求。
#     # def start_requests(self):
#     #     for href in self.start_urls:
#     #         yield scrapy.Request(url=href , callback=self.parse ,method= 'GET',headers = self.headers ,
#     #                              meta=self.meta, cookies=self.cookie, encoding='utf-8')
#
#     def parse(self,response):
#         infoItem = JobInfoItem()
#         # 职业名称信息
#         infoItem['job_name'] = response.xpath('/html/body/div[5]/div[1]/div[1]/h1/text()').extract_first()
#         # infoItem['feedback_rate'] = response.meta['feedback_rate']
#         for item in response.xpath('//div[@class="terminalpage clearfix"]'):
#
#             #url信息
#             infoItem['job_url'] = response.url
#
#             # 职位信息
#             infoItem['salary'] = item.xpath('.//div[1]/ul[1]/li[1]/strong/text()').extract_first()
#             infoItem['work_position'] = item.xpath('.//div[1]/ul[1]/li[2]/strong/a/text()').extract_first()
#             infoItem['publish_date'] = item.xpath('.//div[1]/ul[1]/li[3]/strong/span/text()').extract_first()
#             infoItem['job_nature'] = item.xpath('.//div[1]/ul[1]/li[4]/strong/text()').extract_first()
#             infoItem['work_experience'] = item.xpath('.//div[1]/ul[1]/li[5]/strong/text()').extract_first()
#             infoItem['education_degree'] = item.xpath('.//div[1]/ul[1]/li[6]/strong/text()').extract_first()
#             infoItem['demand_number'] = item.xpath('.//div[1]/ul[1]/li[7]/strong/text()').extract_first()
#             infoItem['job_category'] = item.xpath('.//div[1]/ul[1]/li[8]/strong/a/text()').extract_first()
#
#             #公司信息
#             infoItem['company_name'] = item.xpath('.//div[@class="company-box"]/p[@class="company-name-t"]/a/text()').extract_first()
#
#             for detail in item.xpath('.//div[@class="company-box"]/ul[1]/li'):
#                 subtitle = detail.xpath('.//span/text()').extract_first()
#                 # subtitle.encode('utf-8')
#                 if subtitle ==  unicode('公司规模：'):
#                     infoItem['company_scale'] = detail.xpath('.//strong/text()').extract_first()
#                 elif subtitle == '公司性质：':
#                     infoItem['company_nature'] = detail.xpath('.//strong/text()').extract_first()
#                 elif subtitle == '公司行业：':
#                     infoItem['company_industrial'] = detail.xpath('.//strong/a/text()').extract_first()
#                 elif subtitle == '公司主页：':
#                     infoItem['company_webpage'] = detail.xpath('.//strong/a/@href').extract_first()
#                 elif subtitle == '公司地址：':
#                     infoItem['company_address'] = detail.xpath('.//strong/text()').extract_first()
#             # infoItem['company_scale'] = item.xpath('.//div[@class="company-box"]/ul[1]/li[1]/strong/text()').extract_first()
#             # infoItem['company_nature'] = item.xpath('.//div[@class="company-box"]/ul[1]/li[2]/strong/text()').extract_first()
#             # infoItem['company_industrial'] = item.xpath('.//div[@class="company-box"]/ul[1]/li[3]/strong/a/text()').extract_first()
#             # infoItem['company_webpage'] = item.xpath('.//div[@class="company-box"]/ul[1]/li[4]/strong/a/@href').extract_first()
#             # infoItem['company_address'] = item.xpath('.//div[@class="company-box"]/ul[1]/li[5]/strong/text()').extract_first()
#
#             # 利用meta传递从之前页面爬取到的简历反馈率
#             # infoItem['feedback_rate'] = response.meta['feedback_rate']
#             infoItem['scrape_time'] = get_current_day() + "_" + get_current_time()
#
#
#             yield infoItem
#
#         pass
#
#     pass
