import pymongo
import pandas as pd
db = pymongo.MongoClient().youtube
# final_user = db.selenium_street
# print(final_user.count())
final_user = db.final_user
column = ['url', 'name', 'keyword', 'has_keyword_in_bio', 'language', 'has_location_keyword_time_in_videos']
output_dic = {'url': [], 'name': [], 'keyword': [], 'has_keyword_in_bio': [], 'language': [], 'has_location_keyword_time_in_videos': []}
for item in final_user.find({"ts":616}):
    for i in column:
        output_dic[i].append(item[i])


output_df = pd.DataFrame(columns=column)
for i in column:
    output_df[i] = output_dic[i]
output_df.to_excel('ytb-6-16.xlsx',index=False)