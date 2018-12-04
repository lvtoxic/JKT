# coding=utf-8

import csv
import requests
import json


# 输出列表格式
def readCsvList():
    with open(r'C:\Users\Toxic\Desktop\123.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for item in reader:
            print(item)


# readCsvList()

# 输出字典格式
def readCsvDict():
    with open(r'C:\Users\Toxic\Desktop\123.csv', 'r') as f:
        reader = csv.DictReader(f)
        for item in reader:
            print(dict(item)['URL'])


# readCsvDict()


URL = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%88%90%E9%83%BD&needAddtionalResult=false'


def getHeaders():
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
               'Cookie': 'WEBTJ-ID=20181204224810-16779b0d3c86c8-0aeb53bbf86b87-3f674706-2304000-16779b0d3c92e1; _ga=GA1.2.1359606670.1543934891; _gid=GA1.2.1592565974.1543934891; user_trace_token=20181204224808-9d691955-f7d3-11e8-8ad6-525400f775ce; PRE_HOST=www.baidu.com; LGUID=20181204224808-9d691d84-f7d3-11e8-8ad6-525400f775ce; LGSID=20181204224812-9fae08e6-f7d3-11e8-8ad6-525400f775ce; PRE_UTM=m_cf_cpc_baidu_pc; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.Ks000001qLT2daZnZBpAfe34yQ9LnGf69aUIHFejn8GMiARMDCySd6fCfHy-jjfOL4lEp2hwLD41DAdeo2V1vFQNl6zoM8dS4GIGCpVKCfza4cYBZpqwS-DaF2an3AeJAAG0CYVeVc0vpOrypbudHu5R69uX9i4Wuqq_G7UaXtVTpdsbHjdOKrvdApQ2Yh8e6E7GN8RoBaz_yTQnkf.DD_NR2Ar5Od663rj6tJQrGvKD7ZZKNfYYmcgpIQC8xxKfYt_U_DY2yP5Qjo4mTT5QX1BsT8rZoG4XL6mEukmryZZjzsLTJplePXO-8zNqrw5Q9tSMj_qTr1x9tqvZul3xg1sSxW9qx-9LdJpj_IIBs1f_USMk_R.U1Yk0ZDqs2v4VnL30ZKGm1Yk0Zfqs2v4VnL30A-V5HczPfKM5gKzm6KdpHdBmy-bIfKspyfqnW60mv-b5HczP6KVIjYknjDLg1DsnH-xnH0zndt1njDdg1nvnjD0pvbqn0KzIjYvPHR0uy-b5HDYPH7xnWDknH7xnWm1PHKxnWckPHT0mhbqPj0zg1csP0KVm1YLrj0vPWnknjNxnH0snNtkg1Dsn-ts0Z7spyfqn0Kkmv-b5H00ThIYmyTqn0K9mWYsg100ugFM5H00TZ0qnWc4P1fznW0d0A4vTjYsQW0snj0snj0s0AdYTjYs0AwbUL0qn0KzpWYs0Aw-IWdsmsKhIjYs0ZKC5H00ULnqn0KBI1Ykn0K8IjYs0ZPl5fKYIgnqn1D1PjDkP1bLnHmdPHnvrjnLn0Kzug7Y5HDdPjn4n1f3rjRkrjR0Tv-b5yNbnyDLnhN9nj0snHcznW60mLPV5HIArHR1nHP7wRRYnb7jnYD0mynqnfKsUWYs0Z7VIjYs0Z7VT1Ys0ZGY5H00UyPxuMFEUHYsg1Kxn7tsg100uA78IyF-gLK_my4GuZnqn7tsg1Kxn1D3PWbkg100TA7Ygvu_myTqn0Kbmv-b5HDsP1nLPjD3nWf0ugwGujYVnfK9TLKWm1Ys0ZNspy4Wm1Ys0Z7VuWYs0AuWIgfqn0KhXh6qn0Khmgfqn0KlTAkdT1Ys0A7buhk9u1Yk0Akhm1Ys0APzm1YdnHTknf%26word%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26ck%3D3486.2.470.271.569.138.591.712%26shh%3Dwww.baidu.com%26sht%3Dbaidutop10%26us%3D1.0.2.0.1.302.0%26bc%3D110101; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpc_baidu_pc%26m_kw%3Dbaidu_cpc_cd_e110f9_d2162e_%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591; JSESSIONID=ABAAABAAAFCAAEG79776EAADF04ED47D49E523ECBE1D3BA; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1543934891,1543934895,1543934898; index_location_city=%E6%88%90%E9%83%BD; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1543935518; LGRID=20181204225834-12b33bbf-f7d5-11e8-8ad6-525400f775ce; TG-TRACK-CODE=index_search; SEARCH_ID=20deb5a435594821947c00f909c97a12',
               'Referer': ' https://www.lagou.com/jobs/list_%E6%B5%8B%E8%AF%95?labelWords=&fromSearch=true&suginput='
               }
    return headers


def lagou(page=1):
    r = requests.post(URL, getHeaders(), {'first': True, 'pn': page, 'kd': '测试'})
    print(r.text)
    positions = []
    for i in range(15):
        city=r.json()['content']['positionResult']['result'][i]['city']
        education=r.json()['content']['positionResult']['result'][i]['education']
        positionAdvantage=r.json()['content']['positionResult']['result'][i]['positionAdvantage']
        salary=r.json()['content']['positionResult']['result'][i]['salary']
        companyFullName=r.json()['content']['positionResult']['result'][i]['companyFullName']
        workYear=r.json()['content']['positionResult']['result'][i]['workYear']
        positonLables=r.json()['content']['positionResult']['result'][i]['positionLables']
        position={
            '城市':city,
            '学历':education,
            '工作年限':workYear,
            '福利':positionAdvantage,
            '薪资':salary,
            '公司名称':companyFullName,
            '工作标签':positonLables,
        }
        positions.append(position)
    for item in positions:
        print(item)


def writeCsv():
    headers=['城市','学历','工作年限','福利','薪资','公司名称','工作标签']
    for item in range(1,31):
        positions=lagou(page=item)
        print(positions)




