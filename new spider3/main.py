import requests
from lxml import  etree
web_url='http://www.75dir.com/w/'
f=open(r'result.txt', 'w',encoding='utf-8')
k=1
for i in range(1,14649):
    url=web_url+str(i)
    try:
        data = requests.get(url,cookies={'JSESSIONID':'301D98D176495CA77A115D520E63302B'}).content.decode('utf-8')
        dom_tree = etree.HTML(data)
        links1=dom_tree.xpath("/html/body/div[2]/div/div/div[1]/div[2]/div/table/tbody/tr[2]/td[1]/a/font")
        links2=dom_tree.xpath("/html/body/div[2]/div/div/div[1]/div[2]/div/table/tbody/tr[3]/td[2]/a")
        print(str(k)+':'+links1[0].text,end='\t')
        k=k+1
        f.write(links1[0].text+'\t')
        print(links2[0].text)
        f.write(links2[0].text+'\n')
    except:
        continue
f.close()