import requests
from lxml import etree
import xlwt
import time


class Food1(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
        self.target = ['http://www.xiachufang.com/category/40076/?page={}'.format(i) for i in range(1, 3)]
        self.rows = [['图片', '链接', '菜名', '作者', '评分']]

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
                row = [picture, href, list(name), list(author), list(stars)]
                if len(row[0]) != 0:
                    self.rows.append(row)

    def write_xlwt(self):
        book = xlwt.Workbook(encoding='utf-8')
        sheet = book.add_sheet('food')
        for i in range(len(self.rows)):
            # sheet.write(self.rows[i][0], self.rows[i][1], self.rows[i][2], self.rows[i][3], self.rows[i][4])
            sheet.write(i, 1, self.rows[i][0])
            sheet.write(i, 2, self.rows[i][1])
            sheet.write(i, 3, self.rows[i][2])
            sheet.write(i, 4, self.rows[i][3])
            sheet.write(i, 5, self.rows[i][4])
        book.save('result.xls')
        #     print(self.rows[i][0], self.rows[i][1], self.rows[i][2], self.rows[i][3], self.rows[i][4])
            # print(self.rows[i])

if __name__ == '__main__':
    start = Food1()
    start.get_lis()
    start.write_xlwt()
