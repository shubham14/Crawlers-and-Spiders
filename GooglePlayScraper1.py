import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from urlparse import urljoin
import csv



class CompItem(scrapy.Item):
    rating = scrapy.Field()
    data = scrapy.Field()
    name = scrapy.Field()
    date = scrapy.Field()
    #review_content=scrapy.Field()



class criticspider(CrawlSpider):
    name = "gaana"
    allowed_domains = ["play.google.com"]
    start_urls = ["https://play.google.com/store/apps/details?id=com.gaana&hl=en"]
    # rules = (
        # Rule(
            # SgmlLinkExtractor(allow=('search=jabong&page=1/+',)),
            # callback="parse_start_url",
            # follow=True),
    # )

    def parse(self, response):
        sites = response.xpath('//div[@class="single-review"]')
        items = []

        for site in sites:
            item = CompItem()
            item['data'] = site.xpath('.//div[@class="review-text"]/text()').extract()
            item['name'] = site.xpath('.//div/div/span[@class="author-name"]/a/text()').extract()[0]
            item['date'] = site.xpath('.//span[@class="review-date"]/text()').extract()[0]
            item['rating'] = site.xpath('.//div[@class="tiny-star star-rating-non-editable-container"]/@aria-label/text()').extract()
            #item['review_content']=site.xpath('//div[@class="review-body with-review-wrapper"]/text()').extract()
            

            items.append(item)
        return items


