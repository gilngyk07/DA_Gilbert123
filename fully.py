import scrapy
from scrapy.crawler import CrawlerProcess

class spd(scrapy.Spider):
    name = 'mys'
    urls = ['http://172.17.50.43/varsity']

process = CrawlerProcess(settings= {
    'Feed_FORMAT':'json',
    'FEED_URL':'file.json'

})
process.crawl(spd)
process.start()

