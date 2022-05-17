"""
Exercise 1 - Turn the shopping cart program into an object-oriented program¶
"""

# Create a class called cart that retains items and has methods to add, remove, and show


class Cart():
    
    def orders():
        running = True
        total = 0
        order_dict = {}
        numitems = {}
        valid_input = True

        while running == True:   
            entry = input("What would you like to order? May also 'delete', 'view', or 'quit'. ").lower()
            while entry.isalpha() == False:
                print("Letters only, please.")
                entry = input("What would you like to order? May also 'delete', 'view', or 'quit'. ").lower()
            if entry == "quit":
                for order, price in order_dict.items():
                    print(f"{numitems[order]} {order} at ${price} each, for a total of ${(float(numitems[order]) * float(price))}.")
                    total += (float(numitems[order]) * float(price))
                print(f'Your total is ${total:.2f}.')
                break
            elif entry == "delete":
                remove = input("What would you like to delete? ").lower()
                if remove not in order_dict:
                    print("Item not in cart.")
                else:
                    del order_dict[remove]
            elif entry == "view":
                for order, price in order_dict.items():
                    print(f"{numitems[order]} {order} at ${price} each, for a total of ${(float(numitems[order]) * float(price))}.")
            elif entry not in order_dict.keys():
                cost = input("How much does it cost? Input numbers only, please.")
                order_dict[entry] = cost
                numitems[entry] = 1
            else:
                numitems[entry] += 1     

Cart.orders()
#



"""
Exercise 2 - Write a Python class for an Animal that has a name and energy attributes. The animal class should also have methods for eat, sleep, and play that will take in an integer and increase/decrease the energy of the animal with a formatted print statement
"""

class Animal():
    
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy


    def sleep(self, hours):
        self.energy = self.energy + (hours * 20)
        print(f"{self.name} is sleeping for {hours} hours. Its energy is now {self.energy}.")

    def eat(self, calories):
        self.energy = self.energy + (calories * 10)
        print(f"{self.name} eats {calories} calories. Its energy is now {self.energy}.")

    def play(self, amount):
        self.energy = self.energy - (amount * 30 )
        print(f"{self.name} plays for {amount} minutes. Its energy is now {self.energy}.")
        if self.energy <= 0:
            print("Uh oh, energy is low. Better sleep or eat.")

#barkie = Animal('barkie', 100)

#barkie.sleep(20.1)
#barkie.eat(10)
#barkie.play(3000)