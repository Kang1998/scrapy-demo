import requests
from bs4 import BeautifulSoup
import time
import re

class Demo(object):
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

if __name__ == '__main__':
    start= Demo()
    start.req()