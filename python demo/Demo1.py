import requests
from bs4 import BeautifulSoup
import time

class Demo1(object):
    def __init__(self):
        self.target = "https://www.xiami.com/billboard/328"
        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

    def get_req(self):
        respond = requests.get(url=self.target, headers=self.headers)
        print(respond)
        soup = BeautifulSoup(respond.text, 'html.parser')

        def select(s):
            bf = soup.select(s)[0].get_text()
            return bf

        for i in range(1, len(soup.select("tr"))):
            top = select("tr:nth-child("+str(i)+") > td:nth-child(1) > div > span")
            songs = select("tr:nth-child("+str(i)+") > td:nth-child(4) > div")
            singers = select("tr:nth-child("+str(i)+") > td:nth-child(5) > div")
            albums = select("tr:nth-child("+str(i)+") > td:nth-child(6) > div")
            durations = select("tr:nth-child("+str(i)+") > td:nth-child(7) > div > span")
            time.sleep(1)
            dict1 = {
                '排名': top,
                '歌名': songs,
                '歌手': singers,
                '专辑': albums,
                '时长': durations
            }
            print(dict1)

if __name__ == '__main__':
    aa = Demo1()
    aa.get_req()