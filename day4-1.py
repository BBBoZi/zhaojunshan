# 爬取豆瓣最受欢迎的250部电影，并写入Excel表格中
import requests
import xlwt
from bs4 import BeautifulSoup

# 请求豆瓣网站，获取网页源码
def request_douban(url):
    try :
        # 请求url
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
        response = requests.get(url,headers=headers)
        # 判断网页的返回码是不是200
        print(response.status_code)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None
book = xlwt.Workbook(encoding="utf-8",style_compression=0 )
# 先定义一个Excel表格，写好名称，图片等信息
sheet = book.add_sheet("豆瓣电影Top250",cell_overwrite_ok=True)
sheet.write(0,0,"名称")
sheet.write(0,1,"图片")
sheet.write(0,2,"排名")
sheet.write(0,3,"评分")
sheet.write(0,4,'作者')
sheet.write(0,5,"简介")

n = 1

#将爬取下来的电影信息写入Excel表格中
def save_to_excel(soup):
    # 将存放电影信息的li标签写入列表中
    movie_lists = soup.find(class_="grid_view").find_all("li")
    # 从列表中的源网页解析出电影的名称，作者等信息
    for movie in movie_lists:
        movie_name = movie.find(class_="title").string
        movie_img = movie.find('a').find('img').get("src")
        movie_index = movie.find(class_='').string
        movie_score = movie.find(class_="rating_num").string
        movie_author = movie.find('p').get_text()
        movie_author = movie_author.replace(" ",'')
        movie_author = movie_author.replace("\n",'')
        if (movie.find(class_="inq") !=None):
            movie_intr = movie.find(class_="inq").string
        print('爬取电影：' + movie_index + ' | ' + movie_name + ' | ' + movie_score + ' | '+movie_author  + movie_intr)
        # 将解析出的电影信息写入到Excel表格中
        global n

        sheet.write(n, 0, movie_name)
        sheet.write(n, 1, movie_img)
        sheet.write(n, 2, movie_index)
        sheet.write(n, 3, movie_score)
        sheet.write(n, 4, movie_author)
        sheet.write(n, 5, movie_intr)
        n = n + 1
# 定义主函数
def main(page):
    # 定义请求网页的url链接
    url = 'https://movie.douban.com/top250?start=' + str(page * 25) + '&filter='
    # 请求网页
    html = request_douban(url)
    # 将收到的网页全部展示
    soup = BeautifulSoup(html, "lxml")
    save_to_excel(soup)

if __name__ == "__main__":
    for index in range(0,10):
        main(index)
    # 保存Excel表格
    book.save(r'/Users/jason/Desktop/豆瓣最受欢迎的250部电影.xls')