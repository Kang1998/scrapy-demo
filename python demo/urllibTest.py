import urllib.request

class Test(object):
    def __init__(self):
        self.target = "https://www.taobao.com"

    def print(self):
        response = urllib.request.urlopen(self.target)
        # print(response.read().decode('utf-8'))
        print('输出response的类型：', type(response))
        print('输出响应的状态码：', response.status)
        print('输出响应头信息：', response.getheaders())



if __name__ == '__main__':
    a = Test()
    a.print()
