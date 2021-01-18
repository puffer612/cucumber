aa =  """
   userLoginpwd: "123456qqQQ"
   captcha: ${resultData}
   userMobile: ""
   userLoginname: "YL015359"
   verify: ""
   userEmail: ""
   """
# print(aa)
# pattern = r'\\$\\{(.+?)\\}'
# m = re.compile("\$\{(.+?)\}")
# # b = m.findall(aa)
# # print(type(b))
# ms = re.finditer("\$\{(.+?)\}",aa)
# for match in ms:
#     print(match.group())

#
a = "${aaa}"
# print(re.sub('[${}]','',a))
# b = {}
# # b['a']="2"
# b.setdefault('a','2')
# print(b)
#
# ass = {'captchaToken': 'A3E7371F3D714AF58ABD7B66332C4C84', 'captchaValue': '5237'}
# bss = "resultData"
# c = EnvParamter.getDict().setdefault(bss,ass)
# print(c)
# import jsonpath
# csd =       {'api': 'sc/captcha/captcha', 'result': '000000', 'msg': '', 'data': {'captchaToken': 'FC1D2F5DDA654567902275874EA3DCF6', 'captchaValue': '7383'}, 'gid': 'G2021011811354801000001', 'seqno': '2021011811354801000001', 'cid': '',
#              'timestamp': 1610940949011}
# df=re.sub('[\[\]]','',str(jsonpath.jsonpath(csd,"$.data")))
# print(df)
#
# c = EnvParamter.getDict()
# print(c)
from pathlib import Path
from dotenv import load_dotenv
env_path = Path('.') / '.env'
print(load_dotenv(dotenv_path=env_path))