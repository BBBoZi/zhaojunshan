#导入 web 驱动模块
from selenium import webdriver

#创建一个 Chrome 驱动
driver = webdriver.Chrome()
#使用 get 方法打开百度
driver.get("https://www.baidu.com")

#往输入框里搜索内容
input = driver.find_element_by_css_selector('#kw')
input.send_keys("B站")

#获取到搜索按钮，然后点击
button = driver.find_element_by_css_selector('#su')
button.click()


'''<html>
<body>
 <form id="loginForm">
  <input name="username" type="text" />
  <input name="password" type="password" />
  <input class="login" name="continue" type="submit" value="Login" />
 </form>
</body>
<html>'''

#通过 id 获取 form 表单
login_form = driver.find_element_by_id('loginForm')
#通过 name 获取相应的输入框
username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')
#通过 xpath 获取表单
login_form = driver.find_element_by_xpath("/html/body/form[1]")
login_form = driver.find_element_by_xpath("//form[1]")
login_form = driver.find_element_by_xpath("//form[@id='loginForm']")
#通过标签获取相应的输入框
input1 = driver.find_element_by_tag_name('input')
#通过 class 获取相应的元素
login = driver.find_element_by_class_name('login')

#获取请求链接
driver.current_url
#获取 cookies
driver.get_cookies()
#获取源代码
driver.page_source
#获取文本的值
input.text