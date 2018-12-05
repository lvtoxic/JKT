# coding=utf-8

import xml.dom.minidom
import os


def getXml(value=None):
    '''获取单节点的数据'''
    xmlFile = xml.dom.minidom.parse('data.xml')
    db = xmlFile.documentElement
    itemList = db.getElementsByTagName(value)
    item = itemList[0]
    return item.firstChild.data
# getXml()


def getUser(parent='wa',child=None):
    '''获取单节点的数据'''
    xmlFile = xml.dom.minidom.parse('data.xml')
    db = xmlFile.documentElement
    itemList = db.getElementsByTagName(parent)
    item = itemList[0]
    return item.getAttribute(child)

print(getUser(child='age'))
