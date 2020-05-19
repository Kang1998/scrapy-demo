import requests
from bs4 import BeautifulSoup
import time

class Test(object):
    def __init__(self):
        self.keyword = input("请输入关键词")
        self.target = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd="+self.keyword
        self.headers ={ 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

    def req(self):
        # print(self.target)
        respond = requests.get(url=self.target,headers=self.headers)
        soup = BeautifulSoup(respond.text,'html.parser')
        print(soup.prettify())


if __name__ == '__main__':
    a = Test()
    a.req()