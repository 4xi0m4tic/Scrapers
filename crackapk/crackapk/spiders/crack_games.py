# -*- coding: utf-8 -*-
import scrapy


class CrackGamesSpider(scrapy.Spider):
    name = 'crack-games'
    allowed_domains = ['crackapk.com/crack-games']
    start_urls = ['http://crackapk.com/crack-games/']
    custom_settings = {
        'FEED_FORMAT' : 'csv',
        'FEED_URI' : 'crack-games.csv'
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
