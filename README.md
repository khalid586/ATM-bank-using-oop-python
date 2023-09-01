# Introduction

**In this repository we will build a Basic programs using Object oriented programming in Python which will mainly focus on implementing 
Object oriented programming concepts.**

<br>

# Programs
We will be building following programs
- [Atm Banking System](#atm-banking-system)
    - Our Atm Banking System will have the following features
        - [Create Pin](#create-pin)
        - [Check Pin](#check-pin)
        - [Deposit Money](#deposit-money)
        - [Withdraw Money](#withdraw-money)
        - [Check Balance](#check-balance)
- Custom Datatype
    - Custom datatype which will include the following features
        - Addition
        - Substraction
        - Multiplication
        - Division
 


All the features mentioned above will be implemented using OOP as said before.

# Usage of OOP
- User will be able to transit between multiple banks at the same time which will have **different** pin codes, balanace  etc.

# Atm Banking System
The features are mentioned below

### Create Pin
We will be creating pins for every object and pin is required to perform all other operations.Without a pin no one can perform any other operation. And if pin is created then every time someone is going to perform any operation pin will be checked.

```
def __init__(self):
        self.pin = ""
        self.balance = 0

def create_pin(self):
        if self.pin == "":
            self.pin = input("Create you pin please: ")
            print("Your pin has been set successfully")
        else:
            print("There is already a pin")
```

### Check Pin
If there is a pin already existing in the program then we will check the pin everytime before performing any operation.
```
    def check_pin(self):
        pin = input("Enter your pin please: ")
        if pin == self.pin:
            return 1
        else:
            return 0
```

### Deposit Money

### Withdraw Money

### Check Balance