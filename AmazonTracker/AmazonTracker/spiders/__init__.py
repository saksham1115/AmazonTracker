from scrapy.spider import BaseSpider
from scrapy.shell import inspect_response
from AmazonTracker.items import AmazonTrackerItem

class AmazontrackerSpider(BaseSpider):
    name = "amazing"
    allowed_domains = ["amazon.in"]
    start_urls = [
        "http://www.amazon.in/Philips-Trimmer-Cordless-QT4006-15/dp/B00T7EMMGA/ref=sr_1_11?s=hpc&ie=UTF8&qid=1497301408&sr=1-11&keywords=trimmer"
    ]
    def parse(self, response):
        item = AmazonTrackerItem()
        price = response.xpath('//*[@id="priceblock_ourprice"]/text()').extract_first()
        item["price"] = price
        return item
