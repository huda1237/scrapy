import pymysql
from tugas import settings
import logging
 
class TutorialPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host = settings.MYSQL_HOST,
            db = settings.MYSQL_DBNAME,
            user = settings.MYSQL_USER,
            passwd = settings.MYSQL_PASSWD,
            charset = 'utf8',
            use_unicode = True
        )
        self.cursor = self.connect.cursor();
 
    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                "insert into screaping (nameProduk, harga, stok, url,rating, urlImage) value(%s, %s, %s,%s, %s, %s) on duplicate key update url=(url)",
                ( 
                item['nameProduk'],
                item['harga'] ,
                item['stok'] ,
                item['url'] ,
                item['rating'],
                item['urlImage'] ,
                 ))
            self.connect.commit()
        except Exception as error:
            logging.log(error)
        return item
 
    def close_spider(self, spider):
        self.connect.close();

   