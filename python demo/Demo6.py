import requests
from lxml import etree
from bs4 import BeautifulSoup
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
        soup = BeautifulSoup(respond, 'lxml')
        lis = soup.select('div.pc_temp_songlist > ul>li')
        time_size = soup.select('span.pc_temp_time')
        time_sizes = []
        for e in time_size:
            time_sizes.append(e.string.strip('\t\n'))
        title = []
        data_index = []
        for e in lis:
            title.append(e.attrs['title'])
            data_index.append(e.attrs['data-index'])
        for i in zip(title, data_index, time_sizes):
            print(i)

        end = time.time()
        t = end-start
        print("代码用时：" + str(t))


if __name__ == '__main__':
        a = Demo5()
        a.getLis()


