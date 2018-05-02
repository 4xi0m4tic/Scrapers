# -*- coding: utf-8 -*-
import scrapy

class AppItem(scrapy.Item):
    app_title = scrapy.Field()
    page_link = scrapy.Field()
    download_link = scrapy.Field()
    upload_date = scrapy.Field()
    downloads = scrapy.Field()

class CrackAppsSpider(scrapy.Spider):
    name = 'crack-apps'
    # CrackAPK applications are found on:
    # crackapk.com/app-name links.
    allowed_domains = ['crackapk.com']
    start_urls = ['http://crackapk.com/crack-apps/']
    custom_settings = {
        'FEED_FORMAT' : 'csv',
        'FEED_URI' : 'crackapk_crack-apps.csv'
    }

    def parse(self, response):
        # Info page url.
        url = response.css('li.unique_item a.l::attr(href)').extract()
        # Download button url.
        down = response.css('li.unique_item span.s_btn a::attr(href)').extract()

        for i in range(len(url)):
            yield scrapy.Request(url[i], callback = self.parse_app_page, meta={'d_l':down[i]})

    def parse_app_page(self, response):
        item = AppItem()

        item['page_link'] = response.url
        item['download_link'] = response.meta['d_l']
        item['app_title'] = response.css('div.base_info div.info_box h1.d_app_title::text').extract()
        item['upload_date'] = response.css('div.base_info div.info_box p.icon_box span.icon_time::text').extract()
        item['downloads'] = response.css('div.base_info div.info_box p.icon_box span.icon_donwloads::text').extract()

        return item