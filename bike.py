import dbcon
from datetime import date

dbcon = dbcon.db()
mydb = dbcon.getConnection()
cursor = mydb.cursor()

class bike:
    def __init__(self, ID):
        self.ID = ID

        cursor.execute("""SELECT bikes_tbl.purchased,bikes_tbl.price, models_tbl.Name, manufacturers_tbl.Name
                         FROM bikes_tbl
                            inner join models_tbl on bikes_tbl.model = models_tbl.ID
                            inner join manufacturers_tbl on models_tbl.manufacturer = manufacturers_tbl.ID
                         WHERE bikes_tbl.ID = %s""",[ID])
        
        result = cursor.fetchall()
        
        self.purchaseDate = result[0][0]
        self.price = result[0][1]
        self.model = result[0][2]
        self.manufacturer = result[0][3]
    
    def getPrice(self):
        return self.price
    
    def getModel(self):
        return self.model

    def getManufacturer(self):
        return self.manufacturer

    def getFullName(self):
        return self.manufacturer + " " + self.model

    def getPurchaseDate(self):
        return self.purchaseDate
    
class tools:
    def getFreeBikes(self):
        cursor.execute("""SELECT bikes_tbl.ID, manufacturers_tbl.Name, models_tbl.Name, bikes_tbl.price FROM bikes_tbl
                            inner join models_tbl on bikes_tbl.model = models_tbl.ID
                            inner join manufacturers_tbl on models_tbl.manufacturer = manufacturers_tbl.ID
                        WHERE bikes_tbl.ID NOT IN (
                            SELECT bike from customerBikes_tbl
                            );""")
        return cursor.fetchall()
    
    def checkIfFree(self,ID):
        cursor.execute("""SELECT bikes_tbl.ID from bikes_tbl WHERE bikes_tbl.ID NOT IN (
                            SELECT bike from customerBikes_tbl) 
                            and bikes_tbl.ID = %s """,[ID])
        result = cursor.fetchall()

        if len(result) > 0:
            return True
        else:
            return False

    def assignBike(self, bikeID, custID):
        query = "INSERT INTO customerBikes_tbl(bike, customer, sold) VALUES (%s,%s,%s)"
        today = date.today()
        cursor.execute(query, [bikeID, custID, today])
        mydb.commit()

