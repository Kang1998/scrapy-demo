import requests
from bs4 import BeautifulSoup
import time
import re

class Xiaozhu(object):
    def __init__(self):
        self.target = "http://bj.xiaozhu.com/"
        self.headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

    def req(self):
        respond = requests.get(url=self.target ,headers=self.headers)
        soup = BeautifulSoup(respond.text,'html.parser')
        # print(soup.prettify())
        bf = soup.select('.result_btm_con.lodgeunitname')
        # print(bf)
        bf1 = soup.select('#page_list > ul > li')
        for count in range (0,100):
            print(bf1[count].text.replace('\xa0',''))

#             获取北京地区所有房源标题并写入文本文件保存在本地目录，文件名及保存路径自定义，每个标题占一行，注意：实际操作时只爬前两页，并且每页时间间隔20s以上
    def download(self):
            print();

if __name__ == '__main__':
    start= Xiaozhu()
    start.req()