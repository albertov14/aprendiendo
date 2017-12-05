#AQUI LE DECIMOS AL SPIDER DE DONDE TIENE QUE "COGER" LAS COSAS

import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from aprendiendo.items import AprendiendoItem




class Aprendiendo(CrawlSpider):
	name = "aprendiendo"
	item_count = 0 
	allowed_domain = ['https://www.degustam.com'] 
	start_urls = ("https://www.degustam.com/366-especial-navidad.html",) 

	
	rules = {
	 Rule(LinkExtractor(allow = (), restrict_xpaths = ('//div[@class="next"]/a'))),
	 Rule(LinkExtractor(allow =(), restrict_xpaths = ('//h5/a')),
	 	  callback = 'parse_item', follow = False),




	}

	def parse_item(self, response):
		ml_item = AprendiendoItem()

		
		ml_item['titulo'] = response.xpath ('//h1[@class="col-xs-12 page-title product-name"]/text()').extract()
		ml_item['descripcion'] = response.xpath ('//p/text()').extract()
		ml_item['precio'] = response.xpath ('//span[@itemprop="price"]/text()').extract()
		ml_item['image_urls'] = response.xpath ('//figure[contains(@class, "col-sm-4 col-xs-12 product-img2")]/a/img/@src').extract()
		ml_item['image_name'] = response.xpath ('//h1[@class="col-xs-12 page-title product-name"]/text()').extract_first()
		
		self.item_count += 1
		if self.item_count > 5:
			raise CloseSpider('item_exceeded')
		yield ml_item