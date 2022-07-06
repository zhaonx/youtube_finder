from selenium import webdriver
import time
import lxml.html
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
executable_path = 'C:\\Users\\赵念溪\\AppData\\Local\Google\\Chrome\\Application\\chromedriver'
# chromeOptions = webdriver.ChromeOptions()


user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", user_agent)
#
driver = webdriver.Firefox(firefox_profile=profile)
driver.get(
    'https://en.tripadvisor.com.hk/Attractions-g60763-Activities-a_allAttractions.true-New_York_City_New_York.html')
# a = driver.find_elements_by_xpath('//span[@name="title"]')
# driver.find_element_by_xpath('//a[@aria-label="Next page"]').click()
# for item in a:
#     name = item.find_element_by_xpath('div').text
#     print(name)
# def get_info(driver):
resort_list = []
url_list = []

def find_all(page, times=0):
    times += 1
    time.sleep(5)
    # driver.switch_to.default_content()
    # a = driver.find_elements_by_xpath()
    a = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//span[@name="title"]')))
    for item in a:
        name = item.find_element_by_xpath('div').text
        resort_list.append(name.split('.')[-1])
    try:
        if times < page and driver.find_element_by_xpath('//a[@aria-label="Next page"]'):
            driver.find_element_by_xpath('//a[@aria-label="Next page"]').click()
            # url_list.append(driver.find_element_by_xpath('//a[@aria-label="Next page"]').get_attribute('href'))
            find_all(page, times)
    except:
        pass


find_all(50)
driver.close()
# for url in url_list:
#     driver = webdriver.Chrome(executable_path=executable_path)
#     driver.get(url)
#     time.sleep(5)
#     # a = driver.find_elements_by_xpath()
#     a = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//span[@name="title"]')))
#     for item in a:
#         name = item.find_element_by_xpath('div').text
#         resort_list.append(name.split('.')[-1])
#     driver.close()
    # html = requests.get(url,proxies={'https': 'http://tunnel-proxy.crawler.svc.k8sc1.nb.com:3128'}).text

column = ['name']
df = pd.DataFrame(columns=column)
df['name'] = resort_list
df.to_excel('all_destination.xlsx')
