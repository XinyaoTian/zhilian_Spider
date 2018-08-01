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

# 设置爬取两个页面之间的等待时间
DOWNLOAD_DELAY = 3

#-----2018-3-21------
MONGO_HOST = "127.0.0.1"  # 主机IP
MONGO_PORT = 27017  # 端口号
MONGO_DB = "jobItem_houseInfo"  # 库名
MONGO_COLL = create_time_table()  # collection名
# MONGO_USER = "zhangsan"
# MONGO_PSW = "123456"
#-------------------

#-----2018-3-22------
COOKIE = {'dywez': '95841923.1526257252.10.5.dywecsr', 'campusOperateJobUserInfo': '0b896891-5e7d-4a6a-8e88-6a2b382f1f67', 'Hm_lvt_38ba284938d5eddca645bb5e02a02006': '1525506467,1526110481,1526180966,1526214430', 'dyweb': '95841923.13.9.1526263844414', 'dywec': '95841923', 'dywea': '95841923.3179178797253694500.1522649313.1526257252.1526257252.11', 'stayTimeCookie': '1526266327168', 'referrerUrl': '', '_jzqa': '1.3745435935358784500.1525506467.1526257252.1526263683.9', '_jzqc': '1', 'adfcid2': 'none', 'adfbid': '0', 'adfbid2': '0', 'urlfrom2': '121126445', 'LastSearchHistory': '%7b%22Id%22%3a%2268141590-3233-40d3-a0d1-6ce3baa34e13%22%2c%22Name%22%3a%22hadoop+%2b+%e5%8c%97%e4%ba%ac+%2b+%e4%ba%92%e8%81%94%e7%bd%91%e4%ba%a7%e5%93%81%2f%e8%bf%90%e8%90%a5%e7%ae%a1%e7%90%86+...%22%2c%22SearchUrl%22%3a%22http%3a%2f%2fsou.zhaopin.com%2fjobs%2fsearchresult.ashx%3fjl%3d%25e5%258c%2597%25e4%25ba%25ac%26kw%3dhadoop%26isadv%3d0%26ispts%3d1%26isfilter%3d1%26p%3d1%26bj%3d160200%26sj%3d316%22%2c%22SaveTime%22%3a%22%5c%2fDate(1526264445877%2b0800)%5c%2f%22%7d', '_jzqy': '1.1526180967.1526214431.2.jzqsr', '_jzqx': '1.1526257252.1526263683.2.jzqsr', 'Hm_lpvt_38ba284938d5eddca645bb5e02a02006': '1526266327', 'LastCity%5Fid': '530', 'firstchannelurl': 'https%3A//passport.zhaopin.com/account/login%3FbkUrl%3Dhttp%253A%252F%252Fsou.zhaopin.com%252Fjobs%252Fsearchresult.ashx%253Fjl%253D530%2526bj%253D160000%2526sj%253D044', '__utmz': '269921210.1526257252.11.5.utmcsr', 'urlfrom': '121126445', '__utmt': '1', 'LastCity': '%e5%8c%97%e4%ba%ac', 'zg_did': '%7B%22did%22%3A%20%22163579b251e9d5-018acec8f612c5-f373567-e1000-163579b251f3ef%22%7D', 'qrcodekey': '945bc32f873c44ea8a01fea8e83fccb6', 'zg_08c5bcee6e9a4c0594a5d34b79b9622a': '%7B%22sid%22%3A%201526183175460%2C%22updated%22%3A%201526183181343%2C%22info%22%3A%201526183175466%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22ts.zhaopin.com%22%7D', '__utma': '269921210.1038731062.1522649313.1526257252.1526257252.12', '__utmb': '269921210.13.9.1526263844418', '__utmc': '269921210', '__xsptplus30': '30.6.1526180966.1526180966.1%231%7Cother%7Ccnt%7C121122523%7C%7C%23%23L7vEolKFwetqqIvc4hJ9TS6rm5TQBod2%23', '_jzqckmp': '1', 'JSSearchModel': '0', 'hiddenEpinDiv': 'none', 'adfcid': 'none', 'lastchannelurl': 'http%3A//sou.zhaopin.com/jobs/searchresult.ashx%3Fjl%3D530%26bj%3D160000%26sj%3D044'}


# #--------------------
#
# # -----2018-3-27----- #
# # USER_AGENTS 随机的代理头部
USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]
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
DOWNLOADER_MIDDLEWARES = {
#    'myproject.middlewares.MyCustomDownloaderMiddleware': 543,
    'zhilian_Spider.middlewares.RandomUserAgent': 1,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    #'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    #'Spider.middlewares.ProxyMiddleware': 100,
    #'scrapy.downloadermiddlewares.retry.RetryMiddleware':None,
    #'zhilian_Spider.middlewares.RetryMiddleware':550
}

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
