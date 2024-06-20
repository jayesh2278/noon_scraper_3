import scrapy
import datetime
import os
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class NoonAeSpider(CrawlSpider):
    name = 'noon_saudi'
    allowed_domains = ['www.noon.com']
    start_urls = ['https://www.noon.com/saudi-en/']
    uae_dir = "SAUDI"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if os.path.exists(self.uae_dir):
            pass
        else:
            os.mkdir(self.uae_dir)

    rules = [
        Rule(LinkExtractor(), callback= "parse_data", follow=True),
    ]

    def parse_data(self, response):
        if ("/p/?o=" in response.url) and ("https-imgur-com-undefined" not in response.url) and ('https://www.noon.com/saudi-en/' in response.url):
            new_link = (response.url).replace("https://www.noon.com/saudi-en/", "")
            url = "https://www.noon.com/_svc/catalog/api/v3/u/"+new_link   
            meta={'proxy': 'dc.smartproxy.com:10000'},

            headers={
                'x-locale': 'en-sa',
                }
            
            yield scrapy.Request(
                url=url,
                headers=headers,
                meta=meta,
                callback=self.get_product_info,
            )

    def get_product_info(self, response):
        today = datetime.datetime.now()
        today = today.strftime("%b-%d-%Y %H:%M:%S")
        product = response.json()
        product['datetime'] = today
        yield {
            "product": product
        }