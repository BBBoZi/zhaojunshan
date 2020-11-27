#1.鼠标移动到正确的元素上，显示出没有缺口的图片并下载
#2.点击元素显示出有缺口的图片并下载
#3。对比两张图片找出缺口的移动像素
#4.拖动元素

import time
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from PIL import Image
from io import BytesIO

browser = webdriver.Chrome()

url = "https://www.jd.com/"

# def crop_image(image_file_name):
#     #截取验证码图片
#     #定位某个元素在浏览器中的位置
#     img = browser.find_element_by_xpath("//*[@id='JDJRV-wrap-loginsubmit']/div/div/div/div[1]/div[2]/div[1]")
#     location = img.location
#     print("图片的位置", location)
#     size = img.size
#
#     top, button, left, right = location["y"], location["y"] + size["height"], location["x"], location["x"] + size["width"]
#     print("验证码位置", left, top, right, button)
#     screenshot = browser.get_screenshot_as_png()
#     screenshot = Image.open(BytesIO(screenshot))
#     captcha = screenshot.crop((int(left), int(top), int(right), int(button)))
#     captcha.save(image_file_name)
#     return captcha

def get_tracks(gap):
    track = []  # 移动轨迹
    current = 0  # 当前位移
    # 减速阈值
    mid = gap * 4 / 5  # 前4/5段加速 后1/5段减速
    t = 0.2  # 计算间隔
    v = 0  # 初速度
    while current < gap:
        if current < mid:
            a = 3  # 加速度为+3
        else:
            a = -3  # 加速度为-3
        v0 = v  # 初速度v0
        v = v0 + a * t  # 当前速度
        move = v0 * t + 1 / 2 * a * t * t  # 移动距离
        current += move  # 当前位移
        track.append(round(move))  # 加入轨迹
    return track


def sliding_code(browser):
    # 截取滑块图片
    slider = browser.find_element_by_xpath("//*[@id='JDJRV-wrap-loginsubmit']/div/div/div/div[2]/div[3]")
    ActionChains(browser).move_to_element(slider).perform()
    while True:
        ActionChains(browser).click_and_hold(on_element=slider).perform()
        ActionChains(browser).move_by_offset(xoffset=20, yoffset=0).perform()
        tracks = get_tracks(100)

        for s in tracks:
            ActionChains(browser).move_by_offset(xoffset=s, yoffset=0).perform()

        ActionChains(browser).release().perform()


def login():
    username = "123"
    password = "123"

    browser.get(url)
    browser.maximize_window()
    button = browser.find_element_by_css_selector("#ttbar-login > a.link-login")
    button.click()
    time.sleep(0.5)
    login_page = browser.find_element_by_css_selector("#content > div.login-wrap > div.w > div > div.login-tab.login-tab-r > a")
    login_page.click()

    username_put = browser.find_element_by_xpath("//input[@id='loginname']")
    password_put = browser.find_element_by_xpath("//input[@id='nloginpwd']")
    username_put.send_keys(username)
    password_put.send_keys(password)
    time.sleep(0.5)
    login_button = browser.find_element_by_css_selector("#loginsubmit")
    login_button.click()
    time.sleep(2)

    # #1.鼠标移动到正确的元素上，显示出有缺口的图片并下载
    # slider = browser.find_element_by_xpath("//*[@id='JDJRV-wrap-loginsubmit']/div/div/div/div[2]/div[3]")
    # ActionChains(browser).move_to_element(slider).perform()

    #2.截取图片
    # crop_image("captcha1.png")
    sliding_code(browser)


if __name__ == "__main__":
    login()