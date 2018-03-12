import sqlite3

#TODO: create the database class
class Database: 

    connection = None
    cursor = None

    def __init__(self):
        self.connection = sqlite3.connect('data.db')
        self.cursor = self.connection.cursor()
    
    #TODO: create the database code 
    def createDataBase(self):
        
