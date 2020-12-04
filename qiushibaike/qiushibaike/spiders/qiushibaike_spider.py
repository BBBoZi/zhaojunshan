# -*- coding:utf-8 -*-
import random
import scrapy
from qiushibaike.items import QiushibaikeItem

class QiushiSpider(scrapy.Spider):
    name = "qiushibaike"


    def start_requests(self):
        urls = {
            'https://www.qiushibaike.com/text/page/1/'
        }
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        content_left_div = response.xpath("//*[@id='content']/div/div[2]")
        content_list_div = content_left_div.xpath('./div')

        for content_div in content_list_div:
            item = QiushibaikeItem()
            item['author'] = content_div.xpath('./div/a[2]/h2/text()').get(),
            item['content'] = content_div.xpath('./a/div/span/text()').getall()
            item['_id'] = content_div.attrib['id']
            yield item

        next_page = response.xpath('/html/body/div[1]/div/div[2]/ul/li[8]/a').attrib['href']

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

# items.py：定义我们要存储数据的字段。
# middlewares.py：就是中间件，在这里面可以做一些在爬虫过程中想干的事情，比如爬虫在响应的时候你可以做一些操作。
# pipelines.py：用来定义一些存储信息的文件，比如我们要连接 MySQL或者 MongoDB 就可以在这里定义。
# settings.py：定义我们的各种配置，比如配置请求头信息等。