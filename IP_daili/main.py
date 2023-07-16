import requests

'''
session=requests.Session()
session.proxies = {'http':'http://120.24.33.141:8000','https':'http://47.91.45.198:8080'}
#requests.get(url, headers=headers, proxies=proxies, timeout=3)
print(session.get('http://www.hao123.com'))
'''
import random
import requests

list = open('代理.txt', 'r').readlines()
# 记录成功的ip数量
count_yeah = 0
# 记录失败的ip数量
count_none = 0
for i in list:
    a = i.strip()
    proxies = {
        "HTTP": 'HTTP://' + a,
        "HTTPS": 'HTTPS://' + a,
    }
    print(proxies)
    usa = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'
    ]
    usag = random.choice(usa)
    headers = {
        'User-Agent': usag,
    }
    url = 'https://www.baidu.com/'

    response = requests.get(url, headers=headers, proxies=proxies)
    if response.status_code == 200:
        count_yeah += 1
        with open('可用ip.txt', 'a') as fh:
            fh.write(a + '\n')
            print('{}|{}可用：{}'.format(count_yeah, response.status_code, a))
    else:
        count_none += 1
        with open('不可用ip.txt', 'a') as fh:
            fh.write(a + '\n')
        print('{}|{}可用：{}'.format(count_none, response.status_code, a))