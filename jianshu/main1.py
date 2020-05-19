from scrapy import cmdline
cmdline.execute("scrapy crawl jianshu_spider -o jianshu.csv -s FEED_EXPORT_ENCODING=UTF-8".split())
# cmdline.execute("scrapy crawl jianshu_spider".split())