from scrapy import cmdline
cmdline.execute("scrapy crawl douban -o douban.csv -s FEED_EXPORT_ENCODING=UTF-8".split())
# cmdline.execute("scrapy crawl douban".split())