import scrapy
import json
from fake_useragent import UserAgent
import sys
from sain.items import job

class LazSpider(scrapy.Spider):
    name = 'laz'
    allowed_domains = ['www.lazada.co.id']
    ua = UserAgent()
    def start_requests(self):
        yield scrapy.Request(url=f'https://www.lazada.co.id/beli-aksesori-komputer/?spm=a2o4j.searchlist.cate_2.2.4ba61279E9oiZ7&ajax=true&?=',
        callback=self.parse,
        headers={
        'User-Agent' : self.ua.random,
        'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-encoding' : 'gzip, deflate, br',
        'accept-language' : 'en-US,en;q=0.9',
        'cookie' : 'lzd_cid=46f4d2e8-4c75-4298-858b-8fbd063ddbc4; t_uid=46f4d2e8-4c75-4298-858b-8fbd063ddbc4; hng=ID|id|IDR|360; userLanguageML=id; t_fv=1603778567945; t_sid=kws4m6Cn4wcpnnaUxRcmFZ6BCwdIj2R7; utm_channel=NA; lzd_sid=1c39c5e96f1f8e013d9a48f70963e93f; _m_h5_tk=72e34639400771b06c7153249b2e7513_1603787927466; _m_h5_tk_enc=b177f96adfc34584c0e84deb0fe4d8d4; cna=B6YeGJoZqEMCAbTytNZbHwqp; _tb_token_=588b35fee60e1; _bl_uid=gkkbwgmbr0UkvRcvhn063nmubb6R; _fbp=fb.2.1603778568814.1137794401; xlly_s=1; JSESSIONID=C016CE69D54C9D2CBF02EF2637A50ADF; _uetsid=0a2e00f0181a11ebac65c7ca5c3eaa18; _uetvid=0a2e6020181a11ebb03b0ba03e9cc39b; _ga=GA1.3.783319687.1603778678; _gid=GA1.3.924348641.1603778678; _gat_UA-29801013-1=1; cto_bundle=ry8Qw19SNCUyQkszRk0lMkJFSVh3aWZsejR1YnVPamh0cmpnc2NPbUt4cGY4NEIzbjRha1NBcE91SkR0SVY4WlFEMGNwWW5GeEJ0SDl2Rm5EbUo2TENDZUxSRU1EdU1sQUhxQXpJb2gwSmlLWW1pYVJ5OGJMVVR1UTNvellKSjNtaVB4UWhXanlTYXRUV01DMnRjZlA4Q3lJd1o4TkJRJTNEJTNE; tfstk=cKccBoDdPxybfewodINjJmoUt0pRZVX4cflxabuMaw5KFxhPi56PL75kru8grO1..; l=eBgW3FMlOAea6QVDBOfwourza77OSIRAguPzaNbMiOCPOUfp5RGdWZWoxFY9C3MNh6J9R3RYU61yBeYBqC0XQ2RUnGz_4ukmn; isg=BA4O1wR93e6stWnK0M81S7jfX-TQj9KJWcXsGDhWg5HWm6_1oB4LmQ5B1d_3g8qh'
        },
        dont_filter=True
        )

    def parse(self, response):
        data = json.loads(response.body)
        
        try:
            for item in data.get('mods').get('listItems'):
                yield {
                'nameProduk' : item.get('name'),
                'harga' : item.get('price'),
                'stok'  : "",
                'url' : item.get('productUrl'),
                'rating' : item.get('ratingScore'),
                'urlImage' : item.get('image'),
                }
               
        except TypeError:
            print("NO PAGE LEFT TO SCRAPE")
            sys.exit(0)
        except AttributeError:
            # print("You are blocked on page number :",self.page)
            print("Press control + C to STOP or else continue.")
            print("Hint : uncomment PROXY_POOL and PROXY Download Middleware in settings.py")
        # self.page = self.page + 1
        yield scrapy.Request(url=f'https://www.lazada.co.id/beli-aksesori-komputer/?spm=a2o4j.searchlist.cate_2.2.4ba61279E9oiZ7&ajax=true&?=',
        callback=self.parse,
        headers={
        'User-Agent' : self.ua.random,
        'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-encoding' : 'gzip, deflate, br',
        'accept-language' : 'en-US,en;q=0.9',
        'cookie' : 'lzd_cid=46f4d2e8-4c75-4298-858b-8fbd063ddbc4; t_uid=46f4d2e8-4c75-4298-858b-8fbd063ddbc4; hng=ID|id|IDR|360; userLanguageML=id; t_fv=1603778567945; t_sid=kws4m6Cn4wcpnnaUxRcmFZ6BCwdIj2R7; utm_channel=NA; lzd_sid=1c39c5e96f1f8e013d9a48f70963e93f; _m_h5_tk=72e34639400771b06c7153249b2e7513_1603787927466; _m_h5_tk_enc=b177f96adfc34584c0e84deb0fe4d8d4; cna=B6YeGJoZqEMCAbTytNZbHwqp; _tb_token_=588b35fee60e1; _bl_uid=gkkbwgmbr0UkvRcvhn063nmubb6R; _fbp=fb.2.1603778568814.1137794401; xlly_s=1; JSESSIONID=C016CE69D54C9D2CBF02EF2637A50ADF; _uetsid=0a2e00f0181a11ebac65c7ca5c3eaa18; _uetvid=0a2e6020181a11ebb03b0ba03e9cc39b; _ga=GA1.3.783319687.1603778678; _gid=GA1.3.924348641.1603778678; _gat_UA-29801013-1=1; cto_bundle=ry8Qw19SNCUyQkszRk0lMkJFSVh3aWZsejR1YnVPamh0cmpnc2NPbUt4cGY4NEIzbjRha1NBcE91SkR0SVY4WlFEMGNwWW5GeEJ0SDl2Rm5EbUo2TENDZUxSRU1EdU1sQUhxQXpJb2gwSmlLWW1pYVJ5OGJMVVR1UTNvellKSjNtaVB4UWhXanlTYXRUV01DMnRjZlA4Q3lJd1o4TkJRJTNEJTNE; tfstk=cKccBoDdPxybfewodINjJmoUt0pRZVX4cflxabuMaw5KFxhPi56PL75kru8grO1..; l=eBgW3FMlOAea6QVDBOfwourza77OSIRAguPzaNbMiOCPOUfp5RGdWZWoxFY9C3MNh6J9R3RYU61yBeYBqC0XQ2RUnGz_4ukmn; isg=BA4O1wR93e6stWnK0M81S7jfX-TQj9KJWcXsGDhWg5HWm6_1oB4LmQ5B1d_3g8qh'
        },
        dont_filter=True
        )
