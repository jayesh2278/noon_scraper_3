import scrapy


class Example2Spider(scrapy.Spider):
    name = "example2"
    
    start_urls = ["https://www.ahd.com/free_profile.php?hcfa_id=4fe1e6446c78aaeecf74439cc72e3c66&ek=6a0c46345954fc54b8336d0a163b385a"]

    def parse(self, response):
        print(response.text)
