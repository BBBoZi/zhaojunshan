#导入 urllib 的请求模块
import urllib.request

#通过 request 模块的 urlopen 方法请求网页：urllib.request.urlopen(url, data=None, [timeout, ]*)
response = urllib.request.urlopen('http://www.baidu.com')
print(response.read().decode('utf-8'))

#模拟登陆论坛
#request 模块中的 Request：urllib.request.Request(url, data=None, headers={}, method=None)
#导入 urllib

from urllib import request,parse

url = 'http://bbs.wuyou.net/forum.php'
headers = {
    #假装自己是浏览器
    'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.366',
}
    #定义请求参数
dict = {
    'mod':'logging',
    'action':'login',
    'loginsubmit':'yes',
    'infloat':'yes',
    'lssubmit': 'yes',
    'inajax': '1',
    'fastloginfield': 'username',
    'handlekey': 'ls',
    'password': 'Zjs2811871',
    'quickforward': 'yes',
    'username': 'zhao350779938',
}
    #把请求的参数转化为 byte
data = bytes(parse.urlencode(dict),'utf-8')
    #封装 request
req = request.Request(url,data=data,headers=headers,method='POST')
    #进行请求
response = request.urlopen(req)
print(response.read())




