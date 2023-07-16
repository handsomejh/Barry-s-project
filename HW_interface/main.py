#华为接口查询

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
#打开存放url的文件
f1 = open(r'4000.txt', 'r',encoding='utf-8')
f2 =open(r'result.txt', 'w',encoding='utf-8')
#按行读取文件内容
txt=f1.readlines()
#准备url
url='https://isecurity.huawei.com/sec/web/urlClassification.do'
i=1 #计数器
for w in txt:
    try:
        driver.get(url)