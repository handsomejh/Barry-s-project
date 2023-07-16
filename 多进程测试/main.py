import multiprocessing
import queue
import random
from multiprocessing import Process
import time
from lxml import etree

import requests
import yaml



class MyProcess (Process):

    def __init__(self, name, web_num, q):
        super(MyProcess, self).__init__()
        self.name = name
        self.web_num = web_num
        self.q = q

    def run(self):
        print ("开始进程：" + self.name)
        my_process(self.name, self.web_num, self.q)
        print ("退出进程：" + self.name)

def my_process(threadName,web_num,q):
    f = open(r'config.yml')  # 打开待爬取网页列表
    y = yaml.safe_load(f)
    # ============================================================================================================
    web_url = y[web_num]['front_url']  # 赋值操作
    first_page = y[web_num]['first_num']  # 赋值操作
    final_page = y[web_num]['final_num']  # 赋值操作
    url_Xpath = y[web_num]['url_Xpath']  # 赋值操作
    class_Xpath = y[web_num]['class_Xpath']  # 赋值操作
    for i in range(first_page, final_page):  # 对每一个网站开始爬取
        url = web_url + str(i) + '.html'
        try:
            data = requests.get(url, cookies={'JSESSIONID': '301D98D176495CA77A115D520E63302B'}).content.decode(
                    'utf-8')
            dom_tree = etree.HTML(data)
            links1 = dom_tree.xpath(url_Xpath)
            links2 = dom_tree.xpath(class_Xpath)
            if web_num==1:
                print('生产者-'+threadName+'\t'+'队列大小：'+str(q.qsize())+'\t' + links1[0].text[5:], end='\t')
                q.put(links2[0].text+'\t'+links1[0].text[5:])
            else:
                print('生产者-'+threadName+'\t'+'队列大小：'+str(q.qsize())+'\t' + links1[0].text, end='\t')
                q.put(links2[0].text + '\t' + links1[0].text)
            print(links2[0].text)
            #print('队列大小：'+str(q.qsize()))
        except:
            continue
    f.close()

class MyProcess1 (Process):

    def __init__(self, name,q):
        super(MyProcess1, self).__init__()
        self.name = name
        self.q = q

    def run(self):
        print ("开始线程：" + self.name)
        my_processd2(self.name,self.q)
        print ("退出线程：" + self.name)

def my_processd2(name,q):
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
            res = requests.get(str(url), headers=headers,timeout=2)
            if res.status_code == 200:
                f2.writelines(w)
                print(name+'\t'+w[:] + '\t' + '成功写入')
            else:
                print(name+'\t'+url + '\t' + '不可访问URL,状态码：' + str(res.status_code))
        except:
            print(name+'\t'+"无法建立连接！")



if __name__ == '__main__':
    q = multiprocessing.Queue(maxsize=10000)
    '''
    
    p1=Process(target=my_process,args=('1',1,q,))
    p2=Process(target=my_process,args=('2',2,q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    '''


    for i in range(1,5):
        p = MyProcess(str(i),i,q)
        p.start()
    for i in range(5,10):
        p = MyProcess1(str(i),q)
        p.start()
    for i in range(1,5):
        p.join()
    for i in range(5,10):
        p.join()





