from decimal import Decimal
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import urllib.request
import json
import requests
import re
import pandas as pd
import time

link1 = 'https://bbs.52kd.com/forum-1724-1.html'


def get_HTML(link_name):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.48 Safari/537.36 Edg/85.0.564.23',
    }

    response = requests.get(link_name, headers=headers)
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
        level = data.body.find('div', attrs={'id': 'wp'}).find('div', attrs={'class': 'mn'}). \
            find('div', attrs={'class': 'bm_c xld'}).findAll('dl', attrs={'class': 'bbda cl'})

        for one_row in level:
            data_low = get_HTML('http://www.zjgxw.com/' + one_row.dt.a['href'])
            data_low_next = data_low.body.find("div", attrs={'id': 'wp'}).find("div", attrs={'class': 'ct2 wp cl'}) \
                .find("div", attrs={'class': 'bm vw'}).h1
            print(data_low_next)

        time.sleep(n)
        times -= 1


timer(0.5, 100)

print('测试是否阻塞')
