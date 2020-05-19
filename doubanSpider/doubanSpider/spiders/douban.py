# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from doubanSpider.items import DoubanspiderItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/review/best/?start=10']

    def parse(self, response):
        s = Selector(response)
        divs = s.xpath('//*[@id="content"]/div/div[1]/div[1]').extract()
        # print(divs[0])
        for div in divs:
            s = Selector(text=div)
            name = s.xpath('//header/a[2]/text()').extract()
            time = s.xpath('//header/span[2]/text()').extract()
            title = s.xpath('//div/h2/a/text()').extract()
            content = s.xpath('//div[@class="short-content"]/text()').extract()
            newContent = []
            for c in content:
                t = c.strip()
                if t != '' and t != ')':
                    newContent.append(t)
            # print(len(name), len(time), len(title), len(newContent))
            for i in range(0, len(name)):
                item = DoubanspiderItem()
                item['name'] = name[i]
                item['time'] = time[i]
                item['title'] = title[i]
                item['content'] = newContent[i]
                yield item

