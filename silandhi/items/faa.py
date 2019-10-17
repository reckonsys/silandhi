from scrapy import Item, Field


class Make(Item):
    pass


class Model(Item):
    caption = Field()
    directives = Field()


class Directive(Item):
    published_date = Field()
    ad_link = Field()
    ad_number = Field()
    effective_date = Field()
    subject = Field()
