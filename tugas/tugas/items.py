from typing import NoReturn
import scrapy
from scrapy.item import Field

class Job(scrapy.Item):
    nameProduk = Field()
    harga = Field()
    stok = Field()
    url = Field()
    rating = Field()
    urlImage=Field()

def close_spider(self, spider):
    self.cursor.close()
    self.conn.close()