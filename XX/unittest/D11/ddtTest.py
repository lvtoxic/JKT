# coding=utf-8

import unittest
import requests
import json
import ddt
URL = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'


def getHeaders():
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
               'Cookie': 'JSESSIONID=ABAAABAAADEAAFI4810187CCB712D064EC54C71C5BE9A6C; user_trace_token=20181205142244-0cbedad5-c072-49eb-a66d-70fcfa06fcdf; _ga=GA1.2.1965191215.1543990965; _gid=GA1.2.527844510.1543990965; LGSID=20181205142247-2ec74280-f856-11e8-8bcc-525400f775ce; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dl8jmBmsi7BaVVhQreSIfB2yKRTpOuMWCz6Hi64258LR3xkJg-RZqGKu10NeYIN42%26wd%3D%26eqid%3D86c9da0a000671eb000000065c076ead; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fgongsi%2F147.html; LGUID=20181205142247-2ec74584-f856-11e8-8bcc-525400f775ce; TG-TRACK-CODE=index_search; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1543990966,1543991545; index_location_city=%E5%85%A8%E5%9B%BD; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1543992405; LGRID=20181205144646-8885e87e-f859-11e8-8ce2-5254005c3644; SEARCH_ID=08e737a0f76948cf940a4e3ce5afd15a',
               'Referer': 'https://www.lagou.com/jobs/list_%E6%B5%8B%E8%AF%95?labelWords=&fromSearch=true&suginput='
               }
    return headers

@ddt.ddt
class laGou(unittest.TestCase):
    @ddt.data((1,),(2,),(3,),(4,))
    @ddt.unpack
    def test_lagou(self,page=2):
        positions = []
        r = requests.post(url=URL,headers=getHeaders(),data={'first': True, 'pn': page, 'kd': '测试'})
        print(r.json()['success'])
        self.assertEqual(r.json()['success'],True)



if __name__=='__main__':
    unittest.main(verbosity=2)