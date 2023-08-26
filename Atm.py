class Atm:
    # Constructor
    def __init__(self):
        self.pin = ""
        self.balance = 0


    def create_pin(self):
        if self.pin == "":
            self.pin = input("Create you pin please: ")
            print("Your pin has been set successfully")
        else:
            print("There is already a pin")

    def check_pin(self):
        pin = input("Enter your pin please: ")
        if pin == self.pin:
            return 1
        else:
            print("Pin is incorrect")
            self.check_pin()

    def deposit(self):
        if self.pin == "":
            self.create_pin()

        if self.check_pin():
            amount = input("Please enter your deposit amount: ")
            self.balance += int(amount)
            print("Amount has been deposited successfully")
        else:
            print("You have entered wrong pin")
            self.deposit()

    def withdraw(self):
        if self.pin == "":
            self.create_pin()

        if self.check_pin():
            amount = int(input("Please enter your withdrawal amount or press 0 to return to menu: "))
            if amount == 0:
                pass
            elif amount < 0:
                print("Invalid amount")
            elif self.balance >= amount:
                self.balance -= amount
                print("Amount has been withdrawn successfully")
            else:
                print("Insufficient balance")
                self.withdraw()
        else:
            print("You have entered wrong pin")
            self.withdraw()

    def check_balance(self):
        if self.pin == "":
            self.create_pin()

        if self.check_pin():
            print(f"Your current balance is : {self.balance}")
        else:
            print("You have entered wrong pin")
            self.check_balance()


def menu(object):
    user_input = int(input("""
                    0. Enter 0 to exit
                    1. Enter 1 to create pin
                    2. Enter 2 to deposit
                    3. Enter 3 to withdraw
                    4. Enter 4 to check balance
    """))

    if user_input == 1:
        object.create_pin()
    elif user_input == 2:
        object.deposit()
    elif user_input == 3:
        object.withdraw()
    elif user_input == 4:
        object.check_balance()
    elif user_input < 0 or user_input > 4:
        print("Please Enter a valid input")

    return user_input


def main():
    asiaBank = Atm()
    primeBank = Atm()

    while 1:
        choice = int(input("""Please Select your bank
        1. Asia Bank: 
        2. Prime Bank
        
        3. Exit
        """))

        if choice == 1:
            print(f"Thanks for choosing Asia Bank")
            while 1:
                stay = menu(asiaBank)
                if not stay:
                    break
        elif choice == 2:
            print(f"Thanks for choosing Prime Bank")
            while 1:
                stay = menu(primeBank)
                if not stay:
                    break
        elif choice == 3:
            break
        else:
            print("Please enter a valid choice")


main()
