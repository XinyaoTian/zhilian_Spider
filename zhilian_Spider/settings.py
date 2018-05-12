# -*- coding: utf-8 -*-

#引入我们编写的功能类中的功能函数
from func_pack import create_daytime_table
from func_pack import create_time_table
from func_pack import get_zhima_agency

# Scrapy settings for zhilian_Spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhilian_Spider'

SPIDER_MODULES = ['zhilian_Spider.spiders']
NEWSPIDER_MODULE = 'zhilian_Spider.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# 设置等待时间
DOWNLOAD_DELAY = 1.6

#-----2018-3-21------
MONGO_HOST = "127.0.0.1"  # 主机IP
MONGO_PORT = 27017  # 端口号
MONGO_DB = "jobItem_houseInfo"  # 库名
MONGO_COLL = create_time_table()  # collection名
# MONGO_USER = "zhangsan"
# MONGO_PSW = "123456"
#-------------------

#-----2018-3-22------
COOKIE = {'dywez': '95841923.1525516026.3.2.dywecsr', 'Hm_lvt_38ba284938d5eddca645bb5e02a02006': '1525506467,1526110481', 'dyweb': '95841923.50.9.1526115207155', 'dywec': '95841923', 'dywea': '95841923.3179178797253694500.1522649313.1525668647.1526109521.5', '_jzqa': '1.3745435935358784500.1525506467.1525668648.1526109521.3', '_jzqc': '1', '_jzqb': '1.33.10.1526109521.1', '_qzjto': '33.1.0', 'adfcid2': 'none', 'LastJobTag': '%e4%ba%94%e9%99%a9%e4%b8%80%e9%87%91%7c%e5%b8%a6%e8%96%aa%e5%b9%b4%e5%81%87%7c%e8%8a%82%e6%97%a5%e7%a6%8f%e5%88%a9%7c%e9%a4%90%e8%a1%a5%7c%e7%bb%a9%e6%95%88%e5%a5%96%e9%87%91%7c%e5%ae%9a%e6%9c%9f%e4%bd%93%e6%a3%80%7c%e5%bc%b9%e6%80%a7%e5%b7%a5%e4%bd%9c%7c%e8%a1%a5%e5%85%85%e5%8c%bb%e7%96%97%e4%bf%9d%e9%99%a9%7c%e5%b9%b4%e5%ba%95%e5%8f%8c%e8%96%aa%7c%e4%ba%a4%e9%80%9a%e8%a1%a5%e5%8a%a9%7c%e5%91%98%e5%b7%a5%e6%97%85%e6%b8%b8%7c%e9%80%9a%e8%ae%af%e8%a1%a5%e8%b4%b4%7c%e5%91%a8%e6%9c%ab%e5%8f%8c%e4%bc%91%7c%e5%8a%a0%e7%8f%ad%e8%a1%a5%e5%8a%a9%7c%e8%82%a1%e7%a5%a8%e6%9c%9f%e6%9d%83%7c%e5%85%a8%e5%8b%a4%e5%a5%96%7c%e6%af%8f%e5%b9%b4%e5%a4%9a%e6%ac%a1%e8%b0%83%e8%96%aa%7c%e5%b9%b4%e7%bb%88%e5%88%86%e7%ba%a2%7c14%e8%96%aa%7c%e5%85%8d%e8%b4%b9%e7%8f%ad%e8%bd%a6%7c%e5%88%9b%e4%b8%9a%e5%85%ac%e5%8f%b8%7c%e5%8c%85%e5%90%83%7c%e5%81%a5%e8%ba%ab%e4%bf%b1%e4%b9%90%e9%83%a8%7c%e5%8c%85%e4%bd%8f%7c%e4%b8%8d%e5%8a%a0%e7%8f%ad%7c%e6%88%bf%e8%a1%a5%7c%e9%ab%98%e6%b8%a9%e8%a1%a5%e8%b4%b4%7c%e9%87%87%e6%9a%96%e8%a1%a5%e8%b4%b4%7c%e4%bd%8f%e6%88%bf%e8%a1%a5%e8%b4%b4%7c%e6%97%a0%e8%af%95%e7%94%a8%e6%9c%9f%7c%e5%85%8d%e6%81%af%e6%88%bf%e8%b4%b7', 'adfbid': '0', 'ZP-ENV-FLAG': 'gray', 'adfbid2': '0', 'urlfrom2': '121126445', 'LastSearchHistory': '%7b%22Id%22%3a%223b890a0d-04fb-454f-8c0d-0574112e8c04%22%2c%22Name%22%3a%22hadoop+%2b+%e5%8c%97%e4%ba%ac%22%2c%22SearchUrl%22%3a%22http%3a%2f%2fsou.zhaopin.com%2fjobs%2fsearchresult.ashx%3fjl%3d%25e5%258c%2597%25e4%25ba%25ac%26kw%3dhadoop%26p%3d1%26isadv%3d0%22%2c%22SaveTime%22%3a%22%5c%2fDate(1526116869389%2b0800)%5c%2f%22%7d', 'Hm_lpvt_38ba284938d5eddca645bb5e02a02006': '1526115635', 'LastCity%5Fid': '530', '__utmz': '269921210.1525516026.3.2.utmcsr', 'urlfrom': '121126445', '__utmt': '1', 'LastCity': '%e5%8c%97%e4%ba%ac', '_qzja': '1.1785659975.1525506501733.1525668650605.1526109521173.1526116753921.1526116868415.0.0.0.55.3', '_qzjc': '1', '_qzjb': '1.1526109521173.33.0.0.0', '__utma': '269921210.1038731062.1522649313.1525668647.1526109521.5', '__utmb': '269921210.50.9.1526115207158', '__utmc': '269921210', '__xsptplus30': '30.3.1525668647.1525668647.1%231%7Cother%7Ccnt%7C121122523%7C%7C%23%23_YMpW8aRnH_okX06ktqRLssoDrPVmsER%23', '_jzqckmp': '1', 'JSSearchModel': '0', 'BLACKSTRIP': 'yes', 'adfcid': 'none'}


# #--------------------
#
# # -----2018-3-27----- #
# # USER_AGENTS 随机的代理头部
# USER_AGENTS = [
#     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#     "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
#     "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
#     "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
#     "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
#     "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
#     "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
#     "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
#     "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
# ]
#
# # Crawl responsibly by identifying yourself (and your website) on the user-agent
# #USER_AGENT = 'zhilian_Spider (+http://www.yourdomain.com)'
#
#
#
# '''需要使用ip池时，更新IP池并打开这些设置'''
# COOKIES_ENABLED = False
# 设置DownLoader_middleware
# 插拔中间件需要仔细看文档，了解相应中间件的端口号。
# 把想要拔下来的中间件的值设为 None ； 插上去的自己写的组件，设为相应的流程参数。
# 可以自己去scrapy的包里找源码，在middlewares中粘贴源码并改写，然后插拔组件。示例——RetryMiddleware
# DOWNLOADER_MIDDLEWARES = {
# #    'myproject.middlewares.MyCustomDownloaderMiddleware': 543,
#     'Spider.middlewares.RandomUserAgent': 1,
#     'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
#     #'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
#     #'Spider.middlewares.ProxyMiddleware': 100,
#     'scrapy.downloadermiddlewares.retry.RetryMiddleware':None,
#     'Spider.middlewares.RetryMiddleware':550
# }

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhilian_Spider.middlewares.ZhilianSpiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zhilian_Spider.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'zhilian_Spider.pipelines.ZhilianSpiderPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
