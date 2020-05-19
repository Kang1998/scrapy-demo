# 实训：爬取猫眼电影top100排行榜。2019.10.29有效
import pymongo
import requests
from lxml import etree
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
conn = pymongo.MongoClient('localhost', 27017)
db = conn['douban']
col = db['movie']

def get_info(url):
    res = requests.get(url, headers=headers)
    selector = etree.HTML(res.text)
    infos = selector.xpath('//dl[@class="board-wrapper"]/dd')
    for info in infos:
        rank = info.xpath('i/text()')[0].strip()  # 排名
        title = info.xpath('div/div/div[1]/p[1]/a/text()')[0].strip()  # 电影
        actors = info.xpath('div/div/div[1]/p[2]/text()')[0].strip()  # 主演
        showtime = info.xpath('div/div/div[1]/p[3]/text()')[0].strip()  # 上映时间
        img = info.xpath('a/img[2]/@data-src')[0].strip()  # 海报需要查网页源文件，开发者工具不准
        score1 = info.xpath('div/div/div[2]/p/i[1]/text()')[0].strip()
        score2 = info.xpath('div/div/div[2]/p/i[2]/text()')[0].strip()
        score = score1 + score2  # 评分需要拼接
        row = {'rank': rank, 'title': title, 'actors': actors, 'showtime': showtime, 'score': score, 'img': img}
        col.insert_one(row)
    time.sleep(2)


if __name__ == '__main__':
    urls = ['https://maoyan.com/board/4?offset={}'.format(i) for i in range(0, 21, 10)]
    for url in urls:
        get_info(url)
    head = ['排名', '电影', '主演', '上映时间', '评分', '海报']
