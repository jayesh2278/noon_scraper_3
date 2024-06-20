import scrapy
import datetime
import os
import shutil
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class NoonScraperSpider(CrawlSpider):
    name = 'noon_uae'
    allowed_domains = ['www.noon.com']
    start_urls = ['https://www.noon.com/uae-en/']
    uae_dir = "UAE"
    
    rules = [
        Rule(LinkExtractor(), callback= "parse_data", follow=True),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if os.path.exists(self.uae_dir):
            shutil.rmtree(self.uae_dir)
        os.mkdir(self.uae_dir)
        

    def parse_data(self, response):
        if "/p/?o=" in response.url:
            new_link = (response.url).replace("https://www.noon.com/uae-en/", "")
            url = "https://www.noon.com/_svc/catalog/api/v3/u/"+new_link   
            
            headers = {
                'if-none-match': 'W/"4bd0-wsGTpbHjvMDXy10iNo24v4gj/iw"',
                }
            yield scrapy.Request(
                url=url,
                headers=headers,
                callback=self.get_product_info,
            )   

    def get_product_info(self, response):
        today = datetime.datetime.now()
        today = today.strftime("%d-%m-%Y %H:%M:%S.%f")
        product = response.json()
        product['datetime'] = today
        yield {
            "product": product
        }
