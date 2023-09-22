import scrapy

class LinkSpider(scrapy.Spider):
    name = "link"
    # No need for start_requests for as this is the default anyway
    start_urls = ["https://www.climatefiles.com/collection-index/"]  

    def parse(self, response):
        for j in response.xpath('//a'):

            title_to_save = j.xpath('./text()').get()
            href_to_save= j.xpath('./@href').get()

            print("test")
            print(title_to_save)
            print(href_to_save)

            yield {'title': title_to_save}
