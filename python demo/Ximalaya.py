import requests
import json
from lxml import etree
import re
import os
import time

class Ximalaya(object):
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
        self.server = 'https://www.ximalaya.com/waiyu/yingyu/'
        self.albumIDs = []
        self.albumNames = []
        self.audioInfo = {}

    def get_albumId(self):
        r = requests.get(url=self.server, headers=self.headers)
        html = etree.HTML(r.content)
        li = html.xpath('//*[@class="content"]/ul/li/div//a[@class="album-cover  false lg needhover _FOQv"]')
        for each in li:
            # 获取改页面下的albumID存到列表中
            self.albumIDs.append(re.findall('href="/waiyu/(\d*)/"', str(etree.tostring(each))))

    def ajax_req(self):
        # AJAX请求的实际地址，返回的是json，json中包含的是该albumID对应的audioID
        targets = ["https://www.ximalaya.com/revision/play/v1/show?id={ID}&num=1&sort=-1&size=30&ptype=0".format(ID=each[0]) for each in self.albumIDs]
        for e in targets:
            # print(e)
            req = requests.get(url=e, headers=self.headers)
            js = json.loads(req.text)
            # print((js["data"])["tracksAudioPlay"])    #此时返回的是一个元组数组
            albumName = ((js["data"])["tracksAudioPlay"][0])["albumName"]
            self.albumNames.append(albumName)
            # 一个节目下面对应多个音频id 用数组保存起来
            trackIDs = []
            for each in (js["data"])["tracksAudioPlay"]:
                # 获取了trackId就可以请求audio存放位置的json，
                trackIDs.append(each["trackId"])
            #        合并成一个字典
            self.audioInfo[albumName] = trackIDs
            time.sleep(5)
            self.get_dl_src(albumName)

    def get_dl_src(self, name):
        targets = ['https://www.ximalaya.com/revision/play/v1/audio?id={id}&ptype=1'.format(id=each)for each in self.audioInfo[name]]
        for e in targets:
            re = requests.get(url=e, headers=self.headers).text
            js = json.loads(re)
            data = js["data"]
            trackId = data["trackId"]
            src = data["src"]
            self.download(name,trackId, src)
            time.sleep(3)


    def download(self,name,trackId,src):
        try:
            path = "D:/spider_dl/" +str(name)
            os.mkdir(path)
        except FileExistsError:
            pass
        finally:
            req = requests.get(url=src, headers=self.headers).content
            print("开始下载："+str(name)+"的"+str(trackId) + '.m4a')
            with open(path + '/' + str(trackId) + '.m4a', 'wb') as f:
                f.write(req)
                f.close()
            print("下载" + str(name) + "的" + str(trackId) + '.m4a' + "完毕！")

if __name__ == '__main__':
    aa = Ximalaya()
    aa.get_albumId()
    aa.ajax_req()
