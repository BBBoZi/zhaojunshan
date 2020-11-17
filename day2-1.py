#导入 requests 模块
import requests

#Get 请求
r1 = requests.get('https://api.github.com/events')

#Post 请求
r2 = requests.post('https://httpbin.org/post', data = {'key':'value'})

#其他Http 请求
r3 = requests.put('https://httpbin.org/put', data = {'key':'value'})
r4 = requests.delete('https://httpbin.org/delete')
r5 = requests.head('https://httpbin.org/get')
r6 = requests.options('https://httpbin.org/get')

#携带其他更多参数
payload = {'key1':'value1','key2':'value2'}
r7 = requests.get('https://httpbin.org/get', params=payload)

#假装自己是浏览器
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r8 = requests.get(url, headers=headers)

#获取服务器响应文本内容
import requests
r9 = requests.get('https://api.github.com/events')
print(r9.text,r9.encoding)
#获取字节响应内容
print(r9.content)

#获取响应码
r10 = requests.get('https://httpbin.org/get')
print(r10.status_code)
#获取响应头
print(r10.headers)

#获取 Json 响应内容
import requests
r11 = requests.get('https://api.github.com/events')
print(r11.json())

#获取 socket 流响应内容
r12 = requests.get('https://api.github.com/events', stream=True)
print(r12.raw)
print(r12.raw.read(10))

#Post请求中在一个键里面添加多个值
payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
r13 = requests.post('https://httpbin.org/post', data=payload_tuples)
payload_dict = {'key1': ['value1', 'value2']}
r14 = requests.post('https://httpbin.org/post', data=payload_dict)
print(r13.text)
print(r13.text == r14.text)

#请求的时候用 json 作为参数
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r15 = requests.post(url, json=payload)

#上传文件
url = 'https://httpbin.org/post'
files = {'file': open('report.xls', 'rb')}
r16 = requests.post(url, files=files)
print(r16.text)

#获取 cookie 信息
url = 'http://example.com/some/cookie/setting/url'
r17 = requests.get(url)
print(r17.cookies['example_cookie_name'])

#发送 cookie 信息
url = 'https://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r18 = requests.get(url, cookies=cookies)
print(r18.text)

#设置超时
requests.get('https://github.com/', timeout=0.001)