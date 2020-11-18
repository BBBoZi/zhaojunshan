#补充正则表达式知识点

'''match()'''

import re

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(result)
print(result.group())
print(result.span())

#匹配目标：调用group()方法传入分组的索引即可获取提取的结果
import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\sWorld', content)
print(result)
print(result.group())
print(result.group(1))

#通用匹配：.*
import re

content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^Hello.*Demo$', content)
print(result)
print(result.group())
print(result.span())

#贪婪与非贪婪
##贪婪匹配
import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*(\d+).*Demo$', content)
print(result)
print(result.group(1)) #7, 贪婪匹配：.*尽可能匹配多的字符

##非贪婪匹配
import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*?(\d+).*Demo$', content)
print(result)
print(result.group(1)) #1234567,费贪婪匹配：.*?尽可能匹配少的字符。 .*?在末尾可能匹配不到任何内容

#修饰符
import re

content = '''Hello 1234567 World_This
is a Regex Demo
'''
#result = re.match('^He.*?(\d+).*?Demo$', content)
#print(result.group(1)) #报错
result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
print(result.group(1)) #1234567

#转义匹配
import re

content = '(百度)www.baidu.com'
result = re.match('\(百度\)www\.baidu\.com', content)
print(result)


'''search()'''
import re

content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
#result = re.match('Hello.*?(\d+).*?Demo', content)
#print(result) #报错，因为match()方法在使用时需要考虑到开头的内容，它更适合用来检测某个字符串是否符合某个正则表达式的规则
result = re.search('Hello.*?(\d+).*?Demo', content)
print(result)


'''findall()'''

import re

content = """Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;"""
res = re.findall('Xi.*?(\d+)\s.*?s;',content,re.S)
print(res)   #['100', '100', '100', '100']:#获取所有的100，re.findall


'''sub()'''
#替换100为250：re.sub
import re

content = """Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;"""
content = re.sub('\d+','250',content)
print(content)

'''compile()'''
#re.compile：封装匹配符
import re

content = "Xiaoshuaib has 100 bananas"
pattern = re.compile('Xi.*?(\d+)\s.*s',re.S)
res = re.match(pattern,content)

print(res.group(1)) #100



