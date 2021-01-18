# coding = utf-8
__auther__ = "wangtao"

import re
dict_mogo = {}
class Tpi:

    # 把传过来的数据正则匹配下,然后更换下
    @staticmethod
    def parseString(content:str,caches:dict):
        m = re.finditer("\$\{(.+?)\}",content)
        for match in m:
            # 正则表达式匹配去除${}
            strs = re.sub('[\$\{\}]','',match.group())
            o = caches.get(strs)
            content = content.replace(match.group(),str(o))
        return content.strip()


