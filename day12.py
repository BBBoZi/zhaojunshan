import time

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Wechat_Moment():
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.tencent.mm'
        desired_caps['appActivity'] = '.plugin.account.ui.WelcomeActivity'

        # 定义在朋友圈的时候滑动位置
        self.start_x = 300
        self.start_y = 800
        self.end_x = 300
        self.end_y = 300

        # 启动微信
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # 设置等待
        self.wait = WebDriverWait(self.driver, 300)
        print('微信启动...')

    def login(self):
        # 获取到登录按钮后点击
        login_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@resource-id='com.tencent.mm:id/fam']")))
        login_btn.click()
        # 获取使用微信号登录按钮
        change_login_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/d5u")))
        change_login_btn.click()
        # 获取输入账号元素并输入
        account = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.tencent.mm:id/d5j"]')))
        account.send_keys("17608043248")
        # 获取密码元素并输入
        password = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.tencent.mm:id/d62"]')))
        password.send_keys("zjs2811871.")
        # 登录
        login = self.wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/d5n")))
        login.click()
        # # 点击去掉通讯录提示框
        # no_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/doz")))
        # no_btn.click()
        print('登录成功')

    def find_xiaoshuaib(self):
        # 获取到搜索按钮后点击
        search_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/f8y")))
        # 等搜索建立索引再点击
        time.sleep(10)
        search_btn.click()
        # 获取搜索框并输入
        search_input = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.tencent.mm:id/dn7"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]')))
        search_input.send_keys("xiaoshuai")
        print('搜索小帅b...')
        # 点击头像进入
        xiaoshuaib_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/tm")))
        xiaoshuaib_btn.click()
        # 点击右上角...进入
        menu_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//android.support.v7.widget.LinearLayoutCompat')))
        menu_btn.click()
        # 再点击头像
        icon_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/f3y")))
        icon_btn.click()
        # 点击朋友圈
        moment_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/ja")))
        moment_btn.click()
        print('进入朋友圈...')

    def get_data(self):
        while True:
            # 获取 ListView
            items = self.wait.until(EC.presence_of_all_elements_located((By.ID, 'com.tencent.mm:id/d2s')))
            # 滑动
            self.driver.swipe(self.start_x, self.start_y, self.end_x, self.end_y, 2000)
            #遍历获取每个List数据
            for item in items:
                moment_text1 = item.find_element_by_id('com.tencent.mm:id/b_l').text
                moment_text2 = item.find_element_by_id('com.tencent.mm:id/b__').text
                day_text = item.find_element_by_id('com.tencent.mm:id/fmo').text
                month_text = item.find_element_by_id('com.tencent.mm:id/fnr').text
                print('抓取到小帅b文本朋友圈数据： %s' % moment_text1)
                print('抓取到小帅b图像朋友圈数据： %s' % moment_text2)
                print('抓取到小帅b发布时间： %s月%s' % (month_text, day_text))

if __name__ == '__main__':
    wc_moment = Wechat_Moment()
    wc_moment.login()
    wc_moment.find_xiaoshuaib()
    wc_moment.get_data()