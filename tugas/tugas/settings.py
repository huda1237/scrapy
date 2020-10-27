BOT_NAME = 'tugas'

SPIDER_MODULES = ['tugas.spiders']
NEWSPIDER_MODULE = 'tugas.spiders'

COOKIES_ENABLED = False


ITEM_PIPELINES = {
    'tugas.pipelines.TutorialPipeline':300
}
 
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'tester'
MYSQL_USER = 'root'
MYSQL_PASSWD = ''
MYSQL_PORT = 3306

DOWNLOAD_DELAY = 20


ROBOTSTXT_OBEY = True

