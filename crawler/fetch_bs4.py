from decimal import Decimal
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import urllib.request
import json
import requests
import re
import pandas as pd
from lxml import etree

link1 = 'https://www.dreamgrow.com/top-15-most-popular-social-networking-sites/'

link2 = 'https://stat.unido.org/COVID-19?_ga=2.268806709.554222338.1599739161-1212675059.1599739161'


# link = "https://www.bilibili.com/ranking/bangumi/13/0/7"


def get_HTML(link_name):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.48 Safari/537.36 Edg/85.0.564.23',
    }

    response = requests.get(link_name, headers=headers)
    print(response.status_code)
    response.encoding = None
    if response.status_code != 200:
        raise ConnectionError
    result = response.text
    soup = BeautifulSoup(result, 'html.parser')
    # print(soup)
    return soup


def str_to_double(df_name):
    for c in range(len(df_name)):
        # print(row)
        if re.search('万', df_name[c]):
            row = df_name[c]
            df_name[c] = Decimal(row[:-1])
        else:
            row = df_name[c]
            row = Decimal(row[:-1])
            df_name[c] = row * 10000


def manage_data():
    soup_doc = get_HTML()
    data = []
    i = 0

    soup_doc_next = soup_doc.find("div", attrs={"class": "rank-list-wrap"})
    soup_doc_next_ul = soup_doc_next.find("ul", attrs={"class": "rank-list pgc-list"})
    soup_find_li = soup_doc_next_ul.find_all('li')
    for s in soup_find_li:
        i += 1
        soup_find_class = s.find("div", attrs={"class": "content"})
        soup_find_name = soup_find_class.find("img")
        soup_find_detail = soup_find_class.find("div", attrs={"class": "detail"})
        data_box = soup_find_detail.find_all("span", attrs={"class": "data-box"})
        play_data = [data.text for data in data_box]
        data.append([i, soup_find_name['alt']] + play_data)

    columns = ["total_rank", "title", "play", "comments", "liked"]
    df = pd.DataFrame(data, columns=columns)
    for name in ["play", "comments", "liked"]:
        str_to_double(df[name])
    print(df)

    df.plot.bar(x=df['title'], y=[df['play']])
    plt.show()


# manage_data()

# get_HTML(link1)

soup = get_HTML(link2)

level = soup.body.div.find("form", attrs={'id': 'form'}).div.div.find("div", attrs={'id': 'form:datasets'}) \
    .find("div", attrs={'class': 'ui-grid-col-4 home-dataset-group'})

level_column = level.find("div", attrs={'class': 'ui-grid-col-12'}).findAll('div')
columns = [row.text.replace("\n", "") for row in level_column]
columns = ['Index', 'compared_to_previous_month	', 'compared_to_same_month_previous_year']
# print(columns)

data = level.findAll('div', attrs={'class': 'ui-grid-col-12 home-dataset-group'})
first = []
second = []
third = []
fourth = []
for row in data:
    content_inside_div = row.findAll('div')
    one_line = [row.text.replace("\n", "").replace(" - ", "0").replace("%", "") for row in content_inside_div]
    first.append(one_line[0])
    # second.append(float(one_line[1]))
    third.append(float(one_line[2]))
    fourth.append(float(one_line[3]))

final_dict = {columns[0]: first,
              # columns[1]: second,
              columns[1]: third,
              columns[2]: fourth}
# print(final_dict)
df_external = pd.DataFrame(final_dict, columns=columns)
print(df_external)
# print(data)
# content = [i.string for i in soup.body.div.article.div.table.tbody.findAll('a')]
# print(dict(zip(content[::2], content[1::2])))
# print(list_final)
