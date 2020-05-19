import requests
from bs4 import BeautifulSoup
import time

class s(object):
    def __init__(self):
        self.target = "http://search.dangdang.com/?key=java&act=input"
        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
        self.ids = []
