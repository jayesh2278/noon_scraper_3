# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import datetime
import json
import pandas as pd
import pytz

class RewardforjusticPipeline:
    def open_spider(self,spider):
        now = datetime.datetime.now()
        dt_string = now.strftime("%Y%m%d_%H%M%S")

        self.json_file = open(f'RWJST_{dt_string}.json', 'w')
        self.json_export = []

        self.xlsx_file = f'RWJST_{dt_string}.xlsx'
        self.xlsx_export = []

        pass

    def process_item(self, item, spider):

        self.json_export.append(dict(item))
        self.xlsx_export.append({

        'Page_url' : item['Page_url'],
        'Title' :item['Title'],
        'Reward_amount':item['Reward_amount'],
        'image_urls':item['image_urls'],
        'date_of_birth' : item['date_of_birth'],
        'associated_organisation': item['associated_organisation'],
        'associated_location':item['associated_location'],
        'about' :item['about']

        })

        return item

    def close_spider(self, spider):
        # Write the JSON file
        json.dump(self.json_export, self.json_file)
        self.json_file.close()

        # Write the XLSX file
        df = pd.DataFrame(self.xlsx_export)
        df.to_excel(self.xlsx_file, index=False)