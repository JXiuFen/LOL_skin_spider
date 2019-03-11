import requests
import headers as hea
from lxml import etree
from urllib import request
import re
import json
import os
import time 

class LOL(object):
    def __init__(self):
        self.headers=hea.headers
        #获取英雄详情url
        self.get_figure_url="https://lol.qq.com/biz/hero/champion.js"
        #获取英雄皮肤id的url
        self.get_skin_url="https://lol.qq.com/biz/hero/"
        #获取英雄皮肤下载的url
        self.get_imge_url="https://ossweb-img.qq.com/images/lol/web201310/skin/big"
        #建一个csv格式文本
        with open("E:\Python\LOL_skin\LOL英雄.csv","w") as f:
            f.write("英文名字"+","+"ID"+","+"中文名字"+","+"称号"+"\n")

    #获取英雄详情
    def figure_url(self):
        response=requests.get(self.get_figure_url,headers=self.headers).text
        #英雄id
        re_id=re.findall('"id":"(.+?)"',response,re.S)
        #英雄key
        re_key=re.findall('"key":"(.+?)"',response,re.S)
        #英雄name
        re_name=re.findall('"name":"(.+?)",',response,re.S)
        #英雄title
        re_title=re.findall('"title":"(.+?)",',response,re.S)
        for id,key,name,title in zip(re_id,re_key,re_name,re_title):
            
            #拼接英雄皮肤的url
            url=self.get_skin_url+id+".js"
            print("当前是：{}，url：{}".format(id,url))
            self.skin_url(url)
            time.sleep(2)
           # self.save_content(id,key,name.encode('latin-1').decode('unicode_escape'),title.encode('latin-1').decode('unicode_escape'))
            #print("正在保存中...")
           # print(id,key,name.encode('latin-1').decode('unicode_escape'),title.encode('latin-1').decode('unicode_escape'))

    #获取皮肤链接
    def skin_url(self,url):
        response=requests.get(url,headers=self.headers).text
        #获取皮肤的id
        re_id=re.findall(',.*?{"id":"(.+?)","num"',response,re.S)
        #获取皮肤的name
        re_name=re.findall('"name":"(.+?)"',response,re.S)
        #删除默认皮肤名称
        del (re_name[1])
        #遍历id，name
        for id,name in zip(re_id,re_name):
            #将一些不能作为文件名称的符号给替换掉
            name=re.sub(r'[？\\*|“”<>:/]', '',name.encode('latin-1').decode('unicode_escape'))
            #拼接皮肤图片下载的url
            imge_url=self.get_imge_url+id+".jpg"
            print(id,name)
            #调用下载皮肤方法
            self.download_img(imge_url,re_name[0].encode('latin-1').decode('unicode_escape'),name)

    #下载皮肤
    def download_img(self,url,dir_name,fi_name):
        #每个英雄建一个目录
        directory_name="E:\Python\LOL_skin\LOL皮肤/"+dir_name
        #判断目录是否存在，不存在便新建
        if not os.path.exists(directory_name):
            print("{0}目录不存在，新建{0}目录！".format(dir_name))
            os.mkdir(directory_name)
        #将每张图片用英雄每款皮肤的名字
        file_name=directory_name+"\\"+fi_name+".jpg"
        #下载图片
        request.urlretrieve(url,file_name)
        print("下载成功！")

    #将每个英雄的信息，用csv格式保存
    def save_content(self,id,key,name,title):
        with open("E:\Python\LOL_skin\LOL英雄.csv","a") as f:
            f.write(id+","+key+","+name+","+title+"\n")

if __name__=='__main__':
    l=LOL()
    l.figure_url()



    #request.urlretrieve(img,'images/'+filename),.encode('latin-1').decode('unicode_escape')
##    l.download_img("lol","皮肤")