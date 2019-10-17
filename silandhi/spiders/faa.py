from scrapy import Spider  # , Request
from silandhi.items.faa import Model, Directive

MAKE_URL = 'https://www.faa.gov/regulations_policies/airworthiness_directives/views/modelsByMake.cfm'  # noqa: E501
MODEL_URL = 'https://www.faa.gov/regulations_policies/airworthiness_directives/views/directivesByModel.cfm'  # noqa: E501


class FAA(Spider):
    name = "faa"
    start_urls = [
        'https://www.faa.gov/regulations_policies/airworthiness_directives/',
    ]

    def parse_model(self, response):
        directives = []
        for tr in response.css('tbody tr'):
            data = tr.css('td')
            directives.append(Directive(
                published_date=data[0].css('::text').get().strip(),
                ad_link=data[1].css('a').attrib['href'],
                ad_number=data[1].css('a::text').get(),
                effective_date=data[2].css('::text').get().strip(),
                subject=data[3].css('::text').get().strip(),
            ))
        yield Model(
            caption=response.css('caption::text').get(),
            directives=directives
        )

    def parse_make(self, response):  # , make):
        for model in response.css('a'):
            url = MODEL_URL + model.attrib['href']
            yield response.follow(url, self.parse_model)

    def parse(self, response):
        for make in response.css('.make.makeAnchor a')[:1]:
            url = MAKE_URL + make.attrib['href']
            yield response.follow(url, self.parse_make)
