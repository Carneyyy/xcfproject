# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
scrapy.Request
# CrawlSpider:继承自spider,可以定制规则，从页面源码中提取目标地址,
# 内部会自动构建Request请求对象，交给调度器，最终交给下载器执行下载任务

# 1.地址url的提取规则
# 2.设置回调的解析函数
#  - 拦截提取到的url地址
#  - 拦截Request请求对象



class XcftwoSpider(CrawlSpider):
    #爬虫名称
    name = 'xcftwo'
    #设置允爬取的域
    allowed_domains = ['xiachufang.com']
    #设置起始url地址
    start_urls = ['http://www.xiachufang.com/category/']

    #rules：列表或元组，存放的是Rule对象
       #  Rule：
       #   link_extractor, 是一个对象，定义链接的提取规则和提取范围,符合
       #   规则的url地址会被提取出来,并且scrapy会自动发起请求
       #   callback = None, 回调函数,设置任务下载完成后的回调
       #   follow = None, 是否跟进
       #   process_links = None, 设置函数,拦截提取到的url地址
       #   process_request = identity,设置函数,拦截Request请求对象

       # link_extractor
       #   allow = (), 元组或列表,定义正则规则，提取url地址，发起请求
       #   deny = (), 元组或列表,定义正则规则，提取url地址,提取的url地址一定不会请求
       #   allow_domains = (),#元组或列表,设置允爬取的域
       #   deny_domains = (), #元组或列表,设置不允爬取的域
       #   restrict_xpaths = () #根据xpath路径，确定提取链接的模块（范围）
       #   restrict_css=()


    rules = (
        #定义规则，提取分类的url地址
        #http://www.xiachufang.com/category/20167/
        Rule(
            LinkExtractor(
                allow=r'.*?/category/\d+/$',
                restrict_xpaths='//div[@class="block-bg p40 font16"]'
            ),
           # callback='parse_item',
            process_links= 'get_links',
            process_request= 'get_request',

            follow=True,
        ),
        #提取分类列表页中的菜谱详情url地址
        #http://www.xiachufang.com/recipe/100232976/
        #http://www.xiachufang.com/recipe/102228399/
        Rule(
            LinkExtractor(
                allow=r'.*?/recipe/\d+/$',
            ),
            callback='parse_caipu_detail',
            follow=True
        ),
        # 提取分类中下一页的url地址
        # http://www.xiachufang.com/category/52411/?page=3
        Rule(
            LinkExtractor(
                allow=r'.*?category/\d+/?page=\d+'
            ),
            follow=True
        )
    )

    def get_links(self,links):
        #可以在这里拦截links，提取到的url地址
        # print(links)
        for link in links:
            link.url = link.url + '#adlasbkasbv'
        #print(links)
        return links

    def get_request(self,request):
        #可以在这过滤Request对象
        print(type(request))
        print(request.url)
        if '3094' in request.url:
            return request

    def parse_start_url(self, response):
        """在这个函数中可以获取起始任务的响应结果"""
        pass


    def parse_item(self, response):
        print(response.status)
        print(response.url)

    def parse_caipu_detail(self,response):
        print(response.request.headers)
        print('菜谱详情请求',response.status)
        print(response.url)
        #解析菜谱详情数据



