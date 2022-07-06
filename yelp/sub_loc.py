import requests
import lxml.html
import pandas as pd

# html = requests.get('https://en.wikipedia.org/wiki/List_of_cities_in_Los_Angeles_County,_California',proxies={'https': 'http://tunnel-proxy.crawler.svc.k8sc1.nb.com:3128'}).content.decode()
# selector = lxml.html.fromstring(html)
# xpath = '//*[@id="mw-content-text"]/div[1]/table/tbody/tr'
sub_list = ['bronx', 'brooklyn', 'Manhattan', 'queens', 'staten island', 'new york', 'nyc']
# for item in selector.xpath(xpath):
#     # print(item.xpath('string(.)')[0])
#     try:
#         name = item.xpath('td[1]/a/text()')[0]
#         print(name)
#         sub_list.append(name)
#     except:
#         pass
#
keyword_list = ['food', 'real estate', 'Local life', 'family', 'shopping', 'outdoor', 'local activities', 'housing']
# data = pd.read_excel('youtuber_info.xlsx')
# filter_ = set()
# for index, row in data.iterrows():
#     filter_.add(row['name'])
