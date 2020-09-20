from flask_pymongo import PyMongo, MongoClient

client = MongoClient('mongodb://mongodbSupport:27017/', username='admin', password='password')
db = client.smartDevApi