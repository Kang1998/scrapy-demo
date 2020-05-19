import requests,time
from lxml import etree
import os
import csv



class Demo2(object):
    def __init__(self):
        self.target = "http://www.xiachufang.com/category/40076"
        self.headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

    def req(self):
        respond = requests.get(url=self.target, headers=self.headers)
        html = etree.HTML(respond.content)
        xpath_li = '//div[@class="pure-u-3-4 category-recipe-list"]/div[@class="normal-recipe-list"]/ul/li'
        lis = html.xpath(xpath_li)
        food_name = []
        for i in range(1, len(lis)+1):
            a = html.xpath(xpath_li + '[{}]//div[@class="info pure-u"]/p[@class="name"]/a/text()'.format(i))
            # b = html.xpath(xpath_li + '[{}]//div[@class="cover pure-u"]/img/@src'.format(i))
            food_name.append(a[0].strip('\n').strip())
            # print(b)

        img_src = lis[0].xpath(xpath_li+'/div/a/div/img/@src')
        print(img_src)
        print(food_name)
        # ingredient = lis[0].xpath('//div[@class="info pure-u"]/p[@class="ing ellipsis"]/span/text()')
        # stats = lis[0].xpath('//div[@class="info pure-u"]/p[@class="stats"]/span/text()')





if __name__ == '__main__':
    start= Demo2()
    start.req()