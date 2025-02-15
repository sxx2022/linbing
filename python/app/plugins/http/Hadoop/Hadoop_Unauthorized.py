#!/usr/bin/env python3

from app.lib.common import get_useragent
from app.lib.request import request

class Hadoop_Unauthorized_BaseVerify:
    def __init__(self, url):
        self.info = {
            'name': 'Hadoop 未授权访问漏洞',
            'description': 'Hadoop 未授权访问漏洞',
            'date': '',
            'exptype': 'check',
            'type': 'Unauthorized'
        }
        self.url = url
        if not self.url.startswith("http") and not self.url.startswith("https"):
            self.url = "http://" + self.url
        self.headers = {
            'User-Agent': get_useragent()
        }

    async def check(self):
        
        """
        检测是否存在漏洞

        :param:

        :return bool True or False: 是否存在漏洞
        """
        
        try:
            req = await request.get(self.url + '/cluster/cluster', headers = self.headers)
            if "hbase" in await req.text() or "url=/rs-status" in await req.text() or "hadoop" in await req.text():
                return True
            
        except Exception as e:
            # print(e)
            pass

if  __name__ == "__main__":
    Hadoop_Unauthorized = Hadoop_Unauthorized_BaseVerify('http://baidu.com')
    Hadoop_Unauthorized.check()