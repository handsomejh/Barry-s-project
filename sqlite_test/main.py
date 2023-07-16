# 导入SQLite驱动:
import sqlite3
# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('URL_LIB.db')
# 创建一个Cursor:
cursor = conn.cursor()
#f = open(r'text.txt', 'r',encoding='utf-8')
#f1 = open(r'texe1.txt', 'r',encoding='utf-8')
#f2 = open(r'text2.txt', 'r',encoding='utf-8')
#txt=f.readlines()
#txt1=f1.readlines()
#txt2=f2.readlines()
cursor.execute('create table urllib_com (fenlei varchar(10) primary key, big varchar(10), small varchar(10))')
cursor.execute('create table wzk_com (fenlei varchar(10) primary key, big varchar(10), small varchar(10))')
#for w in txt:
    #cursor.execute("insert into class (name) values ('{idf}')".format(idf=w))
#for w in txt1:
    #cursor.execute("insert into class (ID) values ('{idf}')".format(idf=w))
#for w in txt2:
    #cursor.execute("insert into class (des) values ('{idf}')".format(idf=w))
# 执行SQL语句，创建表:
#cursor.execute('create table url_table (url varchar(100) primary key, PID varchar(10), ID varchar(10))')
#cursor.execute('create table P_class (PID varchar(10) primary key, P_name varchar(10))')
#cursor.execute('create table class (ID varchar(10) primary key, name varchar(10), des varchar(50))')
# 继续执行SQL语句，插入记录:
#cursor.execute('insert into url_table (url, PID, ID) values (\'www.baidu1.com\', \'1\', \'1\')')
#cursor.execute('insert into P_class (PID, P_name) values (\'918\', \'P2P\')')
#cursor.execute('insert into class (ID, name, des) values (\'3\', \'P2P\', \'提供P2P资源下载、资源介绍的网站，该类网站常和一些P2P工具结合在一起，提供种子下载、搜索、发布，如迅雷、verycd等。\')')

#cursor.executescript(
""" 
    create table P_class (PID varchar(10) primary key, P_name varchar(10)); 

    insert into P_class (PID, P_name) values (\'1\', \'P2P\');
    insert into P_class (PID, P_name) values (\'2\', \'下载\');
    insert into P_class (PID, P_name) values (\'3\', \'人文\');
    insert into P_class (PID, P_name) values (\'4\', \'体育/运动\');
    insert into P_class (PID, P_name) values (\'5\', \'社会焦点\');
    insert into P_class (PID, P_name) values (\'6\', \'军事\');
    insert into P_class (PID, P_name) values (\'7\', \'社交网络\');
    insert into P_class (PID, P_name) values (\'8\', \'博彩\');
    insert into P_class (PID, P_name) values (\'9\', \'休闲\');
    insert into P_class (PID, P_name) values (\'10\', \'宗教/超自然\');
    insert into P_class (PID, P_name) values (\'11\', \'性题材\');
    insert into P_class (PID, P_name) values (\'12\', \'房产/家居\');
    insert into P_class (PID, P_name) values (\'13\', \'求职招聘\');
    insert into P_class (PID, P_name) values (\'14\', \'搜索/门户\');
    insert into P_class (PID, P_name) values (\'15\', \'政府/政治\');
    insert into P_class (PID, P_name) values (\'16\', \'教育/科学\');
    insert into P_class (PID, P_name) values (\'17\', \'新闻/媒体\');
    insert into P_class (PID, P_name) values (\'18\', \'时尚\');
    insert into P_class (PID, P_name) values (\'19\', \'交通工具\');
    insert into P_class (PID, P_name) values (\'20\', \'流媒体\');
    insert into P_class (PID, P_name) values (\'21\', \'生活\');
    insert into P_class (PID, P_name) values (\'22\', \'IT相关\');
    insert into P_class (PID, P_name) values (\'23\', \'论坛\');
    insert into P_class (PID, P_name) values (\'24\', \'购物\');
    insert into P_class (PID, P_name) values (\'25\', \'商业/经济/金融/法律\');
    insert into P_class (PID, P_name) values (\'26\', \'饮食/烟酒\');
    insert into P_class (PID, P_name) values (\'27\', \'团体组织\');
    insert into P_class (PID, P_name) values (\'28\', \'低俗/惊悚\');
    insert into P_class (PID, P_name) values (\'29\', \'黄赌毒\');
    insert into P_class (PID, P_name) values (\'30\', \'恶意网站\');
    insert into P_class (PID, P_name) values (\'31\', \'犯罪\');
    insert into P_class (PID, P_name) values (\'32\', \'空置网站\');
    insert into P_class (PID, P_name) values (\'33\', \'武器\');
    insert into P_class (PID, P_name) values (\'34\', \'欺诈\');
    insert into P_class (PID, P_name) values (\'35\', \'流产\');
    insert into P_class (PID, P_name) values (\'36\', \'自杀\');
    insert into P_class (PID, P_name) values (\'37\', \'存储服务器\');
    insert into P_class (PID, P_name) values (\'38\', \'仇恨言论\');
    insert into P_class (PID, P_name) values (\'39\', \'邪教\');
    insert into P_class (PID, P_name) values (\'40\', \'一般性站点\');
    insert into P_class (PID, P_name) values (\'41\', \'其他类\');


#cursor.executescript(

    create table class (ID varchar(10) primary key, name varchar(10), des varchar(50)) 

    insert into class (PID, P_name) values (\'1.1\', \'P2P\', \'提供P2P资源下载、资源介绍的网站，该类网站常和一些P2P工具结合在一起，提供种子下载、搜索、发布，如迅雷、verycd等。\');
    insert into class (PID, P_name) values (\'2.1\', \'电子书下载\', \'提供电子书下载以及在线阅读的网站。\');
    insert into class (PID, P_name) values (\'2.2\', \'软件下载\', \'提供各种软件资源下载的网站，对于提供一些黑客工具下载的网站也有可能被分到黑客类中。\');
    insert into class (PID, P_name) values (\'2.3\', \'图片下载\', \'提供图片资源、桌面墙纸、桌面主题等下载的网站。\');
    insert into class (PID, P_name) values (\'2.4\', \'音乐/电影下载\', \'提供各种音乐、电影下载的网站，但是涉及到在线播放的网站请参考流媒体分类。\');
    insert into class (PID, P_name) values (\'2.5\', \'其他下载\', \'提供其他类型的信息下载的网站，如铃声、彩信等。\');
    insert into class (PID, P_name) values (\'3.1\', \'历史/文化\', \'包括但不限于由博物馆、纪念馆、艺术馆等机构创办的以展示和宣扬历史、文化为主要目的的网站。\');
    insert into class (PID, P_name) values (\'3.2\', \'文学\', \'与文学相关的网站，如讨论、发表、展示诗词、散文、小说、哲学等文学作品的网站。\');
    insert into class (PID, P_name) values (\'3.3\', \'艺术\', \'与艺术相关的网站，如讨论、展示绘画、书法、雕塑等作品的网站，戏剧、舞蹈等各类表演艺术的网站。\');
    insert into class (PID, P_name) values (\'3.4\', \'音乐\', \'提供音乐信息介绍的网站，如流行歌曲、古典乐曲和乐器等的介绍网站。歌曲下载和在线播放等不属于音乐类网站。\');
    insert into class (PID, P_name) values (\'4.1\', \'竞技体育\', \'与竞技类体育活动相关的网站，如足球、篮球、拳击、垒球、游泳及极限运动等。\');
    insert into class (PID, P_name) values (\'4.2\', \'休闲运动\', \'与休闲类体育活动相关的网站，如武术、气功、钓鱼、打猎、登山、健身和野营等。\');
    insert into class (PID, P_name) values (\'4.3\', \'运动用品\', \'与体育运动（包括竞技体育和休闲运动）中所使用的工具、装备和衣物等相关的网站，如球杆、渔具、户外运动装备、野营用品和运动服装等。\');
    insert into class (PID, P_name) values (\'5.1\', \'慈善/公益\', \'与公益和慈善活动相关的网站，包括以公益和慈善为目的的组织和团体，如红十字会、希望工程等。\');
    insert into class (PID, P_name) values (\'5.2\', \'生态/发展/能源\', \'与生态、发展和能源相关的话题，如环境保护、可持续发展、节能等。\');
    insert into class (PID, P_name) values (\'5.3\', \'反恐/犯罪问题讨论\');
    insert into class (PID, P_name) values (\'5.4\', \'社会问题/生活方式\');
    insert into class (PID, P_name) values (\'5.5\', \'人权/种族问题\');
    insert into class (PID, P_name) values (\'6.1\', \'军事\', \'军事\');
    insert into class (PID, P_name) values (\'7\', \'社交网络\');
    insert into class (PID, P_name) values (\'8\', \'博彩\');
    insert into class (PID, P_name) values (\'9\', \'休闲\');
    insert into class (PID, P_name) values (\'10\', \'宗教/超自然\');
    insert into class (PID, P_name) values (\'11\', \'性题材\');
    insert into class (PID, P_name) values (\'12\', \'房产/家居\');
    insert into class (PID, P_name) values (\'13\', \'求职招聘\');
    insert into class (PID, P_name) values (\'14\', \'搜索/门户\');
    insert into class (PID, P_name) values (\'15\', \'政府/政治\');
    insert into class (PID, P_name) values (\'16\', \'教育/科学\');
    insert into class (PID, P_name) values (\'17\', \'新闻/媒体\');
    insert into class (PID, P_name) values (\'18\', \'时尚\');
    insert into class (PID, P_name) values (\'19\', \'交通工具\');
    insert into P_class (PID, P_name) values (\'20\', \'流媒体\');
    insert into P_class (PID, P_name) values (\'21\', \'生活\');
    insert into P_class (PID, P_name) values (\'22\', \'IT相关\');
    insert into P_class (PID, P_name) values (\'23\', \'论坛\');
    insert into P_class (PID, P_name) values (\'24\', \'购物\');
    insert into P_class (PID, P_name) values (\'25\', \'商业/经济/金融/法律\');
    insert into P_class (PID, P_name) values (\'26\', \'饮食/烟酒\');
    insert into P_class (PID, P_name) values (\'27\', \'团体组织\');
    insert into P_class (PID, P_name) values (\'28\', \'低俗/惊悚\');
    insert into P_class (PID, P_name) values (\'29\', \'黄赌毒\');
    insert into P_class (PID, P_name) values (\'30\', \'恶意网站\');
    insert into P_class (PID, P_name) values (\'31\', \'犯罪\');
    insert into P_class (PID, P_name) values (\'32\', \'空置网站\');
    insert into P_class (PID, P_name) values (\'33\', \'武器\');
    insert into P_class (PID, P_name) values (\'34\', \'欺诈\');
    insert into P_class (PID, P_name) values (\'35\', \'流产\');
    insert into P_class (PID, P_name) values (\'36\', \'自杀\');
    insert into P_class (PID, P_name) values (\'37\', \'存储服务器\');
    insert into P_class (PID, P_name) values (\'38\', \'仇恨言论\');
    insert into P_class (PID, P_name) values (\'39\', \'邪教\');
    insert into P_class (PID, P_name) values (\'40\', \'一般性站点\');
    insert into P_class (PID, P_name) values (\'41\', \'其他类\');
"""

# 通过rowcount获得插入的行数:
print(cursor.rowcount)


# 关闭Cursor:
cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection:
conn.close()
#f.close()
#f1.close()
#f2.close()
