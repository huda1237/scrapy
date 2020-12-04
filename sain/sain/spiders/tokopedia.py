from sain.items import job
import scrapy

class tokpetSpider(scrapy.Spider):
    
    name = "tokped"
    start_urls = ['https://www.tokopedia.com/p/komputer-laptop/aksesoris-komputer-laptop' ]

    
    def parse(self,response):  
        for la in response.css('div.css-bk6tzz a::attr(href)').extract():
           yield (scrapy.Request(response.urljoin(la),self.parse_link) )                  
            
            
                  
           
                    
    def parse_link(self, response):
            item = job()
            item['nameProduk'] = response.css('h1.css-x7lc0h::text').extract()
            item['harga'] = response.css('h3.css-c820vl::text').get().replace("Rp","").replace(".","")
            item['stok'] = ""
            item['url'] = response.url
            item['rating'] = response.css('span.css-4g6ai3 > span::text').extract()[0] 
            item['urlImage'] = response.css('img.success.fade::attr(src)').extract()

            return item
           
            
       

           