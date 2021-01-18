# coding = utf-8

__auther__ = "wangtao"
import os
def before_all(content):
    print('begin test')
    API_HOST = 'http://192.168.10.102:7010/'
    os.environ.setdefault("API_HOST",API_HOST)

def after_all(content):
    print('finish test')