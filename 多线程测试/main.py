import queue
import threading
import time
import _thread
import yaml
import requests
from lxml import etree
import random
'''
def my_thread(threadName,web_num):
    print("开始进程"+str(web_num))
    f = open(r'config.yml')  # 打开待爬取网页列表
    y = yaml.safe_load(f)
    f = open(r'spider_result.txt', 'w', encoding='utf-8')  # 打开存储url文件

    k = 1  # 计数器
    # ============================================================================================================
    for j in range(web_num, 1000):  # 遍历爬取网页列表
        if (j not in y):
            break
        web_url = y[j]['front_url']  # 赋值操作
        first_page = y[j]['first_num']  # 赋值操作
        final_page = y[j]['final_num']  # 赋值操作
        url_Xpath = y[j]['url_Xpath']  # 赋值操作
        class_Xpath = y[j]['class_Xpath']  # 赋值操作
        for i in range(first_page, final_page):  # 对每一个网站开始爬取
            url = web_url + str(i) + '.html'
            try:
                data = requests.get(url, cookies={'JSESSIONID': '301D98D176495CA77A115D520E63302B'}).content.decode(
                    'utf-8')
                dom_tree = etree.HTML(data)
                links1 = dom_tree.xpath(url_Xpath)
                links2 = dom_tree.xpath(class_Xpath)
                print(str(k) + ':' + links1[0].text, end='\t')
                print(links2[0].text)
                k = k + 1
                f.write(links1[0].text + '\t')
                f.write(links2[0].text + '\n')
            except:
                continue
    f.close()

try:
    _thread.start_new_thread(my_thread, ("Thread-1", 1,))
    _thread.start_new_thread(my_thread, ("Thread-2", 3,))
except:
    print("错误，无法启动线程！"
'''
q=queue.Queue(maxsize=1000)
class myThread (threading.Thread):

    def __init__(self, threadID, name, web_num):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.web_num = web_num

    def run(self):
        print ("开始线程：" + self.name)
        my_thread(self.name, self.web_num)
        print ("退出线程：" + self.name)

def my_thread(threadName,web_num):
    f = open(r'config.yml')  # 打开待爬取网页列表
    y = yaml.safe_load(f)
    f = open(r'spider_result.txt', 'w', encoding='utf-8')  # 打开存储url文件
    k = 1  # 计数器

    # ============================================================================================================
    for j in range(web_num, 1000):  # 遍历爬取网页列表
        if (j not in y):
            break
        web_url = y[j]['front_url']  # 赋值操作
        first_page = y[j]['first_num']  # 赋值操作
        final_page = y[j]['final_num']  # 赋值操作
        url_Xpath = y[j]['url_Xpath']  # 赋值操作
        class_Xpath = y[j]['class_Xpath']  # 赋值操作
        for i in range(first_page, final_page):  # 对每一个网站开始爬取
            url = web_url + str(i) + '.html'
            try:
                data = requests.get(url, cookies={'JSESSIONID': '301D98D176495CA77A115D520E63302B'}).content.decode(
                    'utf-8')
                dom_tree = etree.HTML(data)
                links1 = dom_tree.xpath(url_Xpath)
                links2 = dom_tree.xpath(class_Xpath)
                if web_num==1:
                    print(threadName + '\t' + str(k) + ':' + links1[0].text[5:], end='\t')
                    q.put(links2[0].text+'\t'+links1[0].text[5:])
                else:
                    print(threadName+'\t'+str(k) + ':' + links1[0].text, end='\t')
                    q.put(links2[0].text + '\t' + links1[0].text)
                print(links2[0].text)
                k = k + 1
                f.write(links1[0].text + '\t')
                f.write(links2[0].text + '\n')
                print('队列大小：'+str(q.qsize()))
            except:
                continue
    f.close()

class myThread2 (threading.Thread):

    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        print ("开始线程：" + self.name)
        my_thread2(self.name)
        print ("退出线程：" + self.name)

def my_thread2(threadName):
    requests.packages.urllib3.disable_warnings()
    f2 = open(r'useful_result.txt', 'w', encoding='utf-8')
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
    for i in range(1,1000000):
        w = q.get()
        url = ('http://' + w.split('\t')[1])+ '/'
        try:
            res = requests.get(str(url), headers=headers)
        except:
            print(threadName+'\t'+"无法建立连接！")
        if res.status_code == 200:
            f2.writelines(w)
            print(threadName+'\t'+w[:] + '\t' + '成功写入')
        else:
            print(threadName+'\t'+url + '\t' + '不可访问URL,状态码：' + str(res.status_code))


# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
thread3 = myThread(3, "Thread-3", 3)
thread4 = myThread2(4, "Thread-4")
thread5 = myThread2(5, "Thread-5")
thread6 = myThread2(6, "Thread-6")
thread7 = myThread2(7, "Thread-7")
thread8 = myThread2(8, "Thread-8")
thread9 = myThread2(9, "Thread-9")


#thread5 = myThread(5, "Thread-5", 5)
# 开启新线程
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread9.start()



thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
thread6.join()
thread7.start()
thread8.start()
thread9.start()

print ("退出主线程")