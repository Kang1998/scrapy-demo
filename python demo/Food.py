import requests
from lxml import etree
import csv
import time


class Food(object):
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
        self.target = ['http://www.xiachufang.com/category/40076/?page={}'.format(i)for i in range(1, 3)]
        self.rows = []

    def get_lis(self):
        for url in self.target:
            time.sleep(1)
            r = requests.get(url, headers=self.headers)
            html = etree.HTML(r.content)
            lis = html.xpath("//ul[@class='list']/li")
            for e in range(0, len(lis)):
                picture = lis[e].xpath('div/a/div/img/@data-src')
                href = lis[e].xpath('div/a/@href')
                name = lis[e].xpath('div/div/p[@class="name"]/a/text()')[0].strip()
                author = lis[e].xpath('div/div/p[@class="author"]/a/text()')[0].strip()
                stars = lis[e].xpath('div/div/p[@class="stats"]//text()')[1].strip()
                row = [picture, href, name, author, stars]
                if len(row[0]) != 0:
                    self.rows.append(row)

    def csv_writer(self):
        with open('result.csv', 'a', encoding='utf-8') as f:
            w = csv.writer(f)
            w.writerow(['图片', '链接', '菜名', '作者', '评分'])
            for each in self.rows:
                w.writerow(each)


if __name__ == '__main__':
    start = Food()
    start.get_lis()
    start.csv_writer()
