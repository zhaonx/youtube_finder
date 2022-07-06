import pymongo
db = pymongo.MongoClient().youtube
candidate = db.candidate
user_handler = db.selenium_street
name = set()
for doc in candidate.find({}):
    name.add(doc['name'])
candidate_ = []
for doc1 in user_handler.find({}):
    if doc1['name'] not in name:
        doc1['date'] = 616
        name.add(doc1['name'])
        candidate_.append(doc1)
candidate.insert_many(candidate_)
# import requests
# import re
# import langdetect
# html = requests.get('https://www.youtube.com/c/MarkWiens/about',proxies={'https': 'http://super-proxy.k8s.apne1.nb-prod.com:8899'}).content.decode()
#
#
# def get_about_info(html):
#     description = re.findall('channelAboutFullMetadataRenderer":{"description":{"simpleText":"(.*?)"},"primaryLinks', html)
#     a= description[0].replace('\\n',' ',)
#     print(langdetect.detect(a),a)
#     for item in description:
#         if 'nyc' in item.lower():
#             return True
#         if 'new york' in item.lower():
#             return True
#
#     return False
# get_about_info(html)