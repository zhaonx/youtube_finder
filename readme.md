## 本项目的目的是收集youtube平台上所有潜在的local youtuber

### 其方式有如下三种：

​	1.通过yelp网站中的餐厅，酒吧等地点的名字作为关键词搜索

​	2.通过tripadvisor中的推荐地点作为关键词搜索

​	3.通过城市内的具体的街道名字作为关键词搜索

### 整体的执行流程如下：

​	1.通过代码手机到yelp，tripadvisor和街道的名字，收集程序分别为yelp_.py tripadvisor.py,街道名的手机与爬取为单独的一个文件夹 selenium_street

​	2.对于yelp和tripadvisor的地名，通过spider文件夹中的using_video爬虫完成youtuber candidate的收集并将其保存至mongo中的user中，对于街道名则通过selenium_street保存到selenium_street。再通过duplicate.py 将其user和selenium_street去重并保存到candidate中

​	3.通过spider文件中的handle_collect爬虫进行删选并保存到final_user中

​	4.通过to_excel.py将final_user中的数据输出为excel格式



### 具体代码中的设置：

爬虫的启动在start.py文件中，通过修改爬虫名字来启动不同的爬虫

spider文件中的的地名需要手动更改

```
url = f'https://www.youtube.com/results?search_query=new+york++{item}&sp=EgIIBQ%253D%253D'
```

这里的new york根据需要换成其他城市



mongo中代表时间的字段时ts和date，暂时需要在代码里手动修改

如handle_collect中的

```
for doc in self.candidate.find({"date":616}):
```

和duplicate中的

```
doc1['date'] = 616
```



duplicate中需要手动切换需要去重的数据库

```
user_handler = db.selenium_street
# user_handler = db.user
```

 pipeline中也需要手动切换，文件中有注释