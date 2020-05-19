import requests
from bs4 import BeautifulSoup
import time

class Demo3(object):
    def __init__(self):
        self.target = "http://search.dangdang.com/?key=java&act=input"
        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
        self.ids = []

    def get_id(self):
        respond = requests.get(url=self.target, headers=self.headers)
        soup = BeautifulSoup(respond.text, 'html.parser')
        li = soup.select("#component_59 > li")
        for i in range(0,len(li)):
            li = soup.select("#component_59 > li")[i]
            pageID  = li.attrs["id"][1:]
            self.ids.append(pageID)

    def get_infor(self):
        for index in range(0,len(self.ids)):
            server =  "http://search.dangdang.com/"+str(self.ids[index])+".html"
            print(server)
            r = requests.get(url=server, headers=self.headers)
            soup = BeautifulSoup(r.text, 'html.parser')
            try:
                book_name = soup.select('.name_info > h1')[0].get_text()
                author = soup.select('div.messbox_info > #author > a:nth-child(1)')[0].get_text()
                dd_name = soup.select('div.messbox_info > span:nth-child(2)')[0].get_text()
                price = soup.select("#dd-price")[0].get_text()
                dict1 = {
                    '书名': book_name.strip(),
                    '作者': author,
                    '出版社': dd_name,
                    '价格': price.replace("\n", "").strip()
                }
                print(dict1)
            except IndexError:
                continue
            time.sleep(2)


if __name__ == '__main__':
    aa = Demo3()
    aa.get_id()
    time.sleep(1)
    aa.get_infor()