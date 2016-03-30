import requests
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
import json
from indeed.items import *
import scrapy


JOB_TITLE_XPATH = '//div[@id="job_header"]/b[@class="jobtitle"]//text()'
COMPANY_XPATH = '//div[@id="job_header"]/span[@class="company"]//text()'
LOCATION_XPATH = '//div[@id="job_header"]/span[@class="location"]//text()'
SUMMARY_XPATH = '//span[@class="summary"]//text()'

class IndeedSpider(scrapy.Spider):
    name = "indeedspider"
    allowed_domains = ["indeed.co.in"]
    response_data = requests.get('http://api.indeed.com/ads/apisearch?publisher=6818688261501036&q=BigData%20OR%20Hadoop%20OR%20Analytics%20OR%20Hortenworks%20OR%20cloudera%20OR%20SPARK&+tx&sort=date&radius=&st=&jt=&start=20&limit=&fromage=&filter=&latlong=1&chnl=&userip=1.2.3.4&co=in&useragent=Mozilla/%2F4.0%28Firefox%29&v=2&format=json')
    content = response_data.content
    data = json.loads(content)
    results = data['results']
    start_urls = [item['url'] for item in results]

    def parse(self,response):
        job_title = response.xpath(JOB_TITLE_XPATH).extract()
        company = response.xpath(COMPANY_XPATH).extract()
        location = response.xpath(LOCATION_XPATH).extract()
        skill_set = response.xpath(SUMMARY_XPATH).extract()[1]
        url = response.url
        item = IndeedItem()
        item['job_title'] = job_title
        item['company'] = company
        item['location'] = location 
        item['skill_set'] = skill_set 
        item['url'] = url
        yield item




