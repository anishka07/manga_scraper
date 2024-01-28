# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MangaItem(scrapy.Item):
    # define the fields for your item here like:
    manga_title = scrapy.Field()
    manga_price = scrapy.Field()
    manga_imageurl = scrapy.Field()
