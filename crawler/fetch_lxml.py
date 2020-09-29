import requests

from lxml import etree
import pandas as pd


def fetch_dian():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.48 Safari/537.36 Edg/85.0.564.23',
    }

    url = 'http://www.dianping.com/brisbane/ch20/g119r81002o3'
    response = requests.get(url, headers=headers).text
    html = etree.HTML(response)
    data = html.xpath(r"//div[@class='txt']/div[@class='tit']/a[@data-hippo-type='shop']/h4/text()")
    print(data)


def fetch_top():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/85.0.4183.48 Safari/537.36 Edg/85.0.564.23',
    }

    url = 'https://www.dreamgrow.com/top-15-most-popular-social-networking-sites/'
    response = requests.get(url, headers=headers).text
    html = etree.HTML(response)
    data = html.xpath(r"//div[@id='wrapper']/table")
    print(data)


def fetch_virus():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/85.0.4183.48 Safari/537.36 Edg/85.0.564.23',
    }

    url = 'https://stat.unido.org/COVID-19?_ga=2.268806709.554222338.1599739161-1212675059.1599739161'
    response = requests.get(url, headers=headers).text
    html = etree.HTML(response)
    data = html.xpath(
        r"//div[@id='maincontainer']/div[@id='contentcontainer']/form")
    # / form[ @ id = 'form'] / div[ @ id = 'form:datasets']

    print(data)


def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/85.0.4183.48 Safari/537.36 Edg/85.0.564.23',
    }

    url = 'https://www.dreamgrow.com/top-15-most-popular-social-networking-sites/'
    response = requests.get(url, headers=headers).text
    html = etree.HTML(response)
    index = html.xpath(r"//div[@class='entry-inner']/table/tbody/tr/td[@style='text-align: left;']/a/text()")
    value = html.xpath(r"//div[@class='entry-inner']/table/tbody/tr/td[@style='text-align: right;']/a/text()")
    df = pd.DataFrame(value, index=index, columns=['Monthly Active Users'])
    print(df)


if __name__ == '__main__':
    fetch_virus()
