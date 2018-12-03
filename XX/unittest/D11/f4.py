# coding=utf-8

import requests
'''有安全证书提示ecrt或443的时候用cerify=false可以忽略'''
r = requests.get(url='https://www.12306.cn/mormhweb', verify=False)
print(r.content.decode('utf-8'))
