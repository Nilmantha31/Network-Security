import os
import sys
import json
import certifi
import pymongo
import pandas as pd
import numpy as np
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv('MONGO_DB_URL')

ca = certifi.where()

class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json_convertor(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def inser_data_to_mongodb(self,records,database,collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)

            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]

            self.collection.insert_many(self.records)

            return len(records)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
# if __name__ == '__main__':
#     file_path = 'Network_Data\phisingData.csv'
#     database = 'NilmanthaAI'
#     collection = 'NetworkData'
#     networkobj = NetworkDataExtract()
#     records = networkobj.csv_to_json_convertor(file_path=file_path)
#     print(records)
#     no_of_records = networkobj.inser_data_to_mongodb(records=records,database=database,collection=collection)
#     print(no_of_records)