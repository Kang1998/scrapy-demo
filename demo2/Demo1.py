import requests,time
from lxml import etree


class Demo1(object):
    def __init__(self):
        self.target = "https://zh.58.com/job/"
        self.headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

    def req(self):
        try:
            respond = requests.get(url=self.target ,headers=self.headers)
            html = etree.HTML(respond.content)
            href = html.xpath('//li[@class="job_item clearfix"]/div/div[@class="job_name clearfix"]/a/@href')
            for i in range(0,len(href)):
                respond1 = requests.get(url=href[i], headers=self.headers)
                html1 = etree.HTML(respond1.content)
                cont = html1.xpath('//*[@class="item_con pos_info"]/div')[0]
                pos_base_info = cont.xpath('//div[@class="pos_base_info"]/span/text()')
                pos_welfare = cont.xpath('//div[@class="pos_welfare"]/span/text()')
                pos_base_condition = cont.xpath('//div[@class="pos_base_condition"]/span[2]/text()')
                pos_area = cont.xpath('//div[@class="pos-area"]/span[2]/text()')
                data ={
                '职位':pos_base_info[0],
                '薪资':pos_base_info[1],
                '福利':pos_welfare,
                '要求':pos_base_condition,
                '地点':pos_area
                }
                time.sleep(2)
                print(data)
        except:
            pass




if __name__ == '__main__':
    start= Demo1()
    start.req()