# coding:utf-8
from baike_spider import url_manager, html_downloader, html_parser, html_outputer

class SpiderMain(object):

    #构造函数：
    def __init__(self):
        self.urls = url_manager.UrlManager()               #url管理
        self.downloader = html_downloader.HtmlDownloader() #下载器
        self.parser = html_parser.HtmlParser()             #解析器
        self.outputer = html_outputer.HtmlOutputer()       #输出管理
        
    def craw(self, root_url):
        
        count = 1
        
        self.urls.add_new_url(root_url) #添加url
        
        # 启动url爬虫
        while self.urls.has_new_url():
            
            try:
                new_url = self.urls.get_new_url()
                
                print count
                
                html_cont = self.downloader.download(new_url)   #下载url页面
                new_urls, new_data = self.parser.parse(new_url, html_cont)  #解析获得新的url列表和数据,new_url为当前爬取的url，html_cont为下载好的数据
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                
                count = count + 1
                
                if count == 10:
                    break
            
            except:
                print "craw failed"
            
        self.outputer.output_html()   #输出数据


if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)  #初始化