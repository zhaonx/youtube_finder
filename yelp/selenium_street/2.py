from selenium import webdriver
import time

executable_path = 'C:\\Users\\赵念溪\\AppData\\Local\Google\\Chrome\\chromedriver'
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--proxy-server=tunnel-proxy.crawler.svc.k8sc1.nb.com:3128')
chromeOptions.add_argument('--headless')

import requests
import lxml.html
import pymongo

db = pymongo.MongoClient().youtube
selenium_street = db.selenium_street
rest_li = []
already = set(selenium_street.distinct('username'))
a = requests.get('https://geographic.org/streetview/usa/ny/bronx.html',
                 proxies={'https': 'http://tunnel-proxy.crawler.svc.k8sc1.nb.com:3128'}).content.decode()
selector = lxml.html.fromstring(a)
xpath = '//span[@class="listspan"]/ul/li'
for item in selector.xpath(xpath):
    name = item.xpath('a/text()')[0]
    rest_li.append(name + ' bronx')


def scroll(times, driver):
    for time_ in range(times):
        script = "window.scrollTo(0,10000000000);"
        driver.execute_script(script)
        if time_ == 0:
            s = "window.scrollTo(document.body.scrollHeight,0);"
            driver.execute_script(s)
        time.sleep(0.5)


import pymongo

for item in rest_li:
    try:
        driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chromeOptions)

        driver.get(f'https://www.youtube.com/results?search_query={item}&sp=EgIIBQ%253D%253D')
        # html = requests.get('https://www.youtube.com/c/Jiedel/videos', headers=headers,
        #                             proxies={'https': 'http://super-proxy.i18n.nb.com:8899'}).content.decode()
        # print(get_info(html))
        #
        scroll(1, driver)

        a = driver.find_elements_by_xpath('//*[@id="text"]/a')

        for item_ in a:
            if item_.text and item_.text not in already:
                already.add(item_.text)
                selenium_street.insert_one({'url': item_.get_attribute('href'), 'name': item_.text, 'keyword': item})
                # youtuber_list.append([item_.get_attribute('href'), item_.text, item])
        driver.close()
    except:
        pass
