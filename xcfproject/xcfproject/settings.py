# -*- coding: utf-8 -*-

# Scrapy settings for xcfproject project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'xcfproject'

SPIDER_MODULES = ['xcfproject.spiders']
NEWSPIDER_MODULE = 'xcfproject.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'xcfproject (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED默认为True,False:不携带cookies
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  # 'Accept-Language': 'en',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'xcfproject.middlewares.XcfprojectSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'xcfproject.middlewares.XcfprojectDownloaderMiddleware': 543,
    'xcfproject.middlewares.UserAgentDownloaderMiddleware':543,
    # 'xcfproject.middlewares.ProxyDownloaderMiddleware':544,
    'xcfproject.middlewares.CookiesDownloaderMiddleware':544,
    'xcfproject.middlewares.SeleniumDownloaderMiddleware':545,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'xcfproject.pipelines.XcfprojectPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


USER_AGENTS = [
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
]


# 在settings.py文件中模拟一个代理池(对于少量代理可以这么做)
PROXIES = [
    {'ip_port': '111.8.60.9:8123', 'user_pwd': 'user1:pass1'},
    {'ip_port': '101.71.27.120:80', 'user_pwd': 'user2:pass2'},
    {'ip_port': '122.96.59.104:80', 'user_pwd': None},
    {'ip_port': '122.224.249.122:8088', 'user_pwd': None},
]


# 在settings.py文件中模拟一个cookies池(对于少量cookies可以这么做)
COOKIES = [
    'bid=1oiYJsrz; gr_user_id=f43f4e27-0106-4a98-8599-13a6606636b9; __utmc=177678124; BAIDU_SSP_lcr=https://www.baidu.com/link?url=nOPS2P4kK0PMeJakN_exJvKcEVqhvf987LaoMoAUGEyQ8LQYceTt7m-FkjXqVGej&wd=&eqid=92339229000514a7000000025d01fab0; Hm_lvt_ecd4feb5c351cc02583045a5813b5142=1560387930,1560410804; Hm_lpvt_ecd4feb5c351cc02583045a5813b5142=1560410804; gr_session_id_8187ff886f0929da=8df39e19-4f45-45d4-9dc9-97e24e967308; __utma=177678124.1209598612.1560387930.1560390200.1560410804.3; __utmz=177678124.1560410804.3.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=177678124.1.10.1560410804; gr_session_id_8187ff886f0929da_8df39e19-4f45-45d4-9dc9-97e24e967308=true',
    'bid=1oiYJsrz; gr_user_id=f43f4e27-0106-4a98-8599-13a6606636b9; __utmc=177678124; BAIDU_SSP_lcr=https://www.baidu.com/link?url=nOPS2P4kK0PMeJakN_exJvKcEVqhvf987LaoMoAUGEyQ8LQYceTt7m-FkjXqVGej&wd=&eqid=92339229000514a7000000025d01fab0; Hm_lvt_ecd4feb5c351cc02583045a5813b5142=1560387930,1560410804; Hm_lpvt_ecd4feb5c351cc02583045a5813b5142=1560410804; gr_session_id_8187ff886f0929da=8df39e19-4f45-45d4-9dc9-97e24e967308; __utma=177678124.1209598612.1560387930.1560390200.1560410804.3; __utmz=177678124.1560410804.3.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=177678124.1.10.1560410804; gr_session_id_8187ff886f0929da_8df39e19-4f45-45d4-9dc9-97e24e967308=true',
    'bid=1oiYJsrz; gr_user_id=f43f4e27-0106-4a98-8599-13a6606636b9; __utmc=177678124; BAIDU_SSP_lcr=https://www.baidu.com/link?url=nOPS2P4kK0PMeJakN_exJvKcEVqhvf987LaoMoAUGEyQ8LQYceTt7m-FkjXqVGej&wd=&eqid=92339229000514a7000000025d01fab0; Hm_lvt_ecd4feb5c351cc02583045a5813b5142=1560387930,1560410804; Hm_lpvt_ecd4feb5c351cc02583045a5813b5142=1560410804; gr_session_id_8187ff886f0929da=8df39e19-4f45-45d4-9dc9-97e24e967308; __utma=177678124.1209598612.1560387930.1560390200.1560410804.3; __utmz=177678124.1560410804.3.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=177678124.1.10.1560410804; gr_session_id_8187ff886f0929da_8df39e19-4f45-45d4-9dc9-97e24e967308=true',
    'bid=1oiYJsrz; gr_user_id=f43f4e27-0106-4a98-8599-13a6606636b9; __utmc=177678124; BAIDU_SSP_lcr=https://www.baidu.com/link?url=nOPS2P4kK0PMeJakN_exJvKcEVqhvf987LaoMoAUGEyQ8LQYceTt7m-FkjXqVGej&wd=&eqid=92339229000514a7000000025d01fab0; Hm_lvt_ecd4feb5c351cc02583045a5813b5142=1560387930,1560410804; Hm_lpvt_ecd4feb5c351cc02583045a5813b5142=1560410804; gr_session_id_8187ff886f0929da=8df39e19-4f45-45d4-9dc9-97e24e967308; __utma=177678124.1209598612.1560387930.1560390200.1560410804.3; __utmz=177678124.1560410804.3.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=177678124.1.10.1560410804; gr_session_id_8187ff886f0929da_8df39e19-4f45-45d4-9dc9-97e24e967308=true',
    'bid=1oiYJsrz; gr_user_id=f43f4e27-0106-4a98-8599-13a6606636b9; __utmc=177678124; BAIDU_SSP_lcr=https://www.baidu.com/link?url=nOPS2P4kK0PMeJakN_exJvKcEVqhvf987LaoMoAUGEyQ8LQYceTt7m-FkjXqVGej&wd=&eqid=92339229000514a7000000025d01fab0; Hm_lvt_ecd4feb5c351cc02583045a5813b5142=1560387930,1560410804; Hm_lpvt_ecd4feb5c351cc02583045a5813b5142=1560410804; gr_session_id_8187ff886f0929da=8df39e19-4f45-45d4-9dc9-97e24e967308; __utma=177678124.1209598612.1560387930.1560390200.1560410804.3; __utmz=177678124.1560410804.3.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=177678124.1.10.1560410804; gr_session_id_8187ff886f0929da_8df39e19-4f45-45d4-9dc9-97e24e967308=true',
]
