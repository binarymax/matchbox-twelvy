# -*- coding: utf-8 -*-

# Scrapy settings for acquisition project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'acquisition'

SPIDER_MODULES = ['acquisition.spiders']
NEWSPIDER_MODULE = 'acquisition.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'scrapy.pipelines.images.ImagesPipeline': 1,
}

IMAGES_STORE = "/home/max/apps/matchbox-twelvy/raw-images"
