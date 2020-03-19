# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArinItem(scrapy.Item):
    judul = Field()
    isi = Field()
    tanggal = Field()
    link = Field()
    
    

    

