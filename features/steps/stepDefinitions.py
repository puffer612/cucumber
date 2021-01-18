# coding =  utf-8
__auther__ = "wangtao"

from behave import *
import yaml,re
from features.utils.Apis import Api
from features.utils.EnvParamters import EnvParamter
from features.utils.Tpi import Tpi

use_step_matcher("re")

dict_cookies = {}

@Given('api (.*?)')
def getApi(content, api):
    content.api = api



@Given("param")
def getParam(content):
    if content.text:
        strs = Tpi.parseString(content.text,EnvParamter.dict_mongo)
        dict1 = yaml.load(strs,Loader=yaml.FullLoader)
        content.requestData = dict1

@Given("Cookiex is a table")
def setCookiex(content):
    for row in content.table:
        values = EnvParamter.dict_mongo.get(re.sub('[\$\{\}]','',row['value']))
        dict_cookies.setdefault(str(row['key']),values)


@When("GET")
def getResponse(content):
    print(dict_cookies)
    content.responseData = Api.getResponse(content.api,"GET", dict_cookies,{},content.requestData)




@Then('JSONPATH_GET_MONGO')
def getValueFormResponse(content):
    for row in content.table:
        param_key = Api.getObjectValue(row['key'],content.responseData)
        EnvParamter.dict_mongo.setdefault(str(row['value']),param_key)
'''
断言有问题，记得修改下,这个jsonpath提取的时候，是什么带什么，所以如果判断code的时候，把''干掉
'''
@Then('JSONPATH_ASSERT "(.*?)" equals "(.*?)"')
def assertResult(content,resultCode,result):
    code = re.sub('[\']','',Api.getObjectValue(resultCode,content.responseData))
    assert code == result
