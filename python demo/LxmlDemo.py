import requests
import json
from lxml import etree
import re
import os
import time

class LxmlDemo(object):
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
        self.server = 'https://zh.58.com/job/'#pn??


    def getLis(self):
        respond = requests.get(url=self.server, headers=self.headers).content
        html = etree.HTML(respond)
        links = html.xpath('//*[@id="jingzhun"]/a')
        # for index in range(len(links)): links[index].attrib['href']
        # print(links[0].attrib['href'])
        r = requests.get(url=links[0].attrib['href'], headers=self.headers).content
        tree = etree.HTML(r)
        result = tree.xpath('//div[@class="item_con pos_info"]')[0]
        res = etree.tostring(result)  ## tostring方法解码是unicode 要用decode解码
        print(res.decode("utf-8"))
        # for each in result:
        #     print(etree.tostring(each))
        # time.sleep(1)

if __name__ == '__main__':
        a = LxmlDemo();
        a.getLis()
