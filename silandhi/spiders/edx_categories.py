import scrapy


class EdxCategoriesSpider(scrapy.Spider):
    name = "edx_categories"
    start_urls = [
        'https://www.edx.org/subjects'
    ]

    def parse(self, response):
        for sc in response.css('.subject-card'):
            yield {
                'text': sc.css('.subject-title::text').get()
            }
