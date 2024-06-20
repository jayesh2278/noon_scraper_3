# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RewardforjusticItem(scrapy.Item):
    
    name = scrapy.Field()
    Page_url = scrapy.Field()
    Title = scrapy.Field()
    Reward_amount = scrapy.Field()
    image_urls = scrapy.Field()
    date_of_birth = scrapy.Field()
    associated_organisation = scrapy.Field()
    associated_location= scrapy.Field()
    about = scrapy.Field()
    
