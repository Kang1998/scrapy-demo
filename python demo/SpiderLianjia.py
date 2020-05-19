import requests
from bs4 import BeautifulSoup
import re
import time
import pymysql


class SpiderLianjia(object):
    def __init__(self, pages):
        self.targets = ['https://zh.lianjia.com/ershoufang/pg{page}'.format(page=i) for i in range(1, pages+1)]
        self.server = 'https://zh.lianjia.com/ershoufang/'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
        self.all_links = []

    def get_movie_links(self):
        try:
            for index in range(0, len(self.targets)):
                respond = requests.get(url=self.targets[index], headers=self.headers).text
                current_page_ids = re.findall('href="https://zh.lianjia.com/ershoufang/(\d*).html', respond)
                print('正在保存第{}页的房源链接'.format(index))
                time.sleep(1)
                # 获取到每页对应的所有房源链接保存在all_links[]中
                for i in range(0, len(current_page_ids)):
                    self.all_links.append(self.server+current_page_ids[i]+'.html')
                print('保存第{}页的房源链接完毕'.format(index))
        except IndentationError:
            print("...")

    def dl_mysql(self, house_info, title, avg_price, price):
        db = pymysql.connect("localhost", "root", "cwk646202", "spider")
        cursor = db.cursor()
        sql = 'insert into INFORMATION(house_info, title, avg_price, price) values (%s,%s,%s,%s)'
        cursor.execute(sql, (house_info, title, avg_price, price))
        db.commit()
        db.close()

    def get_info(self):
        try:
            self.all_links = list(set(self.all_links))
            for index in range(0, len(self.all_links)):
                respond = requests.get(url=self.all_links[index], headers=self.headers).text
                time.sleep(1)
                soup = BeautifulSoup(respond, 'html.parser')
                house_info = soup.select(' div.content > div.houseInfo')[0].get_text()
                title = soup.select('div > div.title > h1')[0].get_text()
                avg_price = soup.select('div.price > div.text > div.unitPrice > span')[0].get_text()
                price = soup.select('div.price > span.total')[0].get_text()
                # text = {
                #     '房源': house_info,
                #     '标题': title,
                #     '单价': avg_price + '万',
                #     '总价': price + '万'
                # }
                self.dl_mysql(house_info, title, avg_price, price)
                # self.download(str(text))

        except IndentationError:
            print('...')



    # @staticmethod
    # def download(content):
    #     文件写入之后不是按照utf-8编码写入 是按照gbk写入的，所以还需要手动改一下
        # with open('./content.txt', 'a+') as f:
        #         f.write(content)
        #         f.write('\n\n')
        #         f.close()


if __name__ == '__main__':

    a = SpiderLianjia(20)
    a.get_movie_links()
    a.get_info()

