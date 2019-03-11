import requests
import headers as hea
from lxml import etree
import os
import json
from urllib import request
import time

class King_glory(object):
    def __init__(self):
        self.headers=hea.headers
        with open("E:\Python\LOL_skin\王者荣耀.csv","a")as f:
            f.write("英雄id"+","+"英雄名称"+","+"默认皮肤名称"+","+"皮肤名称"+"\n")

    #获取英雄的详细信息
    def get_content(self):
        #统计皮肤的数量
        skin_number=0
        #用读的方式打开herolist.json文本
        with open("herolist.json","r",encoding="UTF-8") as f:
            content_str=f.read()
            #因为文本中包含BOM字符,会报错,所以这个判断,是去掉BOM字符
            if content_str.startswith(u'\ufeff'):
                content_str = content_str.encode('utf8')[3:].decode('utf8')
        #解码json数据
        content_dict=json.loads(content_str)
        #遍历content_dict
        for i in content_dict:
            #用|分割字符串
            skin_name=i['skin_name'].split("|")
            #调用保存函数，将数据保存下来
            #self.save_content(i['ename'],i['cname'],i['title'],i['skin_name'])
            #调用下载函数
            self.download_skin(i['ename'],i['cname'],skin_name)
            #累加皮肤数量
            skin_number+=len(skin_name)
            print(i['ename'],i['cname'],i['title'])
            time.sleep(1)
        print("一共有%d个英雄！"%len(content_dict))
        print("一共有%d个皮肤！"%skin_number)

    #将英雄信息用csv格式保存下来
    def save_content(self,ename,cname,title,skin_name):
        with open("E:\Python\LOL_skin\王者荣耀.csv","a")as f:
            #","是表示换列
            f.write(str(ename)+","+cname+","+title+","+skin_name)
            f.write("\n")
        print("写入成功！")

    #下载皮肤
    def download_skin(self,ename,cname,skin_name):
        #目录名称
        directory_name="E:\Python\LOL_skin\王者荣耀皮肤/"+cname
        #判断目录是否存在，不存在则新建
        if not os.path.exists(directory_name):
            print("{0}目录不存在，新建{0}目录！".format(cname))
            os.mkdir(directory_name)
        for i in range(len(skin_name)):
            #拼接皮肤图片的url
            url="https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{0}/{0}-bigskin-{1}.jpg".format(ename,i+1)
            #皮肤图片的名称
            img_name=directory_name+"\\"+skin_name[i]+".jpg"
            #下载皮肤图片
            request.urlretrieve(url,img_name)
            print(skin_name[i],"保存成功！")
            
if __name__=="__main__":
    K=King_glory()
    K.get_content()
