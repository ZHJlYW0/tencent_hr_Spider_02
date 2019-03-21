# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from json import dump, dumps


class TencentHrSpider02Pipeline(object):
    def process_item(self, item, spider):
        # # 方法1
        # dump(dict(item), self.file, ensure_ascii=False)
        # self.file.write(",\n")

        # 方法2
        content = dumps(dict(item), ensure_ascii=False) + ",\n"
        self.file.write(content.encode("utf-8"))

        return item

    def open_spider(self, spider):
        # # 方法1
        # self.file = open("tencent_hr.json", "w")

        # 方法2
        self.file = open("tencent_hr.json", "wb")

    def close_spider(self, spider):
        self.file.close()
