# -*- coding: utf-8 -*-
import scrapy

class TopCrackPagesSpider(scrapy.Spider):
    name = 'top-crack-pages'
    allowed_domains = ['crackapk.com/']

    with open('top-crack-pages.txt', 'rt') as f:
        start_urls = [url.strip() for url in f.readlines()]

    custom_settings = {
        'FEED_FORMAT' : 'csv',
        'FEED_URI' : 'top-crack-apps.csv'
    }

    def parse(self, response):
        titles = response.css('div.base_info div.info_box h1.d_app_title::text').extract()
        dates = response.css('div.base_info div.info_box p.icon_box span.icon_time::text').extract()
        downloads = response.css('div.base_info div.info_box p.icon_box span.icon_donwloads::text').extract()

        for item in zip(titles,dates,downloads):
            scraped_info = {
                'title' : item[0],
                'date_uploaded' : item[1],
                'download_count' : item[2]
            }
            yield scraped_info
