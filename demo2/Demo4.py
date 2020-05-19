import requests
from lxml import etree
import re
import os
import time


# re

class Demo4(object):
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
        self.server = 'https://www.kugou.com/yy/rank/home/1-23784.html?from=rank'


    def getLis(self):
        start = time.time()
        respond = requests.get(url=self.server, headers=self.headers).text
        # print(respond)
        par = '<li class=" " title="(\D*)" data-index="(\d*)">[\s\S]*?<span class="pc_temp_time">\s*([0-9]:[0-9]{2})\s*</span>'
        result = re.findall(par, respond)
        end = time.time()
        t = end-start
        print("代码用时：" + str(t))
        print(result)



if __name__ == '__main__':
        a = Demo4()
        a.getLis()


