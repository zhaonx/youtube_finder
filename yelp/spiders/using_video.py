import scrapy
from selenium import webdriver
import yelp.get_info_excel as yelp
import yelp.sub_loc as subloc
import time
import re
from yelp.items import YelpItem


class ExampleSpider(scrapy.Spider):
    name = 'yelp2'
    # allowed_domains = ['example.com']
    start_urls = ['http://example.com/']
    sub_li = subloc.sub_list
    rest_li = yelp.des_list
    # keyword_li = yelp.keyword_list
    executable_path = 'C:\\Users\\赵念溪\\AppData\\Local\Google\\Chrome\\chromedriver'
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument('--proxy-server=tunnel-proxy.crawler.svc.k8sc1.nb.com:3128')
    chromeOptions.add_argument('--headless')
    units = {"K": 1000, "M": 1000000}
    # filter_ = subloc.filter_
    filter_ = set()
    def handle_video(self, response):
        content = response.text
        info = response.meta['data']
        if self.get_info(content):
            try:
                yield scrapy.Request(info[0] + '/search?query=new%20york', callback=self.handle_about,
                                     meta={'data': info})
            except:
                pass

    def handle_about(self, response):
        content = response.text
        info = response.meta['data']
        if self.get_about_info(content):
            item = YelpItem()
            item['url'] = info[0]
            item['name'] = info[1]
            item['keyword'] = info[2]
            print(item)
            yield item

    def start_requests(self):
        youtuber_list = []
        for item in self.rest_li:
        # for keyword in self.keyword_li:
            driver = webdriver.Chrome(executable_path=self.executable_path, chrome_options=self.chromeOptions)
            # url = f'https://www.youtube.com/results?search_query={item} +"{keyword}"&sp=EgIIBQ%253D%253D'
            url = f'https://www.youtube.com/results?search_query=new+york++{item}&sp=EgIIBQ%253D%253D'

            driver.get(url)
            # html = requests.get('https://www.youtube.com/c/Jiedel/videos', headers=headers,
            #                             proxies={'https': 'http://super-proxy.i18n.nb.com:8899'}).content.decode()
            # print(get_info(html))
            #
            self.scroll(3, driver)

            a = driver.find_elements_by_xpath('//*[@id="text"]/a')

            for item_ in a:
                if item_.text not in self.filter_ and item_.text:
                    self.filter_.add(item_.text)
                    youtuber_list.append([item_.get_attribute('href'), item_.text, item])
            driver.close()
        for info in youtuber_list:
            try:
                yield scrapy.Request(info[0] + '/videos', callback=self.handle_video, meta={'data': info})
            except:
                pass

    @staticmethod
    def scroll(times, driver):
        for time_ in range(times):
            script = "window.scrollTo(0,10000000000);"
            driver.execute_script(script)
            if time_ == 0:
                s = "window.scrollTo(document.body.scrollHeight,0);"
                driver.execute_script(s)
            time.sleep(1)

    def get_info(self, html):
        count = len(re.findall('publishedTimeText', html))
        follower_count = re.findall('subscriberCountText.*?"simpleText":"(.*?) subscribers"', html)[0]
        first_v_time = re.findall('"publishedTimeText":{"simpleText":"(.*?) ago"}', html)[0]
        print(count, follower_count, first_v_time)
        if count > 12 and self.exam_follower(follower_count) and self.exam_time(first_v_time):
            return True
        return False

    def get_about_info(self, html):
        description = re.findall('"title":\{"runs":\[\{"text":"(.*?)"}]', html)
        print(description)
        for item in description:
            for item_ in self.sub_li:
                if item_.lower() in item.lower():
                    return True
        return False

    @staticmethod
    def exam_time(s):
        print(s)
        if 'year' in s:
            return False
        if 'month' in s and ('10' in s or '11' in s or '12' in s):
            return False

        return True

    def exam_follower(self, follower_count):
        try:
            num_follower = float(follower_count)  # try to comber it to a number
        except ValueError:
            unit = follower_count[-1]  # get the letter
            n = float(follower_count[:-1])  # convert all but the letter
            num_follower = n * self.units[unit]
        if num_follower >= 500 and num_follower <= 500000:
            return True
        return False
