import pandas as pd
data = pd.read_excel('all_yelp.xlsx')
des_list = []
for index,row in data.iterrows():
    des_list.append(row['name'])
