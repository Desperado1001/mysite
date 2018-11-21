import scrapy

class XxooSpider(scrapy.Spider):
    name = "Aoisora"
    def start_requests(self):
        urls = [
            'http://lab.scrapyd.cn/page/1',
            'http://lab.scrapyd.cn/page/2'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response): #重构Spider中的parse方法
        page = response.url.split("/")[-2]
        filename = 'Aoisora-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)#下载页面
            #print(response.body)
        self.log('保存文件：%s' % filename)