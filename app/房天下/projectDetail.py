from urllib import request
from bs4 import BeautifulSoup
import requests
import time
import string


#项目详情请求
def make_request_detail(dataId,url,headers):
    content ={
        'm': 'xfinfoSy',
        'city': 'wf',
        'id': dataId
    }
    res = requests.post(url, data=content, headers=headers)
    return parse_detail(res.text)

#项目动态请求
def make_request_project_comment(dataId,url,headers):
    res = requests.get(url, headers=headers)
    return parse_project(res.text)


#客户评论请求
def make_request_customer_comment(dataId,url,headers):
    res = requests.get(url, headers=headers)
    # parse_comment(res.text)
    # print(res.text)

# 项目户型请求
def make_request_house_type(dataId,url,headers):
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Host': 'm.fang.com',
               'Referer': 'https://m.fang.com/xf/wf/2415712699.htm',
               'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36'
               }
    url = 'https://m.fang.com/xf.d?m=huXingList&city=wf&newcode=2415199761';
    res = requests.get(url, headers=headers)
    return parse_house_type(res.text,dataId)

# 项目户型解析
def parse_house_type(html,dataId):
    soup = BeautifulSoup(html, "html.parser")
    liList = soup.select('#waphxlist_B01_07 > li')
    for j in liList:
        # print(j)
        hxid = j['hxid']
        print(hxid)
        list = j.select(' a > div.relative')
        jsonlist = []
        for i in list:
            pic_path = 'https://m.fang.com/xf.d?m=album&hx=hx&city=wf&newcode='+str(dataId)+'&hxid='+str(hxid)+'&number=0'
            print(pic_path)
            name = i.select("h2")[0].get_text()
            print(name)
            description = i.select('p')[0].get_text()
            print(description)
            json = {"name": name, "description": description,"pic_path":pic_path}
            jsonlist.append(json)
    return jsonlist

make_request_house_type(2415712699 ,1,1)

#解析客户评论
def parse_comment(html):
    soup = BeautifulSoup(html, "html.parser")
    list = soup.select('#gradelist > section > ul > li')
    # print(list)
    # for i in list:
    #     lilist = i.select('div.comment-text')
        # for j in lilist:
        #     print(j.get_text())



# 解析项目动态
def parse_project(html):
    soup = BeautifulSoup(html, "html.parser")
    list = soup.select('body > div.main > section.mBox.mb8.dtbk > div > ul ')
    jsonArray =[]
    for i in list:
        lilist = i.find_all("li")
        for j in lilist:
            time = j.select("div.time")[0].getText()
            print(type(time))
            print(time)
            content = j.select("h4")[0].getText()
            print(content)
            json={"createTime":time,"content":content}
            jsonArray.append(json)
    return jsonArray


#解析项目详情
def parse_detail(html):
    soup = BeautifulSoup(html, "html.parser")
    list = soup.select('body > div.main > section > div > ul')
    listdescription = soup.select('body > div.main > section.xqxq.mBox.xmjj ')
    average_price = ""
    estate_used = ""
    property_years = ""
    address = ""
    create_user = ""
    state = ""
    open_time = ""
    delivery_time = ""
    building_type = ""
    developer_company = ""
    telephone = ""
    presale_license = ""
    floor_area = ""
    building_area = ""
    volume_rate = ""
    greening_rate = ""
    parking_rate = ""
    house_type = ""
    property_company = ""
    property_costs = ""
    description=""
    json=""
    for j in listdescription:
        desList = j.find_all("p")
        description = desList[0].get_text()
        print(desList[0].get_text())

    for i in list:
        lilist = i.find_all("li")


        for j in lilist:
            if '价<i style="margin-right:2em;"></i>格' in str(j):
                average_price=j.get_text().strip().split('：')[1].strip()
                print(j.get_text().strip().split('：')[1].strip())
            if '物业类别' in str(j):
                estate_used = j.get_text().strip().split('：')[1].strip()
                print(j.get_text().strip())
            if '建筑类型' in str(j):
                building_type=j.get_text().strip().split('：')[1].strip()
                print(j.get_text().strip())
            if '产权年限' in str(j):
                property_years=j.get_text().strip().split('：')[1].strip()
                print(j.get_text().strip().split('：')[1].strip())
            if '开发商' in str(j):
                developer_company=j.get_text().strip().split('：')[1].strip()
                print(j.get_text().strip().split('：')[1].strip())
            if '楼盘地址：' in str(j):
                address=j.get_text().strip().split('：')[1].strip()
                print(j.get_text().strip().split('：')[1].strip())
            if '销售状态' in str(j):
                state=j.get_text().strip().split('：')[1].strip()
                print(j.get_text().strip().split('：')[1].strip())
            if '开盘时间' in str(j):
                open_time=j.get_text().strip().split('：')[1].strip()
                print(j.get_text().strip().split('：')[1].strip())
            if '交房时间' in str(j):
                delivery_time=j.get_text().strip().split('：')[1].strip()
                print(j.get_text().strip().split('：')[1].strip())
            if '咨询电话' in str(j):
                telephone=j.get_text().strip().split('：')[1].strip()
                print(j.get_text().strip().split('：')[1].strip())
            if '预售许可证' in str(j):
                presale_license=j.get_text().strip().split('：')[1].strip()
                print(j.get_text().strip().split('：')[1].strip())
            if '占地面积' in str(j):
                floor_area=j.get_text().strip().split('：')[1].strip()
                print(j.get_text().strip().split('：')[1].strip())
            if '建筑面积' in str(j):
                building_area=j.get_text().strip().split('：')[1].strip()
                print(j.get_text().strip().split('：')[1].strip())
            if '容<i style="margin-right:.5em"></i>积<i style="margin-right:.5em"></i>率' in str(j):
                volume_rate=j.get_text().strip().split('：')[1].strip()
                print(j.get_text().strip().split('：')[1].strip())
            if '绿<i style="margin-right:.5em"></i>化<i style="margin-right:.5em"></i>率' in str(j):
                greening_rate=j.get_text().strip().split('：')[1].strip()
                print(j.get_text().strip().split('：')[1].strip())
            if '停<i style="margin-right:.5em"></i>车<i style="margin-right:.5em"></i>位' in str(j):
                parking_rate=j.get_text().strip().split('：')[1].strip()
                print(j.get_text().strip().split('：')[1].strip())
            if '总<i style="margin-right:.5em"></i>户<i style="margin-right:.5em"></i>数：' in str(j):
                house_type=j.get_text().strip().split('：')[1].strip()
                print(j.get_text().strip().split('：')[1].strip())
            if '物业公司' in str(j):
                property_company=j.get_text().strip().split('：')[1].strip()
                print(j.get_text().strip().split('：')[1].strip())
            if '物<i style="margin-right:.5em"></i>业<i style="margin-right:.5em"></i>费' in str(j):
                property_costs=j.get_text().strip().split('：')[1].strip()
                print(j.get_text().strip().split('：')[1].strip())
    json = {
        "description": description,
        "average_price": average_price,
        "estate_used": estate_used,
        "building_type": building_type,
        "property_years": property_years,
        "developer_company": developer_company,
        "address": address,
        "state": state,
        "open_time": open_time,
        "delivery_time": delivery_time,
        "telephone": telephone,
        "presale_license": presale_license,
        "floor_area": floor_area,
        "building_area": building_area,
        "volume_rate": volume_rate,
        "greening_rate": greening_rate,
        "parking_rate": parking_rate,
        "house_type": house_type,
        "property_company": property_company,
        "property_costs": property_costs
    };
    return json

