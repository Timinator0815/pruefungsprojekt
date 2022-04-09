import dbcon

dbcon = dbcon.db()
mydb = dbcon.getConnection()

cursor = mydb.cursor()

class customer:
    def __init__(self, username, password):
        if self.checkLogin(username, password) == True:
            self.loggedIn = True

            cursor.execute("SELECT ID, firstname, lastname FROM customers_tbl WHERE username = %s", [username])
            result = cursor.fetchall()

            self.ID = result[0][0]
            self.firstname = result[0][1]
            self.lastname = result[0][2]

            cursor.execute("SELECT bike FROM customerBikes_tbl WHERE customer = %s", [self.ID])
            self.bikes = cursor.fetchall()
        else:
            self.loggedIn = False

    def checkLogin(self, username, password):
        query = "SELECT password FROM customers_tbl WHERE username = %s"
        username = [username]
        cursor.execute(query, username)
        result = cursor.fetchall()

        if not result:
            self.wrongLogin()
            return False
        
        if result[0][0] == password:
            print("Login correct")
            return True
        else:
            self.wrongLogin()   
            return False  

    def wrongLogin(self):
        print("Username or password not valid, try again")
        inp = input("Try again? (y/n): ")
            
        if inp.lower() == "n":
            exit()      

    def getLoginStatus(self):
        return self.loggedIn

    def getBikes(self):
        return self.bikes

    def getFirstname(self):
        return self.firstname

    def getLastname(self):
        return self.lastname
    
    def getFullName(self):
        return self.firstname + " " + self.lastname
    
    def getID(self):
        return self.ID