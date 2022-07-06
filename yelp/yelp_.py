import requests
import lxml.html

rest_li = []


# resort_li = ['the getty center','Griffith Observatory','hollywood','Petersen Automotive Museum']

def find_restaurant(page, url,city, time=0):
    time += 1
    a = requests.get(url, proxies={'https': 'http://tunnel-proxy.crawler.svc.k8sc1.nb.com:3128'}).content.decode()
    selector = lxml.html.fromstring(a)
    xpath = '/html/head/meta[@name="description"]/@content'
    try:
        b = selector.xpath(xpath)[0]
        for item in b.split('-', 1)[1].split(','):
            rest_li.append(item)
    except:
        pass
    if time < page:
        start = time * 10
        find_restaurant(page, f"https://www.yelp.com/search?cflt=restaurants&find_loc={city}&start={start}",city,time)


def find_bars(page, url,city, time=0):
    time += 1
    a = requests.get(url, proxies={'https': 'http://tunnel-proxy.crawler.svc.k8sc1.nb.com:3128'}).content.decode()
    selector = lxml.html.fromstring(a)
    xpath = '/html/head/meta[@name="description"]/@content'
    try:
        b = selector.xpath(xpath)[0]

        for item in b.split('-', 1)[1].split(','):
            rest_li.append(item)
    except:
        pass
    if time < page:
        start = time * 10
        find_bars(page, f"https://www.yelp.com/search?cflt=bars&find_loc={city}&start={start}",city, time)


def find_nightlife(page, url, city, time=0):
    time += 1
    a = requests.get(url, proxies={'https': 'http://tunnel-proxy.crawler.svc.k8sc1.nb.com:3128'}).content.decode()
    selector = lxml.html.fromstring(a)
    xpath = '/html/head/meta[@name="description"]/@content'
    try:
        b = selector.xpath(xpath)[0]

        for item in b.split('-', 1)[1].split(','):
            rest_li.append(item)
    except:
        pass
    if time < page:
        start = time * 10
        find_nightlife(page, f"https://www.yelp.com/search?cflt=nightlifes&find_loc={city}&start={start}",city, time)


def find_shopping(page, url,city, time=0):
    time += 1
    a = requests.get(url, proxies={'https': 'http://tunnel-proxy.crawler.svc.k8sc1.nb.com:3128'}).content.decode()
    selector = lxml.html.fromstring(a)
    xpath = '/html/head/meta[@name="description"]/@content'
    try:
        b = selector.xpath(xpath)[0]
        for item in b.split('-', 1)[1].split(','):
            rest_li.append(item)
    except:
        pass
    if time < page:
        start = time * 10
        find_shopping(page, f"https://www.yelp.com/search?cflt=shppings&find_loc={city}&start={start}",city, time)


def find_resort(page, url,city, time=0):
    time += 1
    a = requests.get(url, proxies={'https': 'http://super-proxy.k8s.apne1.nb-prod.com:8899'}).content.decode()
    selector = lxml.html.fromstring(a)
    xpath = '/html/head/meta[@name="description"]/@content'
    b = selector.xpath(xpath)[0]

    for item in b.split('-', 1)[1].split(','):
        rest_li.append(item)
    if time < page:
        start = time * 10
        find_restaurant(page, f"https://www.yelp.com/search?find_desc=Restaurants&find_loc={city}&start={start}",
                        time)


def find_all(city):
    find_restaurant(24, f'https://www.yelp.com/search?cflt=restaurants&find_loc={city}', city=city)
    find_bars(24, f'https://www.yelp.com/search?cflt=bars&find_loc={city}', city=city)
    find_nightlife(24, f'https://www.yelp.com/search?cflt=nightlife&find_loc={city}', city=city)
    find_shopping(24, f'https://www.yelp.com/search?cflt=shooping&find_loc={city}', city=city)

import pandas as pd
find_all('New+York%2C+NY')
rest_li = list(set(rest_li))
column = ['name']
df = pd.DataFrame(columns=column)
df['name'] = rest_li
df.to_excel('all_yelp.xlsx')
# print(len(rest_li))
# from selenium import webdriver
# import time
# import requests
# import pandas as pd
# import re
#
# executable_path = 'C:\\Users\\赵念溪\\AppData\\Local\Google\\Chrome\\Application\\chromedriver'
# chromeOptions = webdriver.ChromeOptions()
# chromeOptions.add_argument('--proxy-server={http://super-proxy.k8s.apne1.nb-prod.com:8899}')
#
# units = {"K": 1000, "M": 1000000}
#
#
# def scroll(times, driver):
#     for time_ in range(times):
#         script = "window.scrollTo(0,10000000000);"
#         driver.execute_script(script)
#         if time_ == 0:
#             s = "window.scrollTo(document.body.scrollHeight,0);"
#             driver.execute_script(s)
#         time.sleep(2)
#
#
# def exam_time(s):
#     print(s)
#     if 'year' in s:
#         return False
#     if 'month' in s and ('10' in s or '11' in s or '12' in s):
#         return False
#     return True
#
#
# def exam_follower(follower_count):
#     try:
#         num_follower = float(follower_count)  # try to comber it to a number
#     except ValueError:
#         unit = follower_count[-1]  # get the letter
#         n = float(follower_count[:-1])  # convert all but the letter
#         num_follower = n * units[unit]
#     if num_follower >= 500 and num_follower <= 500000:
#         return True
#     return False
#
#
# def get_info(html):
#     count = len(re.findall('publishedTimeText', html))
#     follower_count = re.findall('subscriberCountText.*?"simpleText":"(.*?) subscribers"', html)[0]
#     first_v_time = re.findall('"publishedTimeText":{"simpleText":"(.*?) ago"}', html)[0]
#     print(count,follower_count,first_v_time)
#     if count > 12 and exam_follower(follower_count) and exam_time(first_v_time):
#         return True
#     return False
# def get_about_info(html):
#     description = re.findall('"description":{"simpleText":"(.*?)"}',html)[0]
#     if 'los angeles' in description.lower():
#         return True
#     return False
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/94.0.4606.81 Safari/537.36',
#     'cookies': 'VISITOR_INFO1_LIVE=HAVZUPlstgs; HSID=ACE2RbQE56JOu9S0d; SSID=Ai9mp-NBGOKWHFICn; APISID=-utZTy1w3xdt2Qai/ApKWsEzjejVdRTSWJ; SAPISID=oqTxzhb6dCeuZWsi/AxgsGgM9HqSZkCKtU; __Secure-1PAPISID=oqTxzhb6dCeuZWsi/AxgsGgM9HqSZkCKtU; __Secure-3PAPISID=oqTxzhb6dCeuZWsi/AxgsGgM9HqSZkCKtU; SID=IAhRzp435wjKI0XcD76SOdq_glUJF8muqZg780TmeryK6CqPRi6LddLB5KipTk2Q8nAfCw.; __Secure-1PSID=IAhRzp435wjKI0XcD76SOdq_glUJF8muqZg780TmeryK6CqPbEtP5WIPxBQeS-PA1Wzd_A.; PREF=f4=4000000&tz=Asia.Shanghai&gl=US&hl=en; LOGIN_INFO=AFmmF2swRQIgJO_575Z6DOGIwsu6CX55hKZQ3qbdJfLt8VzW1u4Z4qACIQC57Cc5LGTw5JWzCxlEvNvKrDTBnxJ65pUmB53jJvdwUA:QUQ3MjNmd2hPd3F5WGJIZlVOczl5MUowVjJRVU5TUFJCTkp6ZEFiOWU2eXRSaHB1cVdjc1FlZTVhdXNoY2VOUi1BNjFiQ184a1hrRXpDTGdWSVllZU13ajJNUW5PSXp3RHZtVk1vdnVWYjl4d3ptUk5LR2VTVGs4VEpMbi1MdktyOElBRHVreGxYWTE2YWd1SnNpMWp0OG9JYUwyb0dkSWh3; __Secure-3PSID=IAhRzp435wjKI0XcD76SOdq_glUJF8muqZg780TmeryK6CqPuBvVJmKdhKI6lcH6QAstxg.; YSC=XShIVN71pxM; SIDCC=AJi4QfGTyaioo2MjpyDYyRVjc3p6WWsCX_2epjclF0psW2rKGBZkq-vCij785KTsGnZKbh0CNA; __Secure-3PSIDCC=AJi4QfEeJMAkg7LVEINNXF-zXTBq17nb_LqaKyYlQSntIjMFRcd0eLQwhNyxrD64yYapPpJMPw'}
#
# # selector = lxml.html.fromstring(html)
# # print(html)
# output_dic = {'url': [], 'name': [], 'keyword': []}
# column = ['url', 'name', 'keyword']
# filter_ = set()
#
#
# def get_results(keyword):
#     driver = webdriver.Chrome(executable_path=executable_path)
#     driver.get(f'https://www.youtube.com/results?search_query=Los Angeles+"{keyword}"&sp=EgIIBQ%253D%253D')
#     # html = requests.get('https://www.youtube.com/c/Jiedel/videos', headers=headers,
#     #                             proxies={'https': 'http://super-proxy.i18n.nb.com:8899'}).content.decode()
#     # print(get_info(html))
#     #
#     scroll(5, driver)
#
#     a = driver.find_elements_by_xpath('//*[@id="text"]/a')
#     youtuber_list = []
#
#     for item in a:
#         if item.text not in filter_ and item.text:
#             filter_.add(item.text)
#             youtuber_list.append([item.get_attribute('href'), item.text])
#
#     for info in youtuber_list:
#         try:
#             html = requests.get(info[0] + '/videos', headers=headers,
#                                 proxies={'https': 'http://tunnel-proxy.crawler.svc.k8sc1.nb.com:3128'}).content.decode()
#             html_about = requests.get(info[0] + '/about', headers=headers,
#                                       proxies={'https': 'http://tunnel-proxy.crawler.svc.k8sc1.nb.com:3128'}).content.decode()
#             if get_info(html) and get_about_info(html_about):
#                 output_dic['url'].append(info[0])
#                 output_dic['name'].append(info[1])
#                 output_dic['keyword'].append(keyword)
#                 print(info)
#         except:
#             pass
#
#     driver.close()


# for i in rest_li:
#     get_results(i)
# output_df = pd.DataFrame(columns=column)
# for key in column:
#     output_df[key] = output_dic[key]
# output_df.to_excel('youtuber_info_yelp.xlsx')
# driver.get("http://httpbin.org/ip")
