'''正则表达式'''
#使用正则表达式:re.match(主要传入两个参数,第一个就是匹配规则,第二个就是需要被过滤的内容)

import re

content = 'Xiaoshuaib has 100 bananas'
res1 = re.match('^Xi.*(\d+)\s.*s$',content)
print(res1.group(1))  # 0

res2 = re.match('^Xi.*?(\d+)\s.*s$',content) #.*？表示的就是匹配任意字符，.代表所有的单个字符，除了 \n \r
print(res2.group(1))  #100

#贪婪匹配:第一段代码一个数一个数都要去匹配
#非贪婪匹配：直接把 100 给匹配出来

import re

content = """Xiaoshuaib has 100 
bananas"""
res = re.match('^Xi.*?(\d+)\s.*s$',content,re.S) #re.S:re 的匹配模式
print(res.group(1))  #100

#re.search：会直接去扫描字符串，然后把匹配成功的第一个结果的返回给你

import re

content = """Xiaoshuaib has 100 
bananas"""
res = re.search('Xi.*?(\d+)\s.*s',content,re.S)
print(res.group(1))  #100

#获取所有的100，re.findall
import re
content = """Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;"""
res = re.findall('Xi.*?(\d+)\s.*?s;',content,re.S)
print(res)   #['100', '100', '100', '100']

#替换100为250：re.sub
import re

content = """Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;"""
content = re.sub('\d+','250',content)
print(content)

#re.compile：封装匹配符
import re

content = "Xiaoshuaib has 100 bananas"
pattern = re.compile('Xi.*?(\d+)\s.*s',re.S)
res = re.match(pattern,content)

print(res.group(1)) #100
