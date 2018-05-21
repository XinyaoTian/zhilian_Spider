# -*- coding:utf-8 -*-
import json
import time
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#用于获取已经取得的全部社区的url地址
def get_jobhrefs():
    with open("./overview.json",'r')as f:
        temp = json.loads(f.read())
        #注意json文件以一个空的字典{}结尾！
    f.close()
    list_href = []
    for item in temp:
        if bool(item) is True: #由于json文件中最后一个数据为空，因此设置此判断防止误读
            list_href.append(str(item["job_url"])) #注意这里unicode转为utf-8的方法...
    #print list_href
    return list_href

# l = get_jobhrefs()
# print type(l[0])
# print len(l)

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
#     cookie =  'adfbid2=0; JSSearchModel=0; adfbid=0; dywec=95841923; _jzqc=1; __utmc=269921210; hiddenEpinDiv=none; __xsptplus30=30.6.1526180966.1526180966.1%231%7Cother%7Ccnt%7C121122523%7C%7C%23%23L7vEolKFwetqqIvc4hJ9TS6rm5TQBod2%23; campusOperateJobUserInfo=0b896891-5e7d-4a6a-8e88-6a2b382f1f67; zg_did=%7B%22did%22%3A%20%22163579b251e9d5-018acec8f612c5-f373567-e1000-163579b251f3ef%22%7D; zg_08c5bcee6e9a4c0594a5d34b79b9622a=%7B%22sid%22%3A%201526183175460%2C%22updated%22%3A%201526183181343%2C%22info%22%3A%201526183175466%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22ts.zhaopin.com%22%7D; lastchannelurl=http%3A//sou.zhaopin.com/jobs/searchresult.ashx%3Fjl%3D530%26bj%3D160000%26sj%3D044; qrcodekey=945bc32f873c44ea8a01fea8e83fccb6; firstchannelurl=https%3A//passport.zhaopin.com/account/login%3FbkUrl%3Dhttp%253A%252F%252Fsou.zhaopin.com%252Fjobs%252Fsearchresult.ashx%253Fjl%253D530%2526bj%253D160000%2526sj%253D044; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1525506467,1526110481,1526180966,1526214430; _jzqy=1.1526180967.1526214431.2.jzqsr=baidu|jzqct=%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98.jzqsr=baidu; _jzqckmp=1; dywez=95841923.1526257252.10.5.dywecsr=zhaopin.com|dyweccn=(referral)|dywecmd=referral|dywectr=undefined|dywecct=/; __utmz=269921210.1526257252.11.5.utmcsr=zhaopin.com|utmccn=(referral)|utmcmd=referral|utmcct=/; dywea=95841923.3179178797253694500.1522649313.1526257252.1526257252.11; __utma=269921210.1038731062.1522649313.1526257252.1526257252.12; LastCity%5Fid=530; LastCity=%e5%8c%97%e4%ba%ac; _jzqa=1.3745435935358784500.1525506467.1526257252.1526263683.9; _jzqx=1.1526257252.1526263683.2.jzqsr=zhaopin%2Ecom|jzqct=/.jzqsr=sou%2Ezhaopin%2Ecom|jzqct=/jobs/searchresult%2Eashx; LastSearchHistory=%7b%22Id%22%3a%2268141590-3233-40d3-a0d1-6ce3baa34e13%22%2c%22Name%22%3a%22hadoop+%2b+%e5%8c%97%e4%ba%ac+%2b+%e4%ba%92%e8%81%94%e7%bd%91%e4%ba%a7%e5%93%81%2f%e8%bf%90%e8%90%a5%e7%ae%a1%e7%90%86+...%22%2c%22SearchUrl%22%3a%22http%3a%2f%2fsou.zhaopin.com%2fjobs%2fsearchresult.ashx%3fjl%3d%25e5%258c%2597%25e4%25ba%25ac%26kw%3dhadoop%26isadv%3d0%26ispts%3d1%26isfilter%3d1%26p%3d1%26bj%3d160200%26sj%3d316%22%2c%22SaveTime%22%3a%22%5c%2fDate(1526264445877%2b0800)%5c%2f%22%7d; urlfrom=121126445; urlfrom2=121126445; adfcid=none; adfcid2=none; __utmt=1; dyweb=95841923.13.9.1526263844414; __utmb=269921210.13.9.1526263844418; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1526266327; referrerUrl=; stayTimeCookie=1526266327168'
#     trans = transCookie(cookie)
#     print trans.stringToDict()








#Testing code
#print get_comhrefs()
#print(temp)
#print(temp[1]['href_community'])