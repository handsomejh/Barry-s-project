import requests
from lxml import  etree
'''
web_url='http://42824.com/update/0-'
f=open(r'result.txt', 'w',encoding='utf-8')
k=1
for i in range(1,7841):    #爬页面
    url=web_url+str(i)+'.html'
    try:
        data = requests.get(url,cookies={'JSESSIONID':'301D98D176495CA77A115D520E63302B'}).content.decode('utf-8')
        dom_tree = etree.HTML(data)
        for j in range(1,11):
            links1=dom_tree.xpath('//*[@id="listbox"]/ul/li['+str(j)+']/div/address/a[1]')
            print(str(k)+':'+links1[0].text,end='\n')
            k=k+1
            f.write(links1[0].text+'\n')
    except:
        continue
'''
web_url='http://42824.com/'
f=open(r'result1.txt', 'w',encoding='utf-8')
f1=open(r'result.txt', 'r',encoding='utf-8')
k=1
txt=f1.readlines()
for i in txt:    #爬页面
    url=web_url+i[:-1]+'/'
    try:
        data = requests.get(url,cookies={'JSESSIONID':'301D98D176495CA77A115D520E63302B'}).content.decode('utf-8')
        dom_tree = etree.HTML(data)
        links1=dom_tree.xpath('//*[@id="wrapper"]/div[2]/a[5]')
        print(str(k)+':'+i[:-1]+'\t'+links1[0].text,end='\n')
        k=k+1
        f.write(i[:-1]+'\t'+links1[0].text+'\n')
    except:
        continue
f.close()
f1.close()