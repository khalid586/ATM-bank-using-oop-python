class Atm:
    # Constructor
    def __init__(self, bank_name):
        print(f"Thanks for choosing {bank_name}")
        self.pin = ""
        self.balance = 0

        self.menu()

    def menu(self):
        print("hello")
        # user_input = input("""
        #                 1. Enter 1 to create pin
        #                 2. Enter 2 to deposit
        #                 3. Enter 3 to withdraw
        #                 4. Enter 4 to check balance
        #                 5. Enter 5 to exit
        # """)
        #
        # if user_input == "1":
        #     self.create_pin()
        #     print("Your pin has been set successfully")
        # elif user_input == "2":
        #     self.deposit()
        # elif user_input == "3":
        #     self.withdraw()
        # elif user_input == "4":
        #     self.check_balance()
        # elif user_input == "5":
        #     print("Thanks for being with us.\nBye")
        # else:
        #     print("Please Enter a valid input")

    def create_pin(self):
        self.pin = input("Enter you pin please: ")

    def deposit(self):
        amount = input("Please enter your deposit amount: ")
        self.balance += int(amount)
        print("Amount has been deposited successfully")

    def withdraw(self):
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

    def check_balance(self):
        print(f"Your current balance is : {self.balance}")



prime = Atm("Prime Bank")
prime.deposit()
asia = Atm("Asia Bank")
asia .deposit()

print(prime.check_balance())
print(asia.check_balance())
# while 1:
#     BankName = int(input("""Enter choose your Bank Name please:
#                         1. Prime Bank
#                         2. Asia Bank
#                         3. Dutch Bangla Bank
#                         4. Exit
#     """))
#     if BankName == 1:
#         Prime = Atm("Prime Bank")
#     elif BankName == 2:
#         AsiaBank = Atm("Asia Bank")
#     elif BankName == 3:
#         DutchBanglaBank = Atm("Dutch Bangla Bank")
#     elif BankName == 4:
#         print("Thanks for being with us\nBye")
#         break
#     else:
#         print("Please Enter a valid input")
