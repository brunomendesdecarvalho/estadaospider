# -*- coding: utf-8 -*-
import scrapy


class EstadaoSpider(scrapy.Spider):

    name = 'estadao'
    start_urls = ['https://www.estadao.com.br//']

    custom_settings = {
        'DOWNLOAD_DELAY': 1.5 ,
        'DEPTH_LIMIT': 8 ,
    }

    def parse(self, response):
        manchetes = list(response.xpath(".//figcaption[@class='title']/a/text()").extract())
        links = list(response.xpath(".//figcaption[@class='title']/a/@href").extract())

        for manchete, link in zip(manchetes, links):
            yield {
                'Manchete': manchete ,
                'Link': link ,
            }
