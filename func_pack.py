# -*- coding:utf-8 -*-
import json
import time
import requests

#用于获取已经取得的全部社区的url地址
def get_comhrefs():
    with open("href.json",'r')as f:
        temp = json.loads(f.read())
        #注意json文件以一个空的字典{}结尾！
    f.close()
    list_href = []
    for item in temp:
        if bool(item) is True: #由于json文件中最后一个数据为空，因此设置此判断防止误读
            list_href.append(item["href_community"].encode('utf-8')) #注意这里unicode转为utf-8的方法...
    #print list_href
    return list_href

#获取当前系统日期
def get_current_day():
    current_day = str(time.strftime("%Y_%m_%d"))
    #print current_day
    return current_day

#获取当前系统时间
def get_current_time():
    current_time = str(time.strftime("%H_%M_%S"))
    return current_time

#创建新的数据库名字
#我们设计的爬虫是要部署到云服务器上 利用脚本在每天固定时间对链家网进行爬取的
#因此 我们把每天得到的数据存进不同的表中 方便以后做数据的趋势分析
def create_daytime_table():
    houseInfo = "houseInfo"
    table_name = houseInfo + "_" + get_current_day()
    return table_name

def create_time_table():
    houseInfo = "houseInfo"
    table_name = houseInfo + "_" + get_current_day() + "_" + get_current_time()
    return table_name

# 本函数使用芝麻代理的API接口(HTTP类型,json格式)
# 并将获取到的数据储存为以dict为单元的list，直接对接到 settings.py 的 PROXIES 中使用
def get_zhima_agency(url):
    ip_list = []
    # 尝试获取芝麻代理API接口的ip数据，并组成一个dict，之后放在list中
    try:
        result = requests.get(url)
        content_dict = json.loads(result.content)
        # 可以通过打印 content_dict 来确定从API接口获取到的ip数据结构
        for item in content_dict['data']:
            ip_port_dict = {}
            ip_port_str = str(item['ip']) + ":" + str(item['port'])
            ip_port_dict['ip_port'] = ip_port_str
            ip_port_dict['user_pass'] = ''
            ip_port_dict['ip_status'] = 1 # 初始化ip状态为1 即可用状态。随后如果TCP连续3次未连接上则置0。ip失效。
            ip_list.append(ip_port_dict)
    except:
        print "Warnning!Check your web connection or your ZhiMa Ip agency url status."
    finally:
        # 最终，打印并返回从API中获取的list
        print ip_list
        return ip_list

#这个函数是用于转化浏览器上开发者工具里复制粘贴下来的COOKIE的
#先把cookie那一栏粘贴上从浏览器复制下来的一大长串COOKIE
#运行这个文件，会打印出字典格式的COOKIE
#把这个字典格式的COOKIE复制粘贴到settings里面，再在相关爬虫文件里引用就可以啦
class transCookie():
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        '''
        将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        :return:
        '''
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict

# if __name__ == "__main__":
#     #这个是现在我的COOKIE 大家要根据自己的浏览器复制进自己的COOKIE哟
#     cookie =  'ZP-ENV-FLAG=gray; adfbid2=0; urlfrom2=121126445; adfcid2=none; JSSearchModel=0; dywez=95841923.1525516026.3.2.dywecsr=sou.zhaopin.com|dyweccn=(referral)|dywecmd=referral|dywectr=undefined|dywecct=/jobs/searchresult.ashx; __utmz=269921210.1525516026.3.2.utmcsr=sou.zhaopin.com|utmccn=(referral)|utmcmd=referral|utmcct=/jobs/searchresult.ashx; __xsptplus30=30.3.1525668647.1525668647.1%231%7Cother%7Ccnt%7C121122523%7C%7C%23%23_YMpW8aRnH_okX06ktqRLssoDrPVmsER%23; urlfrom=121126445; adfcid=none; adfbid=0; dywea=95841923.3179178797253694500.1522649313.1525668647.1526109521.5; dywec=95841923; _jzqa=1.3745435935358784500.1525506467.1525668648.1526109521.3; _jzqc=1; _jzqckmp=1; _qzjc=1; __utma=269921210.1038731062.1522649313.1525668647.1526109521.5; __utmc=269921210; BLACKSTRIP=yes; LastCity%5Fid=530; LastCity=%e5%8c%97%e4%ba%ac; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1525506467,1526110481; LastJobTag=%e4%ba%94%e9%99%a9%e4%b8%80%e9%87%91%7c%e5%b8%a6%e8%96%aa%e5%b9%b4%e5%81%87%7c%e8%8a%82%e6%97%a5%e7%a6%8f%e5%88%a9%7c%e9%a4%90%e8%a1%a5%7c%e7%bb%a9%e6%95%88%e5%a5%96%e9%87%91%7c%e5%ae%9a%e6%9c%9f%e4%bd%93%e6%a3%80%7c%e5%bc%b9%e6%80%a7%e5%b7%a5%e4%bd%9c%7c%e8%a1%a5%e5%85%85%e5%8c%bb%e7%96%97%e4%bf%9d%e9%99%a9%7c%e5%b9%b4%e5%ba%95%e5%8f%8c%e8%96%aa%7c%e4%ba%a4%e9%80%9a%e8%a1%a5%e5%8a%a9%7c%e5%91%98%e5%b7%a5%e6%97%85%e6%b8%b8%7c%e9%80%9a%e8%ae%af%e8%a1%a5%e8%b4%b4%7c%e5%91%a8%e6%9c%ab%e5%8f%8c%e4%bc%91%7c%e5%8a%a0%e7%8f%ad%e8%a1%a5%e5%8a%a9%7c%e8%82%a1%e7%a5%a8%e6%9c%9f%e6%9d%83%7c%e5%85%a8%e5%8b%a4%e5%a5%96%7c%e6%af%8f%e5%b9%b4%e5%a4%9a%e6%ac%a1%e8%b0%83%e8%96%aa%7c%e5%b9%b4%e7%bb%88%e5%88%86%e7%ba%a2%7c14%e8%96%aa%7c%e5%85%8d%e8%b4%b9%e7%8f%ad%e8%bd%a6%7c%e5%88%9b%e4%b8%9a%e5%85%ac%e5%8f%b8%7c%e5%8c%85%e5%90%83%7c%e5%81%a5%e8%ba%ab%e4%bf%b1%e4%b9%90%e9%83%a8%7c%e5%8c%85%e4%bd%8f%7c%e4%b8%8d%e5%8a%a0%e7%8f%ad%7c%e6%88%bf%e8%a1%a5%7c%e9%ab%98%e6%b8%a9%e8%a1%a5%e8%b4%b4%7c%e9%87%87%e6%9a%96%e8%a1%a5%e8%b4%b4%7c%e4%bd%8f%e6%88%bf%e8%a1%a5%e8%b4%b4%7c%e6%97%a0%e8%af%95%e7%94%a8%e6%9c%9f%7c%e5%85%8d%e6%81%af%e6%88%bf%e8%b4%b7; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1526115635; __utmt=1; LastSearchHistory=%7b%22Id%22%3a%223b890a0d-04fb-454f-8c0d-0574112e8c04%22%2c%22Name%22%3a%22hadoop+%2b+%e5%8c%97%e4%ba%ac%22%2c%22SearchUrl%22%3a%22http%3a%2f%2fsou.zhaopin.com%2fjobs%2fsearchresult.ashx%3fjl%3d%25e5%258c%2597%25e4%25ba%25ac%26kw%3dhadoop%26p%3d1%26isadv%3d0%22%2c%22SaveTime%22%3a%22%5c%2fDate(1526116869389%2b0800)%5c%2f%22%7d; dyweb=95841923.50.9.1526115207155; __utmb=269921210.50.9.1526115207158; _qzja=1.1785659975.1525506501733.1525668650605.1526109521173.1526116753921.1526116868415.0.0.0.55.3; _qzjb=1.1526109521173.33.0.0.0; _qzjto=33.1.0; _jzqb=1.33.10.1526109521.1'
#     trans = transCookie(cookie)
#     print trans.stringToDict()





#Testing code
#print get_comhrefs()
#print(temp)
#print(temp[1]['href_community'])