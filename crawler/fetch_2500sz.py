from decimal import Decimal
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import urllib.request
import json
import requests
import re
import pandas as pd
import time

link1 = 'http://news.2500sz.com/'


def get_HTML(link_name):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.48 Safari/537.36 Edg/85.0.564.23',
    }

    response = requests.get(link_name, headers=headers)
    # print(response.status_code)
    response.encoding = None
    if response.status_code != 200:
        raise ConnectionError
    result = response.text
    soup = BeautifulSoup(result, 'html.parser')
    return soup


def timer(n, times):
    # 每n秒执行一次
    i = 1

    while times > 0:

        print(time.strftime('%Y-%m-%d %X', time.localtime()))
        print('第' + str(i) + '次执行')
        i += 1
        data = get_HTML(link1)
        level = data.body.div.find("div", attrs={'class': 'clear'}).div.div.find("div", attrs={'class': 'tab'}). \
            find("div", attrs={'class': 'tab-content on'}).ul.findAll("li", attrs={'class': 'type2'})

        for row in level:
            data_low = get_HTML('http://news.2500sz.com/' + row.find("a")['href'])
            data_low_next = data_low.body.div.find("div", attrs={'class': 'content-container'}).findAll('p')
            content = [one_p.text.replace('\u3000', '').replace('\n', '') for one_p in data_low_next]
            print(content)
        time.sleep(n)
        times -= 1


timer(0.1, 100)

print('测试是否阻塞')
