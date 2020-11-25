
##爬取网页需要登陆的网站
#1.添加Coolie，使用.session()持续回话：

headers = {
    # 假装自己是浏览器
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.75 Chrome/73.0.3683.75 Safari/537.36',
    # 把你刚刚拿到的Cookie塞进来
    'Cookie': 'bjo__Session=n2ap09oc7umdos02h4mtps1g08; bjo__user_login=feLyTTdejEVXyL2CEsd4bvc7WtRr7K%2B1car8hhY3tmDZnxo1%2BFfmMPI1OEigDOBpnQ56BoMPG7I3Ovm4zIJbCsz8gMB7%2Fk9p0Z2iErQ9mAyfKAvzOw9Q5vkG%2BIdU5VLls4WcDb4zLZRB3ntsZnlMCQ%3D%3D',
}

session = requests.Session()
response = session.get('https://taobihu.com/', headers=headers)

print(response.text)

#2. 使用Selenium自动登陆

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
WAIT = WebDriverWait(browser, 10)
browser.set_window_size(1400,900)

browser.get("https://taobihu.com/account/login/")


username = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#aw-login-user-name")))
password = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#aw-login-user-password")))
submit = WAIT.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login_submit"]')))

username.send_keys('BBBaoZi')
password.send_keys('zjs2811871')
submit.click()


cookies = browser.get_cookies()