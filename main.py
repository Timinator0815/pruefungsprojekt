import customer
import bike
import os

class GUI:
    def __init__(self):
        self.clearScreen()
        print("Please login:")
        username = input("Username: ")
        password = input("Password: ")
        self.cust = customer.customer(username, password)

        if self.cust.getLoginStatus() == False:
            gui = GUI()
        
        self.mainmenu(True)
    
    def mainmenu(self, first = False):
        if first == True:
            self.clearScreen()
            print("Welcome " + self.cust.getFullName())

        options = {'1':'List my bikes', '2':'Buy a free bike', '3':'Exit'}

        for option in options:
            print("[" + option + "] = " + options[option])

        inp = input("Input your choice: ")
        
        if inp not in options:
            self.clearScreen()
            print("Invalid input, try again...")
            self.mainmenu()
     
        inp = int(inp)
        if inp == 1:
            self.listBikes()
        elif inp == 2:
            self.buyBike()
        elif inp == 3:
            exit()
    
    
    def listBikes(self):
        self.clearScreen()
        bikes = self.cust.getBikes()
        if len(bikes) > 0:
            cnt = 1
            print("Number\tName\t\t\t\tPrice\tPurchased on")
            for x in bikes:
                bikeDetails = bike.bike(x[0])
                print(str(cnt) + "\t" + bikeDetails.getFullName() + "\t\t" + str(bikeDetails.getPrice()) + "€\t" + str(bikeDetails.getPurchaseDate()))
                cnt += 1
        else:
            print("You have no bikes")
        
        print("\r\r")
        input("Press Enter to get to the main menu: ")
        self.mainmenu(True)

    def buyBike(self):
        self.clearScreen()
        bikes = bike.tools().getFreeBikes()
        if len(bikes) > 0:
            print("ID\tName\t\t\t\tPrice")

            for x in bikes:
                print(str(x[0]) + "\t" + x[1] + " " + x[2] + "\t\t" + str(x[3]))
            
            inp = input("\r\rEnter the ID of the bike you want to aquire: ")

            if input("\rReally buy bike " + inp + " (y/n): ").lower() == "y":
                if bike.tools().checkIfFree(int(inp)) == True:
                    bike.tools().assignBike(inp, self.cust.getID())
                    print("You are now the owner of this bike!\r\r\r")
                    input("Press Enter to get to the main menu: ")
                    self.mainmenu()
                else:
                    self.clearScreen()
                    print("Invalid Bike ID, try again..\r\r")
                    self.buyBike()
        else:
            print("There are no bikes available atm\r")
            input("Press Enter to get to the main menu: ")
            self.mainmenu(True)

    def clearScreen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    gui = GUI()