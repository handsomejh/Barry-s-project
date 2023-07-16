import requests  # 数据请求模块
import parsel  # 数据解析模块
import csv  # 数据保存模块
import re
import random


list = open('代理.txt', 'r').readlines()

for page in range(1, 101):
    print(f'\n===================正在抓取第{page}页数据======================')
    prox = random.choice(list)
    prox = prox.strip()

    prox = {"HTTPS": 'HTTPS://' + prox}
    # 1.找数据对应的url地址，分析网页性质
    #url = f'https://nanjing.esf.fang.com/house/i3{page}/'
    #print(url)

    url = 'https://www.baidu.com/'
    # 表示浏览器身份标识，伪装成一个浏览器用户
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

    # 2.发送指定地址的请求q
    response = requests.get(url=url, headers=headers, proxies=prox)
    #print(response.status_code)
    html_data = response.text
    # print(response.text)

    # 3.数据解析 xpath css选择器提取HTML数据
    s = parsel.Selector(html_data)  # 转换数据类型
    #print(s)
    # print(s)
    lis = s.xpath('//div')
    print(lis)
    for li in lis:
        name = li.xpath('.//h4[@class="clearfix"]/a/span/text()').get()
        if name:
            name = name.strip()  # 去除字符串前面两端空格
        print(name)
        price = li.xpath('.//dd[@class="price_right"]/span/b/text()').get()
        if price != None:
            price = price + '万'
        else:
            print("未取得营业凭证")
        room = li.xpath('.//p[@class="tel_shop"]/text()').getall()

        # 4.数据保存
        with open('房天下.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_write = csv.writer(f)
            csv_write.writerow([name, price, room])