import scrapy
from selenium import webdriver
import pymongo
import time
import yelp.sub_loc as sub_loc
import re
from yelp.items import YoutubeItem
import langdetect

filter_word = ['radio', 'news', 'tv', 'tech', 'studio', '.net', '.com', 'foundation']


class ExampleSpider(scrapy.Spider):
    name = 'handle_collect'
    # allowed_domains = ['example.com']
    start_urls = ['http://example.com/']
    db = pymongo.MongoClient().youtube
    final_user = db.final_user
    candidate = db.candidate
    sub_list = sub_loc.sub_list

    def start_requests(self):
        for doc in self.candidate.find({"date":616}):
            check = True
            for word in filter_word:
                if word in doc['name'].lower():
                    check = False
                    break
            if check:
                yield scrapy.Request(doc['url'] + '/about', callback=self.handle, meta=doc)

    def handle(self, response):
        content = response.text
        doc = response.meta
        result = self.get_about_info(content)

        if result:
            doc['language'] = result[0]
            doc['has_keyword_in_bio'] = result[1]
            yield scrapy.Request(doc['url'] + '/videos', callback=self.handle_videos, meta=doc)

    def handle_videos(self, response):
        content = response.text
        doc = response.meta
        if self.get_query_info(content):
            item = YoutubeItem()
            doc['ts'] = 616
            doc['has_location_keyword_time_in_videos'] = self.get_query_info(content)[0]
            item['abc'] = doc
            yield item

    def get_query_info(self, html):
        description = re.findall('"title":\{"runs":\[\{"text":"(.*?)"}]', html)
        true_word = 0
        true_lang = 0
        for item in description:
            if langdetect.detect(item) == 'en':
                true_lang += 1
            for item_ in self.sub_list:
                if item_ in item.lower():
                    true_word += 1
                    break
        if true_word >= 2 and true_lang >= 2:
            return [true_word, true_lang]
        return False

    def get_about_info(self, html):
        has_keyword = False
        try:
            description = \
                re.findall('channelAboutFullMetadataRenderer":{"description":{"simpleText":"(.*?)"},"primaryLinks',
                           html)[
                    0].replace('\\n', ' ', )

            for keyword in self.sub_list:
                if keyword in description.lower():
                    has_keyword = True
                    break
            return [langdetect.detect(description), has_keyword]
        except:
            return []
