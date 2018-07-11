import pymongo
from pymongo import MongoClient
import pandas as pd

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['local']

df = pd.DataFrame(list(db['books'].find({})))
print(df.keys())
client.close()

df['longDescription'].fillna(df['title'], inplace=True)
print(df['title'].head())