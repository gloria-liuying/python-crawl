from urllib import request
from bs4 import BeautifulSoup
import requests
from projectDetail import make_request_detail,make_request_project_comment,make_request_customer_comment,make_request_house_type


def make_request1(page):

    headers = {'Host': 'm.fang.com',
               'Origin':'https://m.fang.com',
               'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
               'Origin': 'http://deal.ggzy.gov.cn',
               'Referer': 'https://m.fang.com/xf/wf/',
               'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36',
               'X-Requested-With': 'XMLHttpRequest'
                   }
    content = {'m': 'xflist',
                   'city': 'wf',
                   'district': '',
                   'price': '',
                   'comarea': '',
                   'purpose': '',
                   'orderby': '',
                   'railway': '',
                   'character':'',
                   'xq': '',
                   'fitment': '',
                   'round': '',
                   'saleDate': '',
                   'yhtype': '',
                   'datatype': 'json',
                   'p': page,
                   'tags': '',
                   'sell': '',
                   'hxpricerange': '',
                   'bedrooms': ''
               }
    res = requests.post('https://m.fang.com/xf/wf/', data=content, headers=headers)
    return parse(res.text)


def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    list = soup.select('a')
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Host': 'm.fang.com',
               'Referer': 'https://m.fang.com/xf/wf/2415712699.htm',
               'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36'
               }
    # for i in list:
    # 项目详情
    url_detail = 'https://m.fang.com/xf.d?m=xfinfoSy&city=wf&id=2415712699'
    # 项目动态
    url_project_comment = 'https://m.fang.com/xf/wf/2415712699/dongtai.htm'
    # 客户评论
    url_comment_comment = 'https://m.fang.com/xf/wf/2415712699/dianping.htm';
    # 所有户型
    url_project_house_type ='https://m.fang.com/xf.d?m=huXingList&city=wf&newcode=2415199761';
    detail = make_request_detail( 2415712699,url_detail,headers)
    comment_list = make_request_project_comment(2415712699,url_project_comment,headers)
    house_type_list = make_request_house_type(2415712699,url_project_house_type,headers)
    detail["projectComment"] = comment_list
    detail["house_type"] = house_type_list
    print(detail)
    make_request_customer_comment(2415712699,url_comment_comment,headers)
    return detail

make_request1(4)