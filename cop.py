#lieutenant serves as input validation
class Cop:
    
    def __int__(self , quantity):
        self.quantity = quantity

    def setQuantity(self , quantity):
        self.quantity = quantity

    def verify(self):
        counter = 0
        while True:
            try:
                if counter < 1:
                    value = int(self.quantity)

                else:
                    value = int(input("Please try entering 1 or 2. "))

                while value < 1 or value > 2:
                    print("Invalid entry; please try again.")
                    value = int(input("Please try entering 1 or 2. "))

            except ValueError:
                #reset to if statement
                counter = counter + 1
                print("Nice try bruh.")
                continue

            else:
                break

        return value

