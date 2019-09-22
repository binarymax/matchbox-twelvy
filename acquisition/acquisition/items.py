import scrapy

class AcquisitionItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()