import requests
from lxml import etree
import re
import os
import time


# re

class Demo5(object):
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
        self.server = 'https://www.kugou.com/yy/rank/home/1-23784.html?from=rank'


    def getLis(self):
        start = time.time()
        respond = requests.get(url=self.server, headers=self.headers).content
        html = etree.HTML(respond)
        lis = html.xpath('//*/div[@class="pc_temp_songlist "]/ul/li')
        # print(html.xpath('//li/@title'))
        # for i in range(0, len(lis)):
        title = lis[0].xpath('//li/@title')
        data_index = lis[0].xpath('//li/@data-index')
        t = []
        for e in lis[0].xpath('//li//span[@class="pc_temp_time"]/text()'):
            t.append(e.strip('\t').strip('\n').strip('\t'))
        for i in zip(title, data_index, t):
            print(i)
        end = time.time()
        t = end-start
        print("代码用时：" + str(t))


if __name__ == '__main__':
        a = Demo5()
        a.getLis()


