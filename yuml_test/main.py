import yaml
import requests
from lxml import etree

f = open(r'config.yml')
y = yaml.safe_load(f)
f=open(r'result.txt', 'w',encoding='utf-8')#打开存储文件

k=1#计数器
#============================================================================================================
for j in range(5,1000):
    if(j not in y):
        break
    web_url = y[j]['front_url']
    first_page = y[j]['first_num']
    final_page = y[j]['final_num']
    url_Xpath = y[j]['url_Xpath']
    class_Xpath = y[j]['class_Xpath']
    for i in range(first_page, final_page):
        url = web_url + str(i)+'.html'
        try:
            data = requests.get(url, cookies={'JSESSIONID': '301D98D176495CA77A115D520E63302B'}).content.decode('utf-8')
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