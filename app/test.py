# -*- coding:utf-8 -*-

#设置系统编码
import sys
import importlib
importlib.reload(sys)
import urllib.request
from bs4 import BeautifulSoup
import requests

# 构建请求头
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Content-Type': 'text/html;charset=utf-8',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

def make_request(url,headers):
    # 构建请求
    reqa=''
    try:
        reqa = urllib.request.urlopen(url)
    except:
        print('error')
    html = reqa.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    return soup


def parsePage(soup):
    list = soup.select('a')
    dataId = set()
    for i in list:
        dataId.add(i.get('data-id'))
    return dataId


def req_list():
    url = 'https://m.anjuke.com/wf/loupan/newajax/?is_homeIndex=1&page='+str(2)
    soup = make_request(url, headers)
    dataId = parsePage(soup)
    return dataId

def parse_detail():
    dataId = req_list()
    print(dataId)


parse_detail()