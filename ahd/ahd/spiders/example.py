import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"

    def start_requests(self):
        url = "https://www.ahd.com/free_profile.php?hcfa_id=4fe1e6446c78aaeecf74439cc72e3c66&ek=6a0c46345954fc54b8336d0a163b385a"
        
        Cookie =  {'PHPSESSID':"3ck7tpbsbksrm3j328mvnhfq41"}
            
        
        yield scrapy.Request(url,cookies=Cookie,callback=self.parse_deatil)

        
    def parse_deatil(self,response):
        print(response)
    