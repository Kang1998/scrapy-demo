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
        try:
            with open('data.csv','w+') as f:
                line1 = ["菜名","评分","配料","图片"]
                f_csv = csv.writer(f)
                f_csv.writerow(line1)
                lis = html.xpath('//div[@class="normal-recipe-list"]/ul[@class="list"]/li//div[@class="info pure-u"]/p[@class="name"]/a/text()')
                # lis = html.xpath('//div[@class="normal-recipe-list"]/ul[@class="list"]/li[1]//div[@class="info pure-u"]/p[@class="ing ellipsis"]/span/text()')
                print(len(lis))
                print(lis)
                img_src = lis[0].xpath('//*/div/a/div/img/@src')
                # food_name = lis[0].xpath('//div[@class="info pure-u"]/p[@class="name"]/a/text()')
                # ingredient = lis[0].xpath('//div[@class="info pure-u"]/p[@class="ing ellipsis"]/span/text()')
                # print(ingredient)
                # stats = lis[0].xpath('//div[@class="info pure-u"]/p[@class="stats"]/span/text()')
                # # print(food_name,stats,ingredient,img_src)
                # for i in range(0,len(lis)):
                #     f_csv.writerow([food_name[i],stats[i],str(ingredient[i]),img_src])
        except:
            pass





if __name__ == '__main__':
    start= Demo2()
    start.req()