# -*- coding: utf-8 -*-
import scrapy
from jianshu.items import JianshuItem
from scrapy import Selector

class JianshuSpider(scrapy.Spider):
    name = 'jianshu_spider'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/c/cyscPK?order_by=added_at&page=1']

    def parse(self, response):
        select = Selector(response)
        lis = select.xpath('//*[@class="note-list"]/li').extract()
        for li in lis:
            li = Selector(text=li)
            title = li.xpath('//*/a[@class="title"]/text()').extract()[0]
            content = li.xpath('//*/p[@class="abstract"]/text()').extract()[0].strip()
            comments = li.xpath('//*/div[@class="meta"]/a[2]/text()').extract()[1].strip()
            like = li.xpath('//*/div[@class="meta"]/span/text()').extract()[-1]

            item = JianshuItem()
            item["title"] = title
            item["content"] = content
            item["comments"] = comments
            item["like"] = like
            yield item

        urls = ['https://www.jianshu.com/c/cyscPK?order_by=added_at&page={}'.format(i)for i in range(2, 5)]
        for url in urls:
            yield scrapy.http.Request(url, callback=self.parse)
        #


