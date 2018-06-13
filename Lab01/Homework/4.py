from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin123@ds035593.mlab.com:35593/minhth-c4e18-lab"

client = MongoClient(mongo_uri)

db = client.get_default_database()

customers = db['customers']

all_customer = customers.find()

import matplotlib
matplotlib.use("TkAgg")
