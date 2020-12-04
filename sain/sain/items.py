# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field


class job(scrapy.Item):
    nameProduk = Field()
    harga = Field()
    stok = Field()
    url = Field()
    rating = Field()
    urlImage=Field()
    
def close_spider(self, spider):
    self.cursor.close()
    self.conn.close()