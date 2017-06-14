# -*- coding: utf-8 -*-
import scrapy
import cookielib
from scrapy.selector import Selector
from bs4 import BeautifulSoup
import re
import datetime
import json
from scrapy.exceptions import IgnoreRequest
from ..items import ZhihuspiderItem


class ZhihuquestionSpider(scrapy.Spider):
    name = 'zhihuQuestion'
    num = 10000000
    url = 'https://www.zhihu.com/question/'
    start_url = url+str(num)

    def start_requests(self):
        req = scrapy.Request(self.start_url, meta={'cookiejar':1})
        yield req
            
    def parse(self, response):
        if response.status == 404:
            yield None
        selector = Selector(response)
        urlToken = selector.xpath('//span[@class="UserLink AuthorInfo-avatarWrapper"]//a[@class="UserLink-link"]/@href').re(r'/people/(.*)')
        ##
#        fh = open(str(self.num)+'.txt','w')
#        fh.write(response.body)
#        fh.close()
        ##
        for u in urlToken:
            item = ZhihuspiderItem()
            item['urlToken'] = u
            yield item
        self.num+=1
        next_page_url = self.url+str(self.num)
        if self.num <= 99999999:
            req = scrapy.Request(response.urljoin(next_page_url))
            yield req
            
class ZhihuBanDetectionPolicy(object):
    """ Zhihu ban detection rules. """
    NOT_BAN_STATUSES = {200, 301}
    NOT_BAN_EXCEPTIONS = (IgnoreRequest,)
    def response_is_ban(self, request, response):
        if response.status == 302:
            return True
        return False

    def exception_is_ban(self, request, exception):
        return not isinstance(exception, self.NOT_BAN_EXCEPTIONS)
