import scrapy


class DocsSpider(scrapy.Spider):
    name = "docs"
    allowed_domains = ["www.climatefiles.com"]
    start_urls = ["https://www.climatefiles.com/collection-index"]

    def parse(self, response):
        for j in response.xpath('//a'):

            title_to_save = j.xpath('./text()').get()
            href_to_save= j.xpath('./@href').get()

            print("test")
            print(title_to_save)
            print(href_to_save)

            yield {'title': title_to_save}
