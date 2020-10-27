from scrapy import Request
from tugas.items import Job
import scrapy

class bhinnekaSpider(scrapy.Spider):
    
    name = "bhinneka"
    allowed_domains = []
    start_urls = ['https://bisnis.bhinneka.com/aksesoris-gadget-komputer/3415416' ]

    
    def parse(self,response):  
             for la in response.css('a.row::attr(href)').extract():
                    yield (scrapy.Request(response.urljoin(la),self.parse_link) )                  
            
            
             next_page = response.css('li.page a::attr(href)').get()
             if next_page is not None:
                yield scrapy.Request(
                 response.urljoin("https://bisnis.bhinneka.com/aksesoris-gadget-komputer/3415416"+next_page),
                 callback=self.parse
                 )        
           
                    
    def parse_link(self, response):
            item = Job()
            item['nameProduk'] = response.css('h1.bt-pd-content__title::text').extract()
            item['harga'] = response.css('h3::text').extract()
            item['stok'] = ""
            item['url'] = response.url
            item['rating'] = "" 
            item['urlImage'] = response.css('img.slick-big::attr(src)').extract()[1]
            # response.url

            return item
           
            
       

           