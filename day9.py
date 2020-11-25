##1.使用开源IP代理池：https://github.com/Python3WebSpider/ProxyPool.git
##2.安装配置redis
##3.安装相关所需的 python 模块：pip3 install -r requirements.txt
##4.开启 redis：redis-server /usr/local/etc/redis.conf
##5.接着运行 run.py
##6.使用RDM查看在redis中爬取到的代理ip

import requests

proxypool_url = 'http://127.0.0.1:5555/random'
target_url = 'https://www.baidu.com/'

def get_random_proxy():
    """
    get random proxy from proxypool
    :return: proxy
    """
    return requests.get(proxypool_url).text.strip()

def crawl(url, proxy):
    """
    use proxy to crawl page
    :param url: page url
    :param proxy: proxy, such as 8.8.8.8:8888
    :return: html
    """
    proxies = {'http': 'http://' + proxy}
    return requests.get(url, proxies=proxies).text


def main():
    """
    main method, entry point
    :return: none
    """
    proxy = get_random_proxy()
    print('get random proxy', proxy)
    html = crawl(target_url, proxy)
    print(html)

if __name__ == '__main__':
    main()