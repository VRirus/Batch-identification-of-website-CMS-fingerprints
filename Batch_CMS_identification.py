#! /usr/bin/env python
#by TeamsSix

import sys
import zlib
import json
import requests
import pandas as pd

def whatweb(url):
    response = requests.get(url,verify=False)
    whatweb_dict = {"url":response.url,"text":response.text,"headers":dict(response.headers)}
    whatweb_dict = json.dumps(whatweb_dict)
    whatweb_dict = whatweb_dict.encode()
    whatweb_dict = zlib.compress(whatweb_dict)
    data = {"info":whatweb_dict}
    return requests.post("http://whatweb.bugscaner.com/api.go",files=data)
    
def results(url):
    result = {}
    request = whatweb(url)
    num = request.headers["X-RateLimit-Remaining"]
    print(u"今日识别剩余次数",num)
    req_json = request.json()
    for i in req_json:
        sub_i = req_json[i][0]
        result[i] = sub_i
    result['URL'] = url
    return result

if __name__ == '__main__':
    pools = []
    readDir = sys.argv[1]
    f = open(readDir,"r")
    for url in f.read().split():
        try:
            pools.append(results(url))
        except requests.exceptions.ConnectionError:
            print('连接超时，正在识别下一个URL')
            pass
        except BaseException as e:
            print('程序发生'+str(e)+'异常','正在保存退出')
            os._exit()
        finally:
            df = pd.DataFrame(pools)
            df.to_csv(r'Output_Result.csv',encoding='GB2312')
