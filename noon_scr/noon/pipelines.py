import json
import zipfile
from datetime import datetime

class NoonPipeline:
    def open_spider(self, spider):
        if spider.name == "noon_uae":
            self.ZIP_DIR = "UAE"
        if  spider.name == "noon_saudi":
            self.ZIP_DIR = "SAUDI"
        if  spider.name == "noon_egypt":
            self.ZIP_DIR = "EGYPT"               
        # tnow = datetime.now()
        # self.today = tnow.strftime("%b-%d-%Y-T-%H-%M-%S")


        self.counter = 1
        self.zipfile_name = f"{self.ZIP_DIR}/{self.ZIP_DIR}_{self.counter}_{datetime.now().strftime('%b-%d-%Y-T-%H-%M-%S')}.zip"
        self.products_list = []
        pass
        

    def process_item(self, item, spider):
        self.products_list.append(
            item.get("product")
        )
        if len(self.products_list)==3:
            # create zip file here
            self.zipfile_name = f"{self.ZIP_DIR}/{self.ZIP_DIR}_{self.counter}_{datetime.now().strftime('%b-%d-%Y-T-%H-%M-%S')}.zip"
            json_name = f"{self.ZIP_DIR}_{self.counter}_{datetime.now().strftime('%b-%d-%Y-T-%H-%M-%S')}.json"
            json_string = json.dumps(self.products_list)
            self.add_to_zip(
                self.zipfile_name, json_name, json_string
            )
            self.products_list = []
            self.counter += 1
        return item

    def close_spider(self, spider):
        if len(self.products_list) > 0:
            self.zipfile_name = f"{self.ZIP_DIR}/{self.ZIP_DIR}_{self.counter}_{datetime.now().strftime('%b-%d-%Y-T-%H-%M-%S')}.zip"
            json_name = f"{self.ZIP_DIR}_{self.counter}_{datetime.now().strftime('%b-%d-%Y-T-%H-%M-%S')}.json"
            json_string = json.dumps(self.products_list)
            self.add_to_zip(
                self.zipfile_name, json_name, json_string
            )
        pass
    
    @staticmethod
    def add_to_zip(zip_name, json_name, json_string):
        zip_file = zipfile.ZipFile(
            zip_name, 
            "w",
            compression=zipfile.ZIP_DEFLATED, 
            compresslevel=9
            )
        zip_file.writestr(
            json_name,
            json_string
        )
        zip_file.close()
        