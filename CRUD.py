# Project 2
# Timothy McGowan
# CS-340
# Thursday, December 12, 2024


from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps  


class CRUD(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!

        # Connection Variables
        #
        
        #USER = 'aacuser'
        #PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30620
        DB = 'AAC'
        COL = 'animals'
        
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

        print("Connection Successful")

    def create(self, data):
        """Method to implement the C in CRUD."""

        if data is not None:
            inserted = self.database.animals.insert_one(data)  

            # Checks to make sure it was successful.
            if inserted != 0:
                return True
            return False
        else:
            raise Exception("Nothing to save, data parameter is empty")

    def read(self, dataSearch):  # dataS is data to search.
        """Method to implement the R in CRUD."""

        if dataSearch is not None:
            read = self.database.animals.find(dataSearch, {"_id": False})
        else:
            raise Exception("Nothing to read, dataS parameter is empty.")
        return read

    def update(self, dataSearch, dataUpdate):
        
        """Method to implement the U in CRUD."""

        if dataSsearch and dataUpdate is not None:
            updated = self.database.animals.update_many(dataSearch, {"$set": dataUpdate})
        else:
            raise Exception("Nothing to update, dataS or data U parameters are empty.")
        return updated.modified_count

    def delete(self, dataDelete):  # dataD is data to delete.
        """Method to implement the D in CRUD."""

        if dataDelete is not None:
            deleted = self.database.animals.delete_many(dataDelete)
        else:
            raise Exception("nothing to delete, dataD parameter is empty")
        return deleted.deleted_count