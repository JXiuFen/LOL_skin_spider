# 英雄联盟、王者荣耀、所有英雄的皮肤爬取
<li>项目需求：获取所有英雄的每一款皮肤并且以一个英雄的名称为目录存放这个英雄的所有皮肤图片，还有将英雄的一些信息用csv格式保存一下！
<br><li>项目分析：
        <br>分析一：首先我们分析网页，发现每个英雄的都对应一个ID号，而这个ID号正是，我们获取皮肤的关键所在。
        
  ![url](https://github.com/JXiuFen/LOL_skin_spider/blob/master/URL%E5%88%86%E6%9E%90.png?raw=true)
        
   <br>分析二：接着发现，每个英雄和皮肤都是以异步加载的形式显示出来的，然后我便采用抓包的形式来分析，发现在一个champion.js文件中，存放着所有英雄的信息。
   ![id](https://github.com/JXiuFen/LOL_skin_spider/blob/master/%E5%88%86%E6%9E%90%E4%B8%80.png?raw=true)    
  <br>分析三：通过分析皮肤的URL，发现每一款皮肤都有特定的序号，我接着抓包分析，发现（英雄ID.js）这个文件中，存放着英雄皮肤的序号。
  ![分析](https://github.com/JXiuFen/LOL_skin_spider/blob/master/%E5%88%86%E6%9E%90%E4%BA%8C.png?raw=true)
  ![皮肤序号](https://github.com/JXiuFen/LOL_skin_spider/blob/master/%E7%9A%AE%E8%82%A4URL%E5%88%86%E6%9E%90.png?raw=true)
  
  <br>分析四：拼接皮肤图片的url，将皮肤图片下载到指定目录。
  ![皮肤url](https://github.com/JXiuFen/LOL_skin_spider/blob/master/%E5%88%86%E6%9E%90%E4%B8%89.png?raw=true)
  
  <br>分析五：以英雄名称为目录名，目录下存放该英雄的所有皮肤。
  ![运行中](https://github.com/JXiuFen/LOL_skin_spider/blob/master/%E8%BF%90%E8%A1%8C%E4%B8%AD.png?raw=true)
  <br>分析六：将英雄信息以csv格式保存
<br><li>项目实施：<br>第一步：获取英雄ID<br>第二步：获取皮肤序号<br>第三：拼接皮肤图片url<br>第四步：保存图片到指定目录
<br><li>项目成果：
        
  ![成果](https://github.com/JXiuFen/LOL_skin_spider/blob/master/%E6%88%90%E6%9E%9C.png?raw=true)


