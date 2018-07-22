import scrapy
import requests

from example.items import ExampleItem

class ExamplespiderSpider(scrapy.Spider):
    name = 'examplespider'
    allowed_domains = ['www.yahoo.co.jp']
    start_urls = ['http://www.yahoo.co.jp/']

    def parse(self, response):
        #print(response.css('div.imageArea.js-none > div.container > img::attr(src)').extract_first())
        imageUrl = response.css('div.imageArea.js-none > div.container > img::attr(src)').extract_first()
        print(imageUrl)
        
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
        timeout = 1
        res = requests.get(imageUrl, timeout=timeout, headers=headers)
        print('&&&&&&&&&&&')
        print(res.status_code)
        print('&&&&&&&&&&&')
        
        imageUrl = 'https://ic4-a.example.net/mi/gr/115/neroinc.xsrv.jp/ama/parrot/main/tk382/tk-1891009_8.jpg'
        res = requests.get(imageUrl, timeout=timeout, headers=headers)
        print('&&&&&&&&&&&')
        print(res.status_code)
        print('&&&&&&&&&&&')

