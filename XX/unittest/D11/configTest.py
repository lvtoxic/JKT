# coding=utf-8
import configparser
import os


def base_dir(filename=None):
    return os.path.join(os.path.dirname(__file__), filename)


def getLinux(linux='linux'):
    list1 = []
    config = configparser.ConfigParser()
    config.read(base_dir('config.ini'))
    ip = config.get(linux, 'IP')
    port = config.get(linux, 'PORT')
    username = config.get(linux, 'USERNAME')
    password = config.get(linux, 'PASSWORD')
    list1.append(ip)
    list1.append(port)
    list1.append(username)
    list1.append(password)
    return list1

print(getLinux())