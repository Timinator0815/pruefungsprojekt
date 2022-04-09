import mysql.connector

class db:
    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="mydb"
            )
        except:
            print("Database connection error, check config, exiting...")
            exit()
    
    def getConnection(self):
        return self.mydb