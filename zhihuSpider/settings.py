# -*- coding: utf-8 -*-

# Scrapy settings for stack project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihuSpider'

SPIDER_MODULES = ['zhihuSpider.spiders']
NEWSPIDER_MODULE = 'zhihuSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'stack.middlewares.StackSpiderMiddleware': 543,
#}


# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'stack.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'zhihuSpider.pipelines.MongoDBPipeline':300
}
MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'zhihu'
MONGODB_COLLECTION = 'user'

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


#失败后重试次数


RETRY_TIMES = 3
#重试的错误码
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 408]
HTTPERROR_ALLOWED_CODES = [404]
DOWNLOADER_MIDDLEWARES = {
    'zhihuSpider.middlewares.ZhihuspiderSpiderMiddleware':543
#    'scrapy.downloadermiddlewares.retry.RetryMiddleware':90,
#    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware':110,
#    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
#    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
#'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware' :130,
#    'zhihuSpider.middlewares.UAPOOLS':140
}




'''
def load_lines(path):
    with open(path, 'rb') as f:
        return [line.strip() for line in
                f.read().decode('utf8').splitlines()
                if line.strip()]

ROTATING_PROXY_LIST = load_lines('ip_pool.txt')
ROTATING_PROXY_BACKOFF_BASE = 999


ROTATING_PROXY_BAN_POLICY = 'zhihuSpider.spiders.zhihuSpider.ZhihuBanDetectionPolicy'
ROTATING_PROXY_PAGE_RETRY_TIMES = 999
'''

import os
os.environ["DISPLAY"] = ":0" 
