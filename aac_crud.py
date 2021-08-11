#     Program: Austin Animal Shelter CRUD
#      Author: Drew Townsend
#        Date: 08/05/21
# Description: Module connects to MongoDB and allows users to utilize CRUD functionality

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:37889/AAC' % (username, password))
        self.database = self.client['AAC']
        # print("done")

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary
            print("True")
        else:
            raise Exception("False")

# Create method to implement the R in CRUD. 
    def read(self, data):
        if data is not None:
            # Leaving out ObjectID for Pandas DataFrame
            return self.database.animals.find(data, { '_id': 0} )
                
        else:
             raise Exception("Parameters returned no records")
                
# Update item based on parameter, which is the U in CRUD.
    def update(self, query, data):
        if data is not None:
            self.database.animals.update_many(query, data)
            print("Updated")
            for x in self.database.animals.find(query):
                print(x)
        else:
            raise Exception("Couldn't update record")
            
# Delete record based on parameter, which is the D in CRUD.
    def delete(self, data):
        if data is not None:
            self.database.animals.delete_many(data)
            for x in self.database.animals.find(data):
                print(x)
        else:
            raise Exception("Couldn't find record to delete")
