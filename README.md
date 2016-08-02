# 百科爬虫


## 简介

+ 爬取百度百科关于python相关的100条网页

+ 解析抓取的结果生成html文件保存到本地



## 爬虫模块

|模块名称|说明|python模块|
|:-:|:-:|:-:|
|spider_main|爬虫主函数|无|
|url_manager|url链接调度器|无|
|html_downloader|网页下载器|urllib2|
|html_parser|网页解析器|urlparser, re, BeautifulSoup|
|html_outputer|结果输出器|无|





## 函数说明



### spider_main

+ craw(self, root_url)：初始化爬虫并启动抓取，传入第一个url(root_url=http://baike.baidu.com/view/21087.htm)

### url_manager

+ add_new_url(self, url)：向url库中添加带抓取的新的url

+ add_new_urls(self, urls)：批量添加url

+ has_new_url(self)：判断url库中是否还包含url

+ get_new_url(self)：从url库中拿出一条url用于抓取，并放入抓取后的url库

### html_downloader

+ download(self, url)：urllib2打开网页并读取

### html_parser

+ _get_new_urls(self, page_url, soup)：通过正则匹配寻找新的url

+ _get_new_data(self, page_url, soup)：解析网页数据，将“summary”内容提取出来。

+ parse(self, page_url, html_cont)：利用上面两个函数对抓取的一个网页进行处理进行处理

### html_outputer

+ collect_data(self, data)：将新的数据加入到数据集中

+ output_html(self)：生成html网页。



## 生成截图

![](https://github.com/MilkCoffeeSugar/baike_spider/blob/master/baike_spider_1.png)
