# coding: utf-8

import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import re

def main():
    url = "https://news.yahoo.co.jp/" 
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    contents = soup.find_all(href=re.compile('news.yahoo.co.jp/pickup'))
    news_table = PrettyTable(
        ["タイトル", "リンク"]
    )
    for content in contents:
        title = content.text
        link = content.attrs['href']
        news_table.add_row([title, link])
    print(news_table)

if __name__=="__main__":
    main()
