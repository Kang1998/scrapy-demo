import requests
import json
import csv



class YQ_spider(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
        self.server = 'https://gwpre.sina.cn/interface/fymap2020_data.json'
        self.allData = {}

# 对接口发起请求
    def getData(self):
        respond = requests.get(url=self.server, headers=self.headers).content
        toJson =json.loads(respond)
        self.allData = toJson['data']

# 获取国内今日和历史数据
    def getDataCN(self):
        # 将今日的数据跟历史数据合并起来
        # 今日的数据
        #  日期 累计确诊 累计死亡 现存疑似 累计治愈 现存确诊 境外输入
        today = self.allData
        todayData = [today['times'], today["gntotal"], today["sustotal"], today["deathtotal"], today["curetotal"], today["econNum"], today["jwsrNum"]]
        result = []
        title = ['日期', '累计确诊', '累计死亡', '累计治愈', '现存疑似', '现存确诊', '境外输入', '死亡率', '治愈率',
                 '武汉现存', '武汉累计确诊', '武汉累计死亡', '武汉累计治愈', '武汉现存疑似', '国内新增']
        result.append(title)
        result.append(todayData)

        historyData = self.allData['historylist']
        for each in historyData:
            li = [each['date'], each['cn_conNum'], each['cn_deathNum'], each['cn_cureNum'], each['cn_susNum'],
                  each['cn_econNum'], each['cn_jwsrNum'], each['cn_deathRate'], each['cn_cureRate'], each['wjw_susNum'],
                  each['wuhan_conNum'], each['wuhan_deathNum'], each['wuhan_cureNum'], each['wuhan_susNum'], each['cn_conadd']]
            result.append(li)

        downloadToCSV("yq_cn", result)


    def getWorldData(self):
        worldData = self.allData['worldlist']
                    # name  value conNum deathNum  cureNum conadd cureadd deathadd
        worldData.pop(0)
        title = ['国家', '确诊总数', '现存确诊', '死亡总数', '治愈总数', '新增确认', '新增治愈', '新增死亡']
        result = [title]
        try:
            for each in worldData:
                re = [each['name'], each['value'], each['conNum'], each['deathNum'], each['cureNum'], each['conadd'], each['cureadd'], each['deathadd']]
                result.append(re)
        finally:
            downloadToCSV("Yq_world", result)





def downloadToCSV(fileName , dataList):
    try:
        with open(fileName+'.csv', 'a+', newline='') as f:
            w = csv.writer(f)
            w.writerows(dataList)
    finally:
        pass

if __name__ == '__main__':
    a = YQ_spider()
    a.getData()
    a.getDataCN()
    a.getWorldData()
