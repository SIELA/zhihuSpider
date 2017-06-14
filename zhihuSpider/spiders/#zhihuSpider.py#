
# -*- coding: utf-8 -*-
import scrapy
import cookielib
from scrapy.selector import Selector
from bs4 import BeautifulSoup
import re
import datetime
import json
from scrapy.exceptions import IgnoreRequest


class ZhihuspiderSpider(scrapy.Spider):
    name = 'zhihuSpider'
    apiurl = 'http://api.ip.data5u.com/dynamic/get.html?order=efed1c976c7b0f2bbf5b5301bc726329&sep=3'
    start_url = 'https://www.zhihu.com/people/xu-jing-85-20/following'
    uid = start_url.split('/')[4]

    def start_requests(self):
        req = scrapy.Request(self.start_url,
                        meta={'cookiejar': 1},
                        cookies = {'q_c1':'afa8370f46f94446b7df38714f6cc9d9|1496218821000|1496218821000','l_n_c':'1','r_cap_id':'"MTMwZGY1MzkyNTIwNDAzMTg2MDI4OTAyYmJkZTk1ODQ=|1496801988|88f8872ab1da1bfb41c0a9372b1a9304e2d4f75b"','cap_id':'"MmYxN2EyNjNhYjlkNGJmMGI5MGZkODA4ZDVmOGJlZjI=|1496801988|983b93c147e7e7004279e5ee2e88de2c28adb03e"',' l_cap_id':'"YWVmN2Q5NmI4NDI0NGYyN2IzNWViMmY4OGQ1ZGRmNDg=|1496801988|6c0ecfdaa10529838f038e55917dc83846ee1f97"','_xsrf':'b1859bc987c204b2cd208e7df65ed372','d_c0':'"AJDCjZYq4AuPToa-kxb9kV9b_8Ht-LNZ5ls=|1496802110"','_zap':'3d4de19e-031f-4adf-9164-efcebb534d06','n_c':'1','__utma':'51854390.150453406.1496802087.1496802087.1496802087.1','__utmc':'51854390','__utmz':'51854390.1496802087.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/explore','__utmv':'51854390.100--|2=registration_date=20151109=1^3=entry_date=20151109=1'},
                        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0' }
                             
        )
        yield req
        
            
    def parse(self, response):
        selector = Selector(response)
        uid = selector.xpath('//*[@id="root"]//a[@class="Tabs-link"]/@href').extract_first().split('/')[2]
        data = selector.xpath('//div[@id="data" and @data-state]/@data-state').extract_first()
        data = json.loads(data)
        data = data['entities']['users'][uid]
        
        yield {
            'uid' : uid,
            'gender' : data['gender'],         # 性别
            'name' : data['name'],     # 昵称
            'educations' : '&&'.join(map( (lambda x:'%s%s%s'%( (x['school']['name'] if x.has_key('school') else '') , (',' if x.has_key('school') and x.has_key('major') else '') ,  (x['major']['name'] if x.has_key('major') else ''))),data['educations'])).strip().replace("'","\\'"),     # 教育经历
            'followingCount' : data['followingCount'],     # 他关注的人数
            'pinsCount' : data['pinsCount'],     # 他的分享数
            'favoriteCount' : data['favoriteCount'],     # 他的收藏数
            'voteupCount' : data['voteupCount'],       # 他获得的赞同数
            'followingColumnsCount' : data['followingColumnsCount'], # 关注的专栏个数
            'headline' : data['headline'].replace("'","\\'"),     # 一句话描述 brief
            'participatedLiveCount' : data['participatedLiveCount'], # 赞助过的live
            'followingFavlistsCount' : data['followingFavlistsCount'], # 关注的收藏夹
            'favoritedCount' : data['favoritedCount'],  # 获得多少次收藏
            'followerCount' : data['followerCount'],   # 关注他的人数
            'employments' : '&&'.join(map( (lambda x:'%s%s%s'%( (x['company']['name'] if x.has_key('company') else '') , (',' if x.has_key('company') and x.has_key('job') else '') , (x['job']['name'] if x.has_key('job') else ''))),data['employments'])).strip().replace("'","\\'"),
            'markedAnswersCount' : data['markedAnswersCount'],     # 知乎收录了多少个回答
            'avatarUrlTemplate' : data['avatarUrlTemplate'].replace('{size}','xl'),   # 头像临时链接
            'followingTopicCount' : data['followingTopicCount'],   # 关注的话题数量
            'description' : data['description'].replace("'","\\'"),       # 个人简介
            'business' : hasattr(data, 'business') and data['business']['name'].replace("'","\\'") or '',     # 所在行业
            'hostedLiveCount' : data['hostedLiveCount'],   # 主持的live数量
            'answerCount' : data['answerCount'],   # 回答的数量
            'articlesCount' : data['articlesCount'],   # 发表的文章数量
            'questionCount' : data['questionCount'],   # 提了多少个问题
            'locations' : '&&'.join(map(lambda x:x['name'] ,data['locations'])).strip().replace("'","\\'"),
            'logsCount' : data['logsCount'],   # 参与过多少次公共编辑
            'followingQuestionCount' : data['followingQuestionCount'],     # 关注的问题数量
            'thankedCount' : data['thankedCount'],     # 收到的感谢数量
            'now' : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")     #  当前时间
        }

        next_page_url = selector.xpath('//div[@id="Profile-following"]//a[@class="UserLink-link"]/@href').extract()
        if next_page_url is not None:
            for next_url in next_page_url:
                req = scrapy.Request(response.urljoin(next_url+'/following'), meta={'cookiejar': response.meta['cookiejar']},headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0' })
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
