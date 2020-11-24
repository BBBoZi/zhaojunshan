from flask import Flask
from flask import request
import requests

app = Flask(__name__)

@app.route('/getInfo')
def hello_world():
    if(str(request.headers.get('User-Agent')).startswith('python')):
        return "小子，使用爬虫是吧？滚你的"
    else:
        return "这里假装有很多数据"

@app.route('/')
def index():
    return "个人主页"


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    url = 'http://127.0.0.1:5000/getInfo'
    response = requests.get(url, headers=headers)
    print(response.text)