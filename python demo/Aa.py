import requests


if __name__ == '__main__':
    header ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
    re = requests.get(url='https://www.ximalaya.com/revision/play/v1/audio?id=178401535&ptype=1',headers=header).text
    print(re.status_code)
    print()