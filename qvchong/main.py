'''
f_read=open(r'./a.txt','r',encoding='utf-8')     #将需要去除重复值的txt文本重命名text.txt
f_write=open(r'./去除重复值后的文本.txt','w',encoding='utf-8')  #去除重复值之后，生成新的txt文本 --“去除重复值后的文本.txt”
data=set()
for a in [a.strip('\n') for a in list(f_read)]:
    if a not in data:
        f_write.write(a+'\n')
        print(a + '\n')
        data.add(a)
f_read.close()
f_write.close()
print('完成')
f_read=open(r'./a.txt','r',encoding='utf-8')
f_write=open(r'./去除重复值后的文本.txt','w',encoding='utf-8')
txt=f_read.readlines()
c=txt.
for line in open("a.txt",encoding='utf-8'):
    try:
        columns = line.split('\t')#分隔符为\t读取文件
    except:
        print("读取文件错误")
        continue
    try:
        if columns[1] not in a:
            f_write.write(a + '\n')
            print(a + '\n')

    # 在fenlei表中查询相应的大分类映射
    print(columns[0])
'''
#f_write1=open(r'./去除重复值后的文本.txt','w',encoding='utf-8')
f_write=open(r'./002.txt','w',encoding='utf-8')
path = "a.txt"  # 数据来源
f = open(path, encoding='utf-8')
line = f.readline()
while line:
    a = line.split('\t')
    b = a[1:]
    b=str(b)[2:-4]

    print(b)
    f_write.write(b+'\n')
    line = f.readline()

f.close()

