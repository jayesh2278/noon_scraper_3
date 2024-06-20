import scrapy
import json
from lxml import etree
from datetime import datetime
from ..items import RewardforjusticItem

class SnameSpider(scrapy.Spider):
    name = "SName"
    allowed_domains = ['rewardsforjustice.net']
    
    def start_requests(self):
        url = 'https://rewardsforjustice.net/wp-admin/admin-ajax.php'
        headers = {
        'authority': 'rewardsforjustice.net',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-IN,en-US;q=0.9,en;q=0.8,gu;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': 'wp-wpml_current_language=en; _ga=GA1.1.1937575707.1677692480; _ga_BPR2J8V0QK=GS1.1.1677748794.4.1.1677750996.0.0.0',
        'dnt': '1',
        'origin': 'https://rewardsforjustice.net',
        'referer': 'https://rewardsforjustice.net/index/?jsf=jet-engine:rewards-grid&tax=crime-category:1070%2C1071%2C1073%2C1072%2C1074&pagenum=1',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
        }

        cookies = {
            "wp-wpml_current_language": "en",
            "_ga": "GA1.1.1937575707.1677692480",
            "_ga_BPR2J8V0QK": "GS1.1.1677748794.4.1.1677751230.0.0.0"
        }
        body = "action=jet_smart_filters&provider=jet-engine%2Frewards-grid&query%5B_tax_query_crime-category%5D%5B%5D=1070&query%5B_tax_query_crime-category%5D%5B%5D=1071&query%5B_tax_query_crime-category%5D%5B%5D=1073&query%5B_tax_query_crime-category%5D%5B%5D=1072&query%5B_tax_query_crime-category%5D%5B%5D=1074&defaults%5Bpost_status%5D%5B%5D=publish&defaults%5Bpost_type%5D%5B%5D=north-korea&defaults%5Bpost_type%5D%5B%5D=rewards&defaults%5Bposts_per_page%5D=250&defaults%5Bpaged%5D=1&defaults%5Bignore_sticky_posts%5D=1&settings%5Blisitng_id%5D=22078&settings%5Bcolumns%5D=3&settings%5Bcolumns_tablet%5D=1&settings%5Bcolumns_mobile%5D=1&settings%5Bpost_status%5D%5B%5D=publish&settings%5Buse_random_posts_num%5D=&settings%5Bposts_num%5D=9&settings%5Bmax_posts_num%5D=&settings%5Bnot_found_message%5D=No+data+was+found&settings%5Bis_masonry%5D=&settings%5Bequal_columns_height%5D=&settings%5Buse_load_more%5D=&settings%5Bload_more_id%5D=&settings%5Bload_more_type%5D=click&settings%5Bloader_text%5D=&settings%5Bloader_spinner%5D=&settings%5Buse_custom_post_types%5D=yes&settings%5Bcustom_post_types%5D%5B%5D=north-korea&settings%5Bcustom_post_types%5D%5B%5D=rewards&settings%5Bhide_widget_if%5D=&settings%5Bcarousel_enabled%5D=&settings%5Bslides_to_scroll%5D=3&settings%5Barrows%5D=true&settings%5Barrow_icon%5D=fa+fa-angle-left&settings%5Bdots%5D=&settings%5Bautoplay%5D=&settings%5Bautoplay_speed%5D=5000&settings%5Binfinite%5D=&settings%5Bcenter_mode%5D=&settings%5Beffect%5D=slide&settings%5Bspeed%5D=500&settings%5Binject_alternative_items%5D=&settings%5Binjection_items%5D%5B0%5D%5Bitem%5D=90086&settings%5Binjection_items%5D%5B0%5D%5B_id%5D=a4c8515&settings%5Binjection_items%5D%5B0%5D%5Bitem_num%5D=1&settings%5Binjection_items%5D%5B0%5D%5Binject_once%5D=yes&settings%5Binjection_items%5D%5B0%5D%5Bmeta_key%5D=dprk&settings%5Binjection_items%5D%5B0%5D%5Bitem_condition_type%5D=item_meta&settings%5Binjection_items%5D%5B0%5D%5Bstatic_item%5D=yes&settings%5Bscroll_slider_enabled%5D=&settings%5Bscroll_slider_on%5D%5B%5D=desktop&settings%5Bscroll_slider_on%5D%5B%5D=tablet&settings%5Bscroll_slider_on%5D%5B%5D=mobile&settings%5Bcustom_query%5D=&settings%5Bcustom_query_id%5D=&settings%5B_element_id%5D=rewards-grid&settings%5Bjet_cct_query%5D=&settings%5Bjet_rest_query%5D=&props%5Bfound_posts%5D=180&props%5Bmax_num_pages%5D=25&props%5Bpage%5D=1&paged=1&referrer%5Buri%5D=%2Findex%2F%3Fjsf%3Djet-engine%3Arewards-grid%26tax%3Dcrime-category%3A1070%252C1071%252C1073%252C1072%252C1074&referrer%5Binfo%5D=&referrer%5Bself%5D=%2Findex.php&indexing_filters=%5B41852%2C41851%5D"
        yield scrapy.Request(url=url,
                            method='POST',
                            dont_filter=True,
                            cookies=cookies,
                            headers=headers,
                            body=body,
                            )

    def parse(self, response):
        data = json.loads(response.text)
        all_data = data['content']
        root = etree.fromstring(all_data)
        urls =  root.xpath('//@href')
        for url in urls:
            yield scrapy.Request(url = url,callback=self.parse_detail,meta={'url':url})

    def parse_detail(self,response):
        item = RewardforjusticItem()

        Page_url = response.meta.get('url')
        Title = response.xpath('.//title/text()').get()
        Reward_amount = response.xpath('.//div[@data-id="5e60756"]//h2/text()').get()
        about = response.xpath('.//div[@data-id="52b1d20"]//p/text()').getall()
        about = ','.join(about)
        image_url = response.xpath('.//div[@data-id="a819a24"]//img/@src').getall()
        image_urls = ','.join(image_url)

        date_of_birth = response.xpath('.//div[@data-id="9a896ea"]/div/text()').get()
        try:
            date_of_birth = datetime.strptime(date_of_birth, "%B %d, %Y").date()
            date_of_birth = date_of_birth.date().isoformat()
        except:
            pass

        as_org = response.xpath('.//div[@data-id="095ca34"]//p[contains(text(), "Associated Organization")]')
        if as_org:
            associated_organisation = response.xpath('.//div[@data-id="095ca34"]//a/text()').get()
        else:
            associated_organisation = None

        associated_location = response.xpath('.//div[@data-id="0fa6be9"]//span/text()').getall()
        associated_location = (' '.join(associated_location))


        item['Page_url']= Page_url
        item['Title']=Title
        item['Reward_amount']= Reward_amount
        item['image_urls']=image_urls
        item['date_of_birth']=date_of_birth
        item['associated_organisation']= associated_organisation
        item['associated_location']= associated_location
        item['about']=about

        yield item
        