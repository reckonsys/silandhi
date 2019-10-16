import scrapy

MAKE_URL = 'https://www.faa.gov/regulations_policies/airworthiness_directives/views/modelsByMake.cfm'  # noqa: E501


class FooBar(scrapy.Spider):
    name = "foo_bar"
    start_urls = [
        'https://www.faa.gov/regulations_policies/airworthiness_directives/'
    ]

    def parse_model(self, model):
        pass

    def parse_make(self, make):
        return make.get()
        # url = MAKE_URL + make.attrib['href']
        # __import__('ipdb').set_trace()
        # scrapy.Request(make.urljoin(url), self.parse_model)

    def parse(self, response):
        makes = [self.parse_make(make) for make in response.css('.make.makeAnchor a')]  # noqa: E501
        return makes
