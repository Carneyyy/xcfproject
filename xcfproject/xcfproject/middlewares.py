# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

#SpiderMiddleware 爬虫中间件
class XcfprojectSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


#DownloaderMiddleware下载中间件
class XcfprojectDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        #所有的请求（request）都会经过这个方法（可以在这里统一对request对象进行处理）
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called

        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


import random
class UserAgentDownloaderMiddleware(object):

    def process_request(self, request, spider):
        print('经过了UserAgentDownloaderMiddleware')
        user_agents = spider.settings['USER_AGENTS']
        random_ua = random.choice(user_agents)

        if random_ua:
            request.headers['User-Agent'] = random_ua
            request.headers.setdefault(b'User-Agent', random_ua)
#
# from fake_useragent import UserAgent
# class UserAgentDownloaderMiddleware(object):
#
#     def __init__(self):
#         self.ua = UserAgent()
#
#     def process_request(self, request, spider):
#         print('经过了UserAgentDownloaderMiddleware')
#         random_ua = self.ua.random
#
#         if random_ua:
#             request.headers['User-Agent'] = random_ua
#             request.headers.setdefault(b'User-Agent', random_ua)


#自定义代理的中间件
import random
import base64
class ProxyDownloaderMiddleware(object):

    def process_request(self, request, spider):
        proxies = spider.settings['PROXIES']
        proxy = random.choice(proxies)

        if proxy:
            if proxy['user_pwd']:
                #私密代理
                user_pwd = base64.b64encode(proxy['user_pwd'].encode('utf-8')).decode('utf-8')
                # 对应到代理服务器的信令格式里
                request.headers['Proxy-Authorization'] = 'Basic ' + user_pwd
                request.meta['proxy'] = proxy['ip_port']
            else:
                #公开普通代理
                request.meta['proxy'] = proxy['ip_port']


# cookies中间件
class CookiesDownloaderMiddleware(object):

    def process_request(self, request, spider):
        cookies = spider.settings['COOKIES']
        cookie = random.choice(cookies)
        #bid=1oiYJsrz
        cookie_dict = {cookie_str.split('=')[0]:cookie_str.split('=')[1] for cookie_str in cookie.split('; ')}
        print(cookie_dict)
        if cookie_dict:
            request.cookies = cookie_dict

#selenium下载中间件
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from scrapy.http import HtmlResponse
class SeleniumDownloaderMiddleware(object):

    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path='/Users/ljh/Desktop/driver/chromedriver'
        )
        self.driver.set_page_load_timeout(10)

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        #监控爬虫结束的信号量
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        return s

    def process_request(self, request, spider):
        url = request.url
        try:
            self.driver.get(url)
            html = self.driver.page_source
        except TimeoutException as err:
            print(err)
            html = None

        if html:
            response = HtmlResponse(url, status=200, headers=None,
                                     body=html.encode('utf-8')
                                     , request=request
                                     )
            return response
        else:
            response = HtmlResponse(url, status=500, headers=None,
                                    body=b'',request=request
                                    )
            return response
    def spider_closed(self,spider):
        #爬虫结束，退出
        self.driver.quit()