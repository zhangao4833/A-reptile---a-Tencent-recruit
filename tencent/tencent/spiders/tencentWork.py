# -*- coding: utf-8 -*-
import scrapy


class TencentworkSpider(scrapy.Spider):
    name = 'tencentWork'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    def parse(self, response):
        tbodys = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        for tbody in tbodys:
            yield {
                    'woekName': tbody.xpath('./td[1]/a/text()').extract_first(),
                    'workCgs' : tbody.xpath('./td[2]/text()').extract_first(),
                    'workPeople': tbody.xpath('./td[3]/text()').extract_first(),
                    'workLocation': tbody.xpath('./td[4]/text()').extract_first(),
                    'workTime': tbody.xpath('./td[5]/text()').extract_first(),
            }
        if len(response.xpath("//a[@id='next' and @class='noactive']")) == 0:
            url = response.xpath("//a[@id='next']/@href").extract_first()
            yield response.follow("https://hr.tencent.com/"+url,self.parse)

