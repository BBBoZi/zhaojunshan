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

def crop_image(image_file_name):
    #截取验证码图片
    #定位某个元素在浏览器中的位置
    img = browser.find_element_by_xpath("//*[@id='JDJRV-wrap-loginsubmit']/div/div/div/div[1]/div[2]/div[1]")
    location = img.location
    print("图片的位置", location)
    size = img.size

    top, button, left, right = location["y"], location["y"] + size["height"], location["x"], location["x"] + size["width"]
    print("验证码位置", left, top, right, button)
    screenshot = browser.get_screenshot_as_png()
    screenshot = Image.open(BytesIO(screenshot))
    captcha = screenshot.crop((int(left), int(top), int(right), int(button)))
    captcha.save(image_file_name)
    return captcha

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

    #1.鼠标移动到正确的元素上，显示出有缺口的图片并下载
    slider = browser.find_element_by_xpath("//*[@id='JDJRV-wrap-loginsubmit']/div/div/div/div[2]/div[3]")
    ActionChains(browser).move_to_element(slider).perform()

    #2.截取图片
    crop_image("captcha1.png")

    ###不会截取 没有缺口的图片




if __name__ == "__main__":
    login()