# coding = utf-8
__auther__ = "wangtao"

import requests
from features.utils.EnvParamters import EnvParamter
import json
import jsonpath
import re

class Api:

    # 定义api,并返回数据
    @staticmethod
    def getResponse(api:str,method:str,cookies:dict,headers:dict,params:dict):
        # 验证api host
        if api.startswith("http") or api.startswith("https"):
            api = api
        else:
            api = EnvParamter.getEnvParamters()+api

        if method == 'GET':
            param = json.dumps(params)
            param = "params="+param
            response = requests.get(api,params=param,headers=headers,cookies=cookies)
        elif method == 'POST':
            response = requests.post(api,data=params,headers=headers,cookies=cookies)
        return response

    # 返回服务器响应状态码
    @staticmethod
    def getStatusCode(response:requests):
        if response != None:
            statusCode = response.status_code
        return statusCode

    #JsonPath 提取
    @staticmethod
    def getObjectValue(JsonPath:str,response:requests):
        json_response = response.json()
        return re.sub('[\[\]]','',str(jsonpath.jsonpath(json_response,JsonPath)))




