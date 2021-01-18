# coding = utf-8
__auther__ = "wangtao"
import os

class EnvParamter:


    # 获取系统变量api
    @staticmethod
    def getEnvParamters():
        return os.environ.get("API_HOST")


    #获取系统数据库的api
    @staticmethod
    def getDBParamters():
        return os.environ.get("DB_HOST")

    # 设置系统dict
    dict_mongo = {}



