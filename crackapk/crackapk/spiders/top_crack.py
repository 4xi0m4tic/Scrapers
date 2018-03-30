# -*- coding: utf-8 -*-
import scrapy

class TopCrackSpider(scrapy.Spider):
    name = 'top-crack'
    allowed_domains = ['crackapk.com/top-crack']
    start_urls = ['http://crackapk.com/top-crack/']
    custom_settings = {
        'FEED_FORMAT' : 'csv',
        'FEED_URI' : 'top-crack.csv'
    }

    def parse(self, response):
        titles = response.css('li.unique_item span.tit a::attr(title)').extract()
        links = response.css('li.unique_item a.l::attr(href)').extract()
        downloads = response.css('li.unique_item span.s_btn a::attr(href)').extract()

        for item in zip(titles,links,downloads):
            scraped_info = {
                'title' : item[0],
                'link' : item[1],
                'download' : item[2]
            }
            yield scraped_info
